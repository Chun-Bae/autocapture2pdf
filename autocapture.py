import pyautogui
import keyboard
import time

num_captures = 953
current_captures = 0

def capture_and_save(x, y, width, height):
    global current_captures
    if current_captures < num_captures:
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f'./img/image_{current_captures}.png')
        print(f'Captured image_{current_captures}.png')

        pyautogui.press('right')
        time.sleep(0.0001) 
        current_captures += 1
    if current_captures >= num_captures:
        print("Completed all captures.")
        keyboard.unhook_all()

def start_capture():
    global current_captures
    current_captures = 0
    print("Starting captures...")
    while current_captures < num_captures:
        capture_and_save(141, 441, 795, 998)  
        time.sleep(0.0001)  


keyboard.add_hotkey('s', start_capture)

print("Press 's' to start capture, ESC to stop.")
keyboard.wait('esc')