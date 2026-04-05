# Importes de bibliotecas
import pyautogui  # importa biblioteca do Pyautogui 
import time  # Importa biblioteca do Time

# Pyautogui segurança
pyautogui.PAUSE = 3  # Vai ter um cooldown de 3 segundos até a próxima exceução
pyautogui.FAILSAFE = True  # Quando o mouse estiver no canto esquerdo superior toda ação é cancelada

# Pyautogui Mouse
time.sleep(3)  # Vai ter uma contagem regressiva de 3 segundos para executar todas ações em diante
print(pyautogui.size())  # Combinando com print() ele mostra a resolução do seu monitor, no console
print(pyautogui.position())  # Mostra a posição do seu cursor, no console
print(pyautogui.onScreen())  # Mostra se a posição do seu cursor está dentro da área do seu monitor, no console
pyautogui.click(X, Y)  # Vai clicar em uma posição X e Y (exemplo: 140, 360)
pyautogui.moveTo(X, Y)  # Move seu cursor para uma posição X e Y
pyautogui.moveRel(X, Y)  # Segura e arrasta qualquer coisa para uma posição X e Y
pyautogui.dragTo(X, Y)  # Vai mover seu cursor para uma posição X e Y enquanto mantêm o esquerdo pressionado
pyautogui.dragRel(X, Y)  # Arrasta o cursor pressionando o esquerdo, bom para desenhar
pyautogui.rightClick(X, Y)  # Vai clicar com o direito em certa posição X e Y
pyautogui.middleClick(X, Y)  # Vai clicar com o M3 (Scroll) em certa posição X e Y
pyautogui.doubleClick(X, Y)  # Vai clicar duas vezes em certa poisição X e Y
pyautogui.tripleClick(X, Y)  # vai clicar três vezes em certa posição X e Y
pyautogui.scroll(100 ou -100)  # Vai usar o scroll do mouse em certa quantidade, +/-
pyautogui.mouseDown(X, Y)  # Fica pressionado um botão do mouse permanente
pyautogui.mouseUp(X, Y)  # Solta o botão do mouse pressionado permanente

# Pyautogui Teclado
pyautogui.write("Texto")  # É possível escrever qualquer texto
pyautogui.press("enter")  # Pressiona uma tecla do teclado
pyautogui.hotkey("ctrl", "s")  # Pressiona várias teclas do teclado ao mesmo tempo

# Pyautogui Box Function
pyautogui.alert("Texto")  # Cria uma caixa de dialogo com o texto
pyautogui.confirm("Texto")  # Cria uma caixa de confirmação com o texto
pyautogui.prompt("Texto")  # Cria um prompt de texto com resposta

# Pyautogui Screenshot Functions
pyautogui.screenshot("imagem.png")  # Consegue clicar, seguir, mover etc... na onde estiver a imagem de referencia
# Também usada para printar e salvar imagens diretamente da pasta dos programas
______________________________________________________________________________________________________________________________________________________