import pyautogui
from PIL import Image

def FindColor(r,g,b):
    image = Image.open('screenshot.png')
    for x in range(1, 2080):
        for y in range(1, 1330):
            try:
                px = image.getpixel((x, y))
                if px[0] == r and px[1] == g and px[2] == b:
                    print x, y
                    pyautogui.moveTo(x, y, duration=1.00)
            except KeyboardInterrupt:
                pass

FindColor(0,0,0)