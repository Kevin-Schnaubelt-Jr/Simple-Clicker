# Might have to pip install pyautogui
import pyautogui
# Might have to pip install keyboard, too
import keyboard
import time
import threading

'''
set click_rate to change clicks per second (CpS)
30 CpS = 0.0333
60 CpS = 0.0166
100 CpS = 0.01
Alteratively, set it to 1 divided by your desired CpS
Example: 1/200 for 200 CpS
'''

class AutoClicker:
    def __init__(self, click_rate=0.01):
        self.click_rate = click_rate
        self.clicking = False
        self.click_thread = threading.Thread(target=self.start_clicking)

    def start_clicking(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(self.click_rate)

    def stop_clicking(self):
        self.clicking = False

    def toggle_clicking(self, e):
        if self.clicking:
            self.stop_clicking()
            if self.click_thread.is_alive():
                self.click_thread.join()  # Wait for the thread to finish
        else:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.start_clicking)
            self.click_thread.start()  # Start clicking in a separate thread

if __name__ == "__main__":
    autoclicker = AutoClicker()
    keyboard.on_press_key('F12', autoclicker.toggle_clicking, suppress=True)
    keyboard.wait()
