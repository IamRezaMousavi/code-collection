#!/bin/sh

echo "Updating system..."
sudo pacman -Syu --noconfirm

if ! command -v yay > /dev/null; then
    echo "yay not found. Installing yay..."
    sudo pacman -S --needed --noconfirm git base-devel
    tmpdir=$(mktemp -d)
    git clone https://aur.archlinux.org/yay.git "$tmpdir/yay"
    cd "$tmpdir/yay" || exit
    makepkg -si --noconfirm
    cd - || exit
    rm -rf "$tmpdir"
else
    echo "yay is already installed."
fi

echo "Installing core packages with pacman..."
sudo pacman -S --noconfirm \
    firefox git \
    go \
    tmux neovim \
    fastfetch onefetch \
    linux-firmware-qlogic \
    ufw traceroute whois \
    nmap wireshark-qt scapy \
    vlc fwupd \
    p7zip unrar \
    gnome-terminal alacritty \
    otf-comicshanns-nerd \
    power-profiles-daemon \
    zsh eza pkgfile starship bat \
    zsh-syntax-highlighting zsh-autosuggestions \
    samba \
    hyperfine \
    thunderbird \
    cups cups-pdf \
    man-db \
    jdk-openjdk \
    nodejs npm \
    mariadb \
    libreoffice-fresh \
    bitwarden \
    freeplane \
    inkscape \
    gnu-free-fonts ttf-opensans ttf-linux-libertine ttf-gentium-plus \
    ntfs-3g \
    alsa-utils alsa-plugins alsa-firmware \
    irqbalance \
    jq \
    ruff \
    jupyter-notebook \
    nginx \
    obs-studio \
    qbittorrent \
    virtualbox virtualbox-host-modules-arch virtualbox-guest-iso \
    arm-none-eabi-gcc arm-none-eabi-newlib \
    openocd \
    arduino-ide \
    docker \
    chrony \
    pacman-contrib



echo "Installing AUR packages with yay..."
yay -S --noconfirm \
    upd72020x-fw ast-firmware aic94xx-firmware wd719x-firmware \
    tray-icons-reloaded \
    auto-cpufreq \
    borna-fonts iran-nastaliq-fonts \
    visual-studio-code-bin \
    localsend-bin \
    marktext-bin \
    vazirmatn-fonts ttf-joypixels otf-openmoji noto-fonts-emoji \
    ttf-mononoki ttf-monaco otf-hermit ttf-hack iranian-fonts ttf-tahoma borna-fonts iran-nastaliq-fonts

echo "Enabling services..."
sudo systemctl enable power-profiles-daemon.service
sudo systemctl start power-profiles-daemon.service

sudo systemctl enable auto-cpufreq.service
sudo systemctl start auto-cpufreq.service

sudo systemctl enable cups.socket
sudo systemctl start cups.socket

sudo systemctl enable paccache.timer
sudo systemctl start paccache.timer

echo "Updating pkgfile database..."
sudo pkgfile --update

echo "Installation and setup complete!"
