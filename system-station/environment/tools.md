# Tools

## Environment

- Desktop: In computing, a desktop environment (DE) is an implementation of the desktop metaphor made of a bundle of programs running on top of a computer operating system that share a common graphical user interface (GUI), sometimes described as a graphical shell. [wikipedia](https://en.wikipedia.org/wiki/Desktop_environment)

- CLI: A command-line interface (CLI) is a means of interacting with a device or computer program with commands from a user or client, and responses from the device or program, in the form of lines of text. [wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)

---

## Softwares

### Benchmarking

Benchmarking is the practice of comparing business processes and performance metrics to industry bests and best practices from other companies. Dimensions typically measured are quality, time and cost. [wikipedia](https://en.wikipedia.org/wiki/Benchmarking)

- hyperfine: A command-line benchmarking tool. [github](https://github.com/sharkdp/hyperfine) `Apache-2.0, MIT` `Rust`
  - arch: `hyperfine`

### Bittorrent

BitTorrent is a communication protocol for peer-to-peer file sharing (P2P), which enables users to distribute data and electronic files over the Internet in a decentralized manner. [wikipedia](https://en.wikipedia.org/wiki/BitTorrent)

- [qbittorrent](https://www.qbittorrent.org/): qBittorrent is a cross-platform free and open-source BitTorrent client written in native C++. It relies on Boost, Qt 6 toolkit and the libtorrent-rasterbar library, with an optional search engine written in Python. [github](https://github.com/qbittorrent/qBittorrent) `GPL-3.0` `C++`
  - arch: `qbittorrent`

### Email

Electronic mail (email or e-mail) is a method of transmitting and receiving messages using electronic devices. [wikipedia](https://en.wikipedia.org/wiki/Email)

- [thunderbird](https://www.thunderbird.net/): Mozilla Thunderbird is a free and open-source cross-platform email client, personal information manager, news client, RSS and chat client that is operated by the Mozilla Foundation's subsidiary MZLA Technologies Corporation. [source-code](https://hg.mozilla.org/comm-central) `MPL-2.0` `C`
  - arch: `thunderbird`

### File Management

- bat: A cat(1) clone with syntax highlighting and Git integration. [github](https://github.com/sharkdp/bat) `Apache-2.0 and MIT` `Rust`
  - arch: `bat`

- [eza](https://the.exa.website/):  A modern replacement for `ls`. [github](https://github.com/eza-community/eza) `MIT` `Rust`
  - aur: `eza`

#### File Archiver

- p7zip: 7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as "archives". [github](https://github.com/p7zip-project/p7zip) `LGPL-2.1-or-later` `C`
  - arch: `p7zip`

### Game

- [nudoku](http://jubalh.github.io/nudoku/): nudoku is a ncurses based sudoku game. [github](https://github.com/jubalh/nudoku) `GPL-3.0` `C`
  - aur: `nudoku`

### Media Player

Media player software is a type of application software for playing multimedia computer files like audio and video files. [wikipedia](https://en.wikipedia.org/wiki/Media_player_software)

- [vlc](https://www.videolan.org/vlc/): VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files, and various streaming protocols. [source-code](https://code.videolan.org/videolan/vlc) `GPL-2.0-or-later` `C-C++`
  - arch: `vlc`

### Office

An office suite is a bundle of productivity software (a software suite) intended to be used by office workers. [wikipedia](https://en.wikipedia.org/wiki/Productivity_software#Office_suite)

- [libreoffice](https://www.libreoffice.org/): LibreOffice is a free and powerful office suite [source-code](https://git.libreoffice.org/core) `MPL-2.0` `C++`
  - arch: `libreoffice-fresh`

### Password Manager

A password manager is a computer program that allows users to store. Password managers can generate passwords and fill online forms. [wikipedia](https://en.wikipedia.org/wiki/Password_manager)

- [Bitwarden (Client)](https://bitwarden.com/): Bitwarden is an integrated open source password management solution for individuals, teams, and business organizations. [github](https://github.com/bitwarden/clients) `GPL-3.0-only` `Typescript`
  - arch: `bitwarden`

### Screen Recorder

A screencast is a digital recording of computer screen output, also known as a video screen capture or a screen recording, often containing audio narration. [wikipedia](https://en.wikipedia.org/wiki/Screencast)

- [OBS Studio](https://obsproject.com/): Free and open source software for live streaming and screen recording. [github](https://github.com/obsproject/obs-studio) `GPL-2.0-or-later` `C`
  - arch: `obs-studio`

### System Information

- neofetch: Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way. [github](https://github.com/dylanaraps/neofetch) `MIT` `Bash`
  - arch: `neofetch`

- fastfetch: Fastfetch is a neofetch-like tool for fetching system information and displaying them in a pretty way. It is written mainly in C, with performance and customizability in mind. Currently, Linux, Android, FreeBSD, MacOS and Windows 7+ are supported. [github](https://github.com/fastfetch-cli/fastfetch) `MIT` `C`
  - arch: `fastfetch`

### Terminal Multiplexer

- [tmux](https://github.com/tmux/tmux/wiki): tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. [github](https://github.com/tmux/tmux) `ISC` `C`
  - arch: `tmux`

### Version Control

In software engineering, version control is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management. [wikipedia](https://en.wikipedia.org/wiki/Version_control)

- [Git](https://git-scm.com/): Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. [source-code](https://git.kernel.org/pub/scm/git/git.git) `GPL-2.0-only` `C`
  - arch: `git`

- [onefetch](https://onefetch.dev/): Onefetch is a command-line Git information tool that displays project information and code statistics for a local Git repository directly to your terminal. [github](https://github.com/o2sh/onefetch) `MIT` `Rust`
  - arch: `onefetch`

### Virtualization

Virtualization is the act of creating a virtual version of something at the same abstraction level, including virtual computer hardware platforms, storage devices, and computer network resources. [wikipedia](https://en.wikipedia.org/wiki/Virtualization)

- [docker](https://www.docker.com/): Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. [github](https://github.com/moby/moby) `Apache-2.0` `Go`
  - arch: `docker`

- [virtualbox](https://www.virtualbox.org/): VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. [source-code](https://www.virtualbox.org/browser/vbox/trunk) `GPL-3.0` `C++`
  - arch: `virtualbox` (`virtualbox-host-modules-arch`)
  - arch: `virtualbox-guest-iso`

---
