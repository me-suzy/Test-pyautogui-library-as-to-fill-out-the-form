import ctypes
from pynput import mouse

# Structură Windows pentru coordonate precise
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_mouse_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

click_steps = []
step_number = 1

def on_click(x, y, button, pressed):
    global step_number
    if pressed:
        pos = get_mouse_position()
        if button.name == 'left':
            click_steps.append(pos)
            print(f"PAS {step_number}: CLICK la ({pos[0]}, {pos[1]})")
            step_number += 1
        elif button.name == 'right':
            print("\n=== Înregistrare completă ===\n")
            for idx, (x, y) in enumerate(click_steps, 1):
                print(f"PAS {idx}: CLICK la coordonata: ({x}, {y})")
            return False

def main():
    print("🖱 CLICK stânga = salvează coordonata ca PAS")
    print("🖱 CLICK dreapta = încheie și afișează toți pașii\n")
    print("Navighează manual la formularul dorit și începe să faci click-uri...")

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()