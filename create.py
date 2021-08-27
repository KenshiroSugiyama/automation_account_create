# coding: UTF-8

# PyAutoGUIをインポート
import pyautogui 
import time
import webbrowser

# x = pyautogui.position()
# print(x)

#postman 
# pyautogui.click(x=1277, y=1054)

#IE
# pyautogui.click(x=993, y=1054)

#personal_info_sheet
# pyautogui.click(x=243, y=22)

#API結果シート
# pyautogui.click(x=590, y=23)

#postman起動
pyautogui.click(x=258, y=1058,duration=1)
time.sleep(3)
pyautogui.typewrite(['p', 'o', 's', 't', 'm', 'a', 'n'])
time.sleep(3)
pyautogui.hotkey('enter')
time.sleep(40)
pyautogui.click(x=1225, y=805)
time.sleep(2)
pyautogui.click(x=963, y=408)
time.sleep(2)

for i in range(20):
    #personal_information起動
    webbrowser.open("https://docs.google.com/spreadsheets/d/1xLALVzxv9QzsQ7FOLtoEKGb-rYTRXzP-3w7_YS2FXfg/edit?ts=5ed48b49&pli=1#gid=1347913400")
    time.sleep(10)
    #テスト結果起動
    webbrowser.open("https://docs.google.com/spreadsheets/d/1EKNtThtt4YQXwO5r_T5gsrG8i0Z5K8M-UC5SkjUiIds/edit#gid=395302572")
    time.sleep(10)


    #個人情報取得
    pyautogui.click(x=243, y=22)
    time.sleep(2)
    for i in range(4):
        pyautogui.hotkey('right')
        time.sleep(0.5)
    pyautogui.hotkey('down')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'shift','down')
    time.sleep(0.5)
    for i in range(2):
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
    pyautogui.hotkey('down')


    # APIテスト結果シートに記入
    pyautogui.click(x=590, y=23)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(3)
    for i in range(6):
        pyautogui.hotkey('right')
        time.sleep(0.5)
    pyautogui.hotkey('ctrl','down')
    time.sleep(0.5)
    pyautogui.hotkey('down')
    time.sleep(0.5)
    x = pyautogui.locateOnScreen('suusiki.png' , confidence=0.7)
    pyautogui.click(x)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    # pyautogui.hotkey('ctrl', 'w')
    # time.sleep(3)
    # y = pyautogui.locateOnScreen('idou.png' , confidence=0.6)
    # time.sleep(0.5)
    # pyautogui.doubleClick(y)
    # time.sleep(3)
    # print("送る内容貼り付け")


    #postman起動
    time.sleep(2)
    pyautogui.click(x=1275, y=1050)
    time.sleep(1)
    pyautogui.doubleClick(x=675, y=656)
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.6)
    pyautogui.hotkey('del')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.click(x=1662, y=333)
    time.sleep(15)

    #request_id取得
    x = pyautogui.locateOnScreen('request.png' , confidence=0.7)
    pyautogui.tripleClick(x)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.6)
    # pyautogui.click(x=1874, y=15)
    # time.sleep(3)


    #メモ帳起動、request_id修正
    time.sleep(0.6)
    pyautogui.click(x=258, y=1058,duration=1)
    time.sleep(3)
    pyautogui.typewrite(['m', 'e', 'm', 'o'])
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.6)
    pyautogui.press('up')
    time.sleep(0.6)
    for i in range(19):
        pyautogui.press('del')
        time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.6)
    pyautogui.hotkey('right')
    time.sleep(2)
    for i in range(2):
        pyautogui.hotkey('left')
        time.sleep(0.6)
    pyautogui.hotkey('del')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.6)
    pyautogui.hotkey('n')

    #request_id貼り付け
    time.sleep(1)
    pyautogui.click(x=993, y=1054)
    time.sleep(1)
    pyautogui.click(x=590, y=23)
    time.sleep(1)
    pyautogui.click(x=590, y=23)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(3)
    pyautogui.hotkey('down')
    time.sleep(0.6)
    pyautogui.hotkey('right')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl','down')
    time.sleep(0.6)
    pyautogui.hotkey('down')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'v')
    # time.sleep(0.6)
    # pyautogui.hotkey('ctrl', 'w')
    # time.sleep(3)
    # y = pyautogui.locateOnScreen('idou.png' , confidence=0.6)
    # time.sleep(0.5)
    # pyautogui.doubleClick(y)
    time.sleep(3)
    print("request_id貼り付け完了")

    #メアド貼り付け
    pyautogui.click(x=243, y=22)
    time.sleep(3)
    # pyautogui.press('down')
    time.sleep(0.5)
    for i in range(2):
        pyautogui.hotkey('down')
        time.sleep(0.5)
    for i in range(4):
        pyautogui.hotkey('left')
        time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'w')
    pyautogui.click(x=590, y=23)
    time.sleep(1)
    for i in range(9):
        pyautogui.press('right')
        time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'w')
    # time.sleep(3)
    # k = pyautogui.locateOnScreen('idou.png' , confidence=0.6)
    # time.sleep(0.5)
    # pyautogui.doubleClick(y)
    # time.sleep(6)

    #送信後スプレッドシートに記入
    # webbrowser.open("https://docs.google.com/spreadsheets/d/1xLALVzxv9QzsQ7FOLtoEKGb-rYTRXzP-3w7_YS2FXfg/edit?ts=5ed48b49&pli=1#gid=1536068967")
    # time.sleep(10)
    pyautogui.click(x=243, y=22)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('pageup')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(3)
    for i in range(11):
        pyautogui.hotkey('right')
        time.sleep(0.5)
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('down')
    pyautogui.typewrite('Used')
    pyautogui.hotkey('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(10)
    print("--終了--")



