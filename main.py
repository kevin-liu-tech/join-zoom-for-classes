import subprocess
import pyautogui
import time
import pandas as pd 
from datetime import datetime

def sign_in(meetingid, pswd):
    print("Opening Zoom")
    subprocess.Popen('C:\\Users\\gerni\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

    time.sleep(1)

    print("Joining A Meeting Now")
    join_btn = pyautogui.locateCenterOnScreen(r'C:\Users\gerni\Documents\Programming Projects\Life Hacks\Programming a Zoom Bot\join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(1)

    print("Clicking Meeting ID")
    meeting_id_btn =  pyautogui.locateCenterOnScreen(r'C:\Users\gerni\Documents\Programming Projects\Life Hacks\Programming a Zoom Bot\meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click(duration=5)
    pyautogui.write(meetingid)


    time.sleep(1)

    print("Join Meeting")
    join_btn = pyautogui.locateCenterOnScreen(r'C:\Users\gerni\Documents\Programming Projects\Life Hacks\Programming a Zoom Bot\join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(5)

    print("Clicking Meeeting Passcode")
    meeting_pswd_btn = pyautogui.locateCenterOnScreen(r'C:\Users\gerni\Documents\Programming Projects\Life Hacks\Programming a Zoom Bot\meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.moveTo(meeting_pswd_btn, duration=5)
    pyautogui.write(pswd)
    pyautogui.press('enter')

# Reading the file
df = pd.read_csv('C:\\Users\gerni\Desktop\zoomtimings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')
