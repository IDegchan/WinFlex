from pathlib import Path
import subprocess
import winreg

class Tool:
    HOME = Path.home()
    FILEPATH = Path(__file__).resolve().parent

    @staticmethod
    def run_command(command: str):
        subprocess.run(["powershell", "-Command", command], capture_output=True)

class Highlight(Tool):
    DEFAULT_HILIGHT = "0 120 215"
    DEFAULT_HOTTRACK = "0 102 204"
    REG_PATH = r"Control Panel\Colors"

    @staticmethod
    def _set_color(key: str, value: str):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, Highlight.REG_PATH, 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, key, 0, winreg.REG_SZ, value)
        Tool.run_command("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

    def change(self, red: int, green: int, blue: int):
        adjust = lambda x: max(1, x - 20)
        self._set_color("Hilight", f"{red} {green} {blue}")
        self._set_color("HotTrackingColor", f"{adjust(red)} {adjust(green)} {adjust(blue)}")

    def reset(self):
        self._set_color("Hilight", self.DEFAULT_HILIGHT)
        self._set_color("HotTrackingColor", self.DEFAULT_HOTTRACK)

class ExplorerBlur(Tool):
    def init(self):
        self.run_command("src\\progs\\ExplorerBlur\\register.cmd")

class Console(Tool):
    POWERSHELL_PROFILE_PATH = Tool.HOME / "Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1"
    WINDOWS_TERMINAL_PATH = next(Tool.HOME.glob("AppData/Local/Packages/Microsoft.WindowsTerminal*/LocalState/settings.json"), None)

    def init(self):
        self.run_command("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser")
        self.run_command("winget install --id Microsoft.WindowsTerminal -e")
        self.run_command("winget install --id Microsoft.Powershell --source winget")
        self.run_command("irm get.scoop.sh | iex")
        self.run_command("scoop install winfetch")

        with open("src\\progs\\Console\\settings.json", "r", encoding="utf-8") as readable_file:
            with open(self.WINDOWS_TERMINAL_PATH, "w", encoding="utf-8") as writable_file:
                writable_file.write(readable_file.read())

        with open("src\\progs\\Console\\Microsoft.PowerShell_profile.ps1", "r", encoding="utf-8") as readable_file:
            with open(self.POWERSHELL_PROFILE_PATH, "w", encoding="utf-8") as writable_file:
                writable_file.write(readable_file.read())

        self.run_command("wt")
