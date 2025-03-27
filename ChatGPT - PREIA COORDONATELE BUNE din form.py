from pynput import mouse
import ctypes

# Structură POINT nativă Windows
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_cursor_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

positions = []
scroll_events = []

def on_click(x, y, button, pressed):
    if pressed:
        pos = get_cursor_position()
        if button.name == 'left':
            print(f"[CLICK] ({pos[0]}, {pos[1]})")
            positions.append(('click', pos))
        elif button.name == 'right':
            print("\n=== Înregistrare finalizată ===\n")
            for i, entry in enumerate(positions + scroll_events, 1):
                action, data = entry
                if action == 'click':
                    print(f"{i}. CLICK la coordonata: {data}")
                elif action == 'scroll':
                    print(f"{i}. SCROLL {'în sus' if data > 0 else 'în jos'}: {abs(data)} trepte")
            return False

def on_scroll(x, y, dx, dy):
    if dy != 0:
        scroll_events.append(('scroll', dy))
        print(f"[SCROLL] {'↑' if dy > 0 else '↓'} cu {abs(dy)} trepte")

def main():
    print("🖱 CLICK stânga = înregistrează poziția")
    print("🖱 CLICK dreapta = oprește programul și afișează tot")
    print("🌀 Scroll-ul mouse-ului este înregistrat automat\n")

    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

if __name__ == "__main__":
    main()
