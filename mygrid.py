from pynput.mouse import Listener

start_pos = None
end_pos = None

def on_click(x, y, button, pressed):
    global start_pos, end_pos
    if pressed:
        start_pos = (x, y)
    else:
        end_pos = (x, y)

        return False

print("start drag.")
with Listener(on_click=on_click) as listener:
    listener.join()

x_start, y_start = start_pos
x_end, y_end = end_pos
width = x_end - x_start
height = y_end - y_start

print(str(x_start)+", "+ str(y_start)+", "+ str(width)+", "+ str(height))
print("finish.")