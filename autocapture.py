import pyautogui
import keyboard
import time

num_captures = 119
current_captures = 0

def capture_and_save(x, y, width, height):
    global current_captures
    if current_captures < num_captures:
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        formatted_number = str(current_captures).zfill(4)
        screenshot.save(f'./img/image_{formatted_number}.png')
        print(f'Captured image_{formatted_number}.png')

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
        capture_and_save(257, 74, 1401, 951)  
        time.sleep(0.0001)  


keyboard.add_hotkey('s', start_capture)

print("Press 's' to start capture, ESC to stop.")
keyboard.wait('esc')