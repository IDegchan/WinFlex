import winreg
import os

def change_highlight_color(red: int, green: int, blue: int):
    key = r"Control Panel\Colors"
    HilightColor = f"{red} {green} {blue}" #Default: 0 120 215
    HotTrackingColor = f"{red-20} {green-20} {blue-20}" #Default: 0 102 204

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as regkey:
        winreg.SetValueEx(regkey, "Hilight", 0, winreg.REG_SZ, HilightColor)
        winreg.SetValueEx(regkey, "HotTrackingColor", 0, winreg.REG_SZ, HotTrackingColor)

    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

change_highlight_color(125, 125, 125)