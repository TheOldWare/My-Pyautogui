import pyautogui
import time

pyautogui.PAUSE = 0.3

# pegar posição do mouse e o tamanho da tela
print(pyautogui.position())
print(pyautogui.size())

# funções do mouse
time.sleep(3)
# pyautogui.click(x, y) #clicar em uma posição especifica da minha tela
# pyautogui.moveTo(419, 129, duration=2) # move o mouse para uma posição especifica da minha tela
# pyautogui.click(380, 294)
# pyautogui.scroll(-500)

# funções do teclado
pyautogui.write("Nigga", interval=1)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "s")