import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.hotkey ('win')    # Tecla de atalho
pyautogui.write ('Brave')
pyautogui.press ('enter')

# Acessar Whatsapp Web
link = 'https://web.whatsapp.com/'
pyperclip.copy(link)
pyautogui.hotkey ('ctrl', 'v')
pyautogui.press ('enter')


# Buscar um contato

time.sleep(15)  # Tempo de espera para carregamento (evita que o código continue rodando antes do tempo necessario para o carregamento da página)

pyautogui.click(110, 272)   # Eixo X e Y varia de acordo com o tamanho da tela (desvantagem de se usar o Pyautogui)
pyautogui.write ('Contato Teste')

# Clicar no contato
time.sleep(2)
pyautogui.click(175, 396)

# Clicar no campo de texto
pyautogui.click(817, 1017)

# Digitar a mensagem

msg = 'Teste de automação com Python'
pyperclip.copy(msg)
pyautogui.hotkey ('ctrl', 'v')
pyautogui.press ('enter')

# Enviar mensagem
pyautogui.press ('enter')
