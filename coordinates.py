from pynput.mouse import Controller
import time

mouse = Controller()
mouse.move(100,1000)

print("Move your mouse. Press Ctrl+C to stop.")
try:
    while True:
        x, y = mouse.position  # Gets the mouse position
        print(f"Mouse Position: ({x}, {y})", end="\r")
except KeyboardInterrupt:
    print("\nStopped.")
