#!/usr/bin/env bash
# backup-git-repos.sh
#
# Recursively find Git repositories, create bundles, and compress them
# with tar.xz while preserving the directory tree in the destination.
#
# Usage:
#   ./backup-git-repos.sh [SRC_DIR] [DEST_DIR]
#
# Optional env vars:
#   COMPRESSOR=xz      # xz (default) | gz | zstd | none
#   XZ_LEVEL=6         # xz compression level: 0-9 (default 6)
#   KEEP_BUNDLE=0      # 1 = keep the raw bundle file too (default: delete)

set -euo pipefail

# -------- Settings --------
SRC_DIR="${1:-.}"
DEST_DIR="${2:-./git-backups}"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

COMPRESSOR="${COMPRESSOR:-xz}"        # xz | gz | zstd | none
XZ_LEVEL="${XZ_LEVEL:-6}"             # 0..9
KEEP_BUNDLE="${KEEP_BUNDLE:-0}"       # 0 = delete raw bundle

# -------- Colors --------
if [[ -t 1 ]]; then
    RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; YELLOW=$'\033[1;33m'
    BLUE=$'\033[0;34m'; CYAN=$'\033[0;36m'
    BOLD=$'\033[1m'; RESET=$'\033[0m'
else
    RED=""; GREEN=""; YELLOW=""; BLUE=""; CYAN=""; BOLD=""; RESET=""
fi

# -------- Pre-flight checks --------
[[ -d "$SRC_DIR" ]] || { echo "${RED}Error: source directory does not exist: $SRC_DIR${RESET}" >&2; exit 1; }
command -v git >/dev/null 2>&1 || { echo "${RED}Error: git is not installed${RESET}" >&2; exit 1; }

# Verify compressor availability
case "$COMPRESSOR" in
    xz)   command -v xz   >/dev/null || { echo "${RED}Error: xz is not installed${RESET}" >&2; exit 1; } ;;
    gz)   command -v gzip >/dev/null || { echo "${RED}Error: gzip is not installed${RESET}" >&2; exit 1; } ;;
    zstd) command -v zstd >/dev/null || { echo "${RED}Error: zstd is not installed${RESET}" >&2; exit 1; } ;;
    none) : ;;
    *)    echo "${RED}Error: invalid COMPRESSOR: $COMPRESSOR${RESET}" >&2; exit 1 ;;
esac

mkdir -p "$DEST_DIR"
SRC_DIR=$(cd "$SRC_DIR" && pwd)
DEST_DIR=$(cd "$DEST_DIR" && pwd)

# -------- Determine extension and compression flags --------
case "$COMPRESSOR" in
    xz)   EXT="tar.xz";   TAR_FLAGS=(-I "xz -T0 -${XZ_LEVEL}") ;;
    gz)   EXT="tar.gz";   TAR_FLAGS=(-I "gzip -9") ;;
    zstd) EXT="tar.zst";  TAR_FLAGS=(-I "zstd -19 -T0") ;;
    none) EXT="tar";      TAR_FLAGS=() ;;
esac

echo "${BOLD}Source      :${RESET} $SRC_DIR"
echo "${BOLD}Destination :${RESET} $DEST_DIR"
echo "${BOLD}Compressor  :${RESET} $COMPRESSOR  (extension: .$EXT)"
echo "${BOLD}Timestamp   :${RESET} $TIMESTAMP"
echo

# -------- Counters (while loop runs in a subshell, so use a temp file) --------
TMP_STATS=$(mktemp)
trap 'rm -f "$TMP_STATS"' EXIT
echo "0 0 0 0" > "$TMP_STATS"   # total ok fail bytes

# -------- Main loop --------
find "$SRC_DIR" -type d -name ".git" -prune -print0 |
while IFS= read -r -d '' git_dir; do
    repo_dir=$(dirname "$git_dir")

    rel_path="${repo_dir#"$SRC_DIR"/}"
    [[ "$rel_path" == "$repo_dir" ]] && rel_path=$(basename "$repo_dir")

    base=$(basename "$rel_path")
    parent=$(dirname "$rel_path")
    [[ "$parent" == "." ]] && parent=""

    target_dir="$DEST_DIR/$parent"
    mkdir -p "$target_dir"

    short_sha=$(git -C "$repo_dir" rev-parse --short HEAD 2>/dev/null || echo "nosha")

    # Temp and final files
    tmp_dir=$(mktemp -d)
    bundle_file="$tmp_dir/${base}.bundle"
    archive_name="${base}__${TIMESTAMP}__${short_sha}.${EXT}"
    out_file="$target_dir/$archive_name"
    rel_out="${out_file#"$DEST_DIR"/}"

    printf "${BLUE}-->  %-40s${RESET} " "$rel_path"

    # --- 1) Create bundle ---
    if ! git -C "$repo_dir" bundle create "$bundle_file" --all >/dev/null 2>&1; then
        printf "${RED}FAILED to create bundle${RESET}\n"
        rm -rf "$tmp_dir"
        read -r t o f b < "$TMP_STATS"; echo "$((t+1)) $o $((f+1)) $b" > "$TMP_STATS"
        continue
    fi

    bundle_size=$(stat -c%s "$bundle_file" 2>/dev/null || stat -f%z "$bundle_file")

    # --- 2) Compress ---
    if [[ "$COMPRESSOR" == "none" ]]; then
        mv "$bundle_file" "$out_file"
        final_size=$bundle_size
    else
        # -C makes the archive store just the basename
        if ! tar -cf - "${TAR_FLAGS[@]}" -C "$tmp_dir" "${base}.bundle" 2>/dev/null | \
             cat > "$out_file"; then
            if ! tar -c "${TAR_FLAGS[@]}" -C "$tmp_dir" -f "$out_file" "${base}.bundle"; then
                printf "${RED}FAILED to compress${RESET}\n"
                rm -rf "$tmp_dir" "$out_file"
                read -r t o f b < "$TMP_STATS"; echo "$((t+1)) $o $((f+1)) $b" > "$TMP_STATS"
                continue
            fi
        fi
        final_size=$(stat -c%s "$out_file" 2>/dev/null || stat -f%z "$out_file")

        # Optionally keep the raw bundle alongside
        if [[ "$KEEP_BUNDLE" == "1" ]]; then
            cp "$bundle_file" "$target_dir/${base}__${TIMESTAMP}__${short_sha}.bundle"
        fi
    fi

    rm -rf "$tmp_dir"

    # --- 3) Report ---
    human_final=$(numfmt --to=iec --suffix=B "$final_size" 2>/dev/null || echo "${final_size}B")
    if [[ "$COMPRESSOR" == "none" ]]; then
        printf "${GREEN}OK   %s (%s)${RESET}\n" "$rel_out" "$human_final"
    else
        human_bundle=$(numfmt --to=iec --suffix=B "$bundle_size" 2>/dev/null || echo "${bundle_size}B")
        ratio=$(awk -v a="$bundle_size" -v b="$final_size" 'BEGIN{ if(a>0) printf "%.0f%%", (1-b/a)*100; else print "0%" }')
        printf "${GREEN}OK   %s  ${CYAN}[%s -> %s, saved %s]${RESET}\n" \
               "$rel_out" "$human_bundle" "$human_final" "$ratio"
    fi

    read -r t o f b < "$TMP_STATS"
    echo "$((t+1)) $((o+1)) $f $((b+final_size))" > "$TMP_STATS"
done

# -------- Summary --------
read -r total ok fail total_bytes < "$TMP_STATS"
echo
echo "${BOLD}--- Summary ---${RESET}"
echo "  Total repos    : $total"
echo "  Succeeded      : ${GREEN}$ok${RESET}"
[[ "$fail" -gt 0 ]] && echo "  Failed         : ${RED}$fail${RESET}" || echo "  Failed         : 0"
human_total=$(numfmt --to=iec --suffix=B "$total_bytes" 2>/dev/null || echo "${total_bytes}B")
echo "  Total size     : $human_total"
echo
echo "${GREEN}Done.${RESET} Destination: $DEST_DIR"

