import winreg, os

class Highlight:
    def __init__(self, red: int, green: int, blue: int):
        self.r = red
        self.g = green
        self.b = blue

    def change(self):
        red = self.r
        if red > 20: red -= 20
        else: red = 1

        green = self.g
        if green > 20: green -= 20
        else: green = 1

        blue = self.b
        if blue > 20: blue -= 20
        else: blue = 1

        HilightColor = f"{self.r} {self.g} {self.b}"
        HotTrackingColor = f"{red} {green} {blue}"

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, "Hilight", 0, winreg.REG_SZ, HilightColor)
            winreg.SetValueEx(regkey, "HotTrackingColor", 0, winreg.REG_SZ, HotTrackingColor)

        os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
    
    def reset(self):
        HilightColor = f"0 120 215"
        HotTrackingColor = f"0 102 204"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, winreg.KEY_SET_VALUE) as regkey:
            winreg.SetValueEx(regkey, "Hilight", 0, winreg.REG_SZ, HilightColor)
            winreg.SetValueEx(regkey, "HotTrackingColor", 0, winreg.REG_SZ, HotTrackingColor)
        
        os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

Highlight(0, 255, 115).change()