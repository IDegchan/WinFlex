import winreg
import os

class Highlight:
    DEFAULT_HILIGHT = "0 120 215"
    DEFAULT_HOTTRACK = "0 102 204"
    REG_PATH = r"Control Panel\Colors"

    def __init__(self, red: int, green: int, blue: int):
        self.r, self.g, self.b = red, green, blue

    @staticmethod
    def _set_color(key: str, value: str):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, Highlight.REG_PATH, 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, key, 0, winreg.REG_SZ, value)
        os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

    def change(self):
        adjust = lambda x: max(1, x - 20)
        self._set_color("Hilight", f"{self.r} {self.g} {self.b}")
        self._set_color("HotTrackingColor", f"{adjust(self.r)} {adjust(self.g)} {adjust(self.b)}")

    def reset(self):
        self._set_color("Hilight", self.DEFAULT_HILIGHT)
        self._set_color("HotTrackingColor", self.DEFAULT_HOTTRACK)

if __name__ == "__main__":
    Highlight(0, 255, 115).change()
