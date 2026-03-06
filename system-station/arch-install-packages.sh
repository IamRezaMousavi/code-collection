#!/bin/sh

echo "Updating system..."
sudo pacman -Syu --noconfirm

if ! command -v yay > /dev/null; then
    echo "yay not found. Installing yay..."
    sudo pacman -S --needed --noconfirm git base-devel
    tmpdir=$(mktemp -d)
    git clone https://aur.archlinux.org/yay-bin.git "$tmpdir/yay-bin"
    cd "$tmpdir/yay-bin" || exit
    makepkg -si --noconfirm
    cd - || exit
    rm -rf "$tmpdir"
else
    echo "yay is already installed."
fi

echo "Installing core packages with pacman..."
sudo pacman -S --noconfirm \
    firefox \
    libreoffice-fresh \
    git lazygit \
    neovim tmux less \
    fastfetch onefetch \
    ufw \
    7zip zip unrar rsync \
    alacritty \
    power-profiles-daemon \
    eza starship bat \
    zsh zsh-syntax-highlighting zsh-autosuggestions pkgfile \
    cups cups-pdf \
    man-db \
    cmake cppcheck nlohmann-json spdlog tomlplusplus \
    ipython python-numpy python-pandas ruff \
    jdk17-openjdk \
    nodejs npm \
    rustup \
    go \
    mariadb \
    bitwarden \
    inkscape \
    gnu-free-fonts ttf-roboto ttf-opensans ttf-linux-libertine ttf-gentium-plus ttf-scheherazade-new noto-fonts noto-fonts-emoji \
    otf-comicshanns-nerd \
    ntfs-3g \
    irqbalance \
    nginx \
    virtualbox virtualbox-host-modules-arch virtualbox-guest-iso \
    arm-none-eabi-gcc arm-none-eabi-newlib \
    openocd \
    docker docker-compose \
    pacman-contrib reflector \
    gnome-shell-extensions \
    wireshark-qt nmap scapy openbsd-netcat \
    logrotate \
    vlc vlc-plugins-all

echo "Installing AUR packages with yay..."
yay -S --noconfirm \
    borna-fonts iran-nastaliq-fonts \
    visual-studio-code-bin \
    localsend-bin \
    vazirmatn-fonts otf-openmoji \
    bibata-cursor-theme-bin

fc-cache

chsh -l
chsh -s /usr/bin/zsh

sudo usermod -aG docker reza
sudo usermod -aG wireshark reza
sudo usermod -aG vboxusers reza

echo "Enabling services..."
sudo systemctl enable --now power-profiles-daemon
sudo systemctl enable --now cups.socket
sudo systemctl enable --now ufw
sudo systemctl enable --now docker.socket
sudo systemctl enable --now paccache.timer
sudo systemctl enable --now reflector.timer
sudo systemctl enable --now irqbalance
sudo systemctl enable --now logrotate.timer
sudo ufw enable

echo "Updating pkgfile database..."
sudo pkgfile --update

rustup default stable

echo "Installation and setup complete!"
