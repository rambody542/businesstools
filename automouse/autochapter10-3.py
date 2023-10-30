import pyautogui
import time
import pyperclip

pyautogui.moveTo(1238, 151, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 985
start_y = 232
end_x = 1654
end_y = 653

pyautogui.screenshot(r'automouse\서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
