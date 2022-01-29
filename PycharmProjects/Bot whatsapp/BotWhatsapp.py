import pyautogui as py, time, webbrowser as web
web.open('https://web.whatsapp.com/send?phone=+573167850101')
time.sleep(5)
Doc=open('Whatsapp.txt','r')
print(str(Doc))
for i in Doc:
    py.write(str(i))
    py.press('enter')


