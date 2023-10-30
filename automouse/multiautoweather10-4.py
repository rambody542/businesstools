import pyautogui
import time
import pyperclip

weather = ["서울 날씨","시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨" ]

addr_x = 1104
addr_y = 63
start_x = 985
start_y = 232
end_x = 1654
end_y = 653

for localweather in weather:
  pyautogui.moveTo(addr_x, addr_y, 1)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.write("www.naver.com", interval=0.1)
  pyautogui.write(["enter"])
  time.sleep(1)
  
  pyperclip.copy(localweather)
  pyautogui.hotkey("ctrl", "v")
  time.sleep(0.5)
  pyautogui.write(["enter"])
  time.sleep(1)
  save_path = 'automouse\\'+ localweather + '.png'
  pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))