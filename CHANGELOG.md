# Changelog - Universal Project Launcher

## [2.2.0] - 2026-04-10
### Added
- **Windows Robustness Standards (Mandatory)**: 
    - Forced `set PYTHONUTF8=1` in all generated launchers.
    - Mandatory absolute path referencing using `"%~dp0"` with double quotes.
    - Pure linear execution in `.bat` (removed all `if/else` logic to prevent CMD silent crashes).
    - Removed all Emoji and non-ASCII characters from launcher source.
- **GUI Defensive Patterns**:
    - Added security audit checks for `app.update()` before `mainloop()`.
    - Mandatory `try...except` blocks for hardware-dependent libraries (e.g., `pyttsx3`, `ttk.Style`).

## [2.1.0] - 2026-04-09
### Added
- **Robust Launcher Generation**: Simplified `.bat` creation logic to prevent Windows encoding/syntax crashes.
- **Unicode Support**: Added `chcp 65001`, `PYTHONUTF8=1`, and `PYTHONIOENCODING=utf-8` to ensuring all characters display correctly in CMD.
- **Fail-Safe UI**: Added mandatory `pause` at the end of launchers to keep error messages visible.
- **Auto-Browser Open**: Integrated automatic browser launch for Streamlit projects with a 5-second delay to ensure server readiness.

### Fixed
- **CMD Crash (Encoding)**: Removed non-English comments and complex loops in `.bat` that caused crashes in certain Windows locales.
- **Streamlit Launch Mode**: Optimized launcher to use `python -m streamlit run` for higher stability across virtual environments.

## [2.0.0] - 2026-04-09
### Added
- **PowerShell Syntax Support**: Added mandatory `&` operator rule in `SKILL.md` for executable path resolution in Windows environments.
- **Shell Compatibility Principle**: Defined clear boundaries between CMD (.bat) and PowerShell (Agent execution) syntax.

### Fixed
- **create_launcher.py (Argument Parsing)**: Replaced positional `sys.argv` with `argparse` to prevent misidentifying CLI flags as project names.
- **Launcher Template**: Improved `.bat` generation to include virtual environment validation and non-blocking `start` execution for GUI apps.
