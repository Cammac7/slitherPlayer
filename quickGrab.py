import pyscreenshot
# part of the screen
screenshot=pyscreenshot.grab(bbox=(0,100,1040,665))
screenshot.save('screenshot.png')