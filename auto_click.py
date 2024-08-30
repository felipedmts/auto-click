import pyautogui
import keyboard
import threading
import time

# Variável global para controlar o estado do auto clique
auto_click = False

# Função que realiza o auto clique
def click_mouse():
    while True:
        if auto_click:
            pyautogui.mouseDown()  # Pressiona o botão do mouse
            pyautogui.mouseUp()    # Solta o botão do mouse
            time.sleep(0.001)      # Intervalo mínimo entre cliques
        else:
            time.sleep(0.1)        # Intervalo maior quando o auto clique está desativado

# Função que alterna o estado do auto clique
def toggle_auto_click():
    global auto_click
    auto_click = not auto_click
    if auto_click:
        print("✅ Auto clique ativado.")
    else:
        print("❌ Auto clique desativado.")

# Inicia a thread do auto clique
click_thread = threading.Thread(target=click_mouse)
click_thread.daemon = True
click_thread.start()

# Define a tecla que ativa/desativa o auto clique (exemplo: 'F1')
keyboard.add_hotkey('F1', toggle_auto_click)

# Mantém o programa em execução
print("Pressione 'F1' para ativar/desativar o auto clique. Pressione 'esc' para sair.")
keyboard.wait('esc')
