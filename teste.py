import pyautogui
import time
pyautogui.PAUSE = 0.3

time.sleep(4)
pyautogui.moveTo(514, 16, duration=3)
pyautogui.click(514, 16)
pyautogui.moveTo(468, 63, duration=1)
pyautogui.click(468, 63)

pyautogui.write("https://www.youtube.com/@warewsk", interval=0.1)
pyautogui.press("enter")