import pyautogui
import time
pyautogui.PAUSE = 0.3

time.sleep(3)
pyautogui.moveTo(23, 881, duration=2)
pyautogui.click(23, 881)
pyautogui.write("bloco de notas", interval=0.2)
pyautogui.press("enter")

pyautogui.write("Kenedy é viado e neguinho malandro", interval=0.2)
pyautogui.press("enter")
pyautogui.write("Max é comedor de viados", interval=0.2)
pyautogui.hotkey("ctrl", "s")

pyautogui.moveTo(309, 332, duration=1)
pyautogui.click(309, 332)
pyautogui.moveTo(367, 537, duration=1)
pyautogui.click(367, 537, button="left", clicks=2, interval=1)
pyautogui.press("backspace")
pyautogui.write("nego ney", interval=0.2)
pyautogui.moveTo(845, 614, duration=1)
pyautogui.click(845, 614)
pyautogui.moveTo(1383, 126, duration=1)
pyautogui.click(1383, 126)

pyautogui.moveTo(682, 887, duration=1)
pyautogui.click(682, 887)
pyautogui.moveTo(276, 274, duration=1)
pyautogui.click(276, 274)
pyautogui.moveTo(599, 266, duration=1)
pyautogui.click(599, 266, button="left", clicks=2, interval=0.1)