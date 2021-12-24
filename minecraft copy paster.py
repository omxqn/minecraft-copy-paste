
# importing the library
import pyperclip as pc
import keyboard
import time
cmd = []
def import_text():
    global cmd
    commands = open("ranks.yml",'r')
    cmd = commands.readlines()
    commands.close()
import_text()
while True:
    if keyboard.is_pressed("a"):
        while True:
            for i in cmd:
      
                keyboard.send("t")
                print("T pressed")
                time.sleep(0.5)
                keyboard.write(i)
                print("CMD pressed")
                time.sleep(0.5)
                keyboard.press("enter")
                print("ENTER pressed")
                time.sleep(0.5)
                if keyboard.is_pressed("q"):
                    break

            break

            