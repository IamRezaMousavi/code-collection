# Shell

A shell is a computer program that exposes an operating system's services
to a human user or other programs. In general, operating system shells
use either a command-line interface (CLI) or graphical user interface (GUI),
depending on a computer's role and particular operation. It is named a shell
because it is the outermost layer around the operating system.
[wikipedia](https://en.wikipedia.org/wiki/Shell_(computing))

- [Bash](https://www.gnu.org/software/bash/):
  Bash is the GNU Project's shell—the Bourne Again SHell.
  [source-code](https://git.savannah.gnu.org/cgit/bash.git) `GPL-3.0-or-later` `C`
      - arch: `bash`

- [Zsh](https://www.zsh.org/):
  Zsh is a shell designed for interactive use,
  although it is also a powerful scripting language.
  [source-code](https://sf.net/p/zsh/code/) `MIT-Modern-Variant` `C`
      - arch: `zsh`

- [Powershell](https://microsoft.com/PowerShell):
  PowerShell is a cross-platform (Windows, Linux, and macOS)
  automation and configuration tool/framework that works well
  with your existing tools and is optimized for
  dealing with structured data (e.g. JSON, CSV, XML, etc.),
  REST APIs, and object models.
  [github](https://github.com/PowerShell/PowerShell) `MIT` `C#`
      - aur: `powershell`

- To change default shell

    ```bash
    chsh -s <full-path-to-shell>
    ```

- [Starship](https://starship.rs/):
  The minimal, blazing-fast, and infinitely customizable prompt for any shell!
  [github](https://github.com/starship/starship) `ISC license` `Rust`
  - arch: `starship`
