import pyautogui
mesaj=pyautogui.prompt(text="Text",title="DIORspammer")
while True:
    pyautogui.typewrite(mesaj)
    pyautogui.press('enter')
