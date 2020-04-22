import speech_recognition as sr
from Speak import speak2
from time import sleep
import sys
from Code import *
from random import choice

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     # print("Listening....")
#     audio = r.listen(source)
#
# try:
#     said = r.recognize_google(audio)
#     said = said.lower()
#     print(f"Command : {said}")
#
# except:
#     print("I Don't Understand, Sorry :)")
#     # takeCommand()

def intro():
    global name
    global master
    # speak2("Let me introduce myself, My name is haico, I'm a software assistant, like the basic purpose of the machine, I'm here to help with your work, tell me what is your name ?")
    # master = input("Name : ")
    # sleep(2)
    # speak2(f"Nice to meet you, {master}")
    # speak2("would you like to give me a nickname for the next time ?")
    # name = input("Nick Name : ")
    # sleep(2)
    # respon = [f"{name} ??..., yeahh, thats a good idea", f"{name} ??....., i think its sounds great", f"{name} ??...,sure, its sounds great"]
    # speak2(choice(respon))

    name = "Haico"
    master = "Dimas"

def action():
    command = input(f"{master} : ").lower()

    def loop(answer):
        for char in answer:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

    agree = ["Okay", "Sure", "Sure Thing", "Of Course", "As You Wish", "Okey", "Yes Sir", "Yes Mam", "Opening"]
    keluar = ["exit", "quit", "break"]

    # global said
    if command in "hello" or "hello" in command or command in "heyy" or "hey" in command or len(command) == 0 :
        print(f"{name} : ", end="")
        sleep(2)
        answer = "Hello.. How can i help you ? \n"
        loop(answer)
        sleep(1)
        action()

    elif command in "describe yourself" or command in "describe yourself":
        print("Let me introduce myself, My name is haico, I'm a software assistant, like the basic purpose of the machine, I'm here to help with your work")
        speak2("Let me introduce myself, My name is haico, I'm a software assistant, like the basic purpose of the machine, I'm here to help with your work")
        action()
        # speak5("I'm Sarah, a software program to help you, nice to meet you, what's your name?")

    elif "live without the internet" in command:
        print(f"{name} : ", end="")
        sleep(2)
        answer = "These days, the internet is very essential. What would life be like without it?\n"
        loop(answer)
        sleep(1)
        action()
        # command = input(f"\n{master} : ")

    elif command in "setting":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        setting()
        sleep(1)
        action()

    elif command in "file":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        file()
        sleep(1)
        action()

    elif command in "task manager" or command in "task":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        task()
        sleep(1)
        action()

    elif command in "reboot" or command in "restart":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        reboot()
        action()

    elif command in "shutdown" or command in "shut up":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        shutdown()
        action()

    elif command in "lock":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        lock()
        action()

    elif command in "sign" or command in "signout" or command in "sign out":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        sign()
        action()

    elif command in "sleep":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        sleep1()
        action()

    elif command in "defrag":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        defrag()
        sleep(1)
        action()

    elif command in "defrag c":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        defragc()
        sleep(1)
        action()

    elif command in "defrag d":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        defragd()
        sleep(1)
        action()

    elif command in "defrag e":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        defrage()
        sleep(1)
        action()

    elif command in "control" or command in "control panel" or command in "control panel":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        control()
        sleep(1)
        action()

    elif command in "clean" or command in "clean up" or command in "cleanup":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        clean()
        sleep(1)
        action()

    elif command in "clean c"or command in "clean up c" or command in "cleanup c":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        cleanc()
        action()

    elif command in "clean d" or command in "clean up d" or command in "cleanup d":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        cleand()
        action()

    elif command in "clean e" or command in "clean up e" or command in "cleanup e":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        cleane()
        action()

    elif command in "python" or command in "pycharm" or  command in "jet":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        python()
        sleep(1)
        action()

    elif command in "steam":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        steam()
        action()

    elif command in "firefox" or command in "mozilla" or command in "mozila":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        firefox()
        sleep(1)
        action()

    elif command in "chrome":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        chrome()
        sleep(1)
        action()

    elif command in "web steam":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        web_steam()
        sleep(1)
        action()

    elif command in "mail" or command in "email":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        mail()
        action()

    elif command in "weather":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        cuaca()
        sleep(1)
        action()

    elif command in "calc":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        calc()
        action()

    elif command in "wa":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        wa()
        sleep(1)
        action()

    elif command in "spotify":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        spotify()
        action()

    elif command in "xampp":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        xampp()
        sleep(1)
        action()

    elif command in "encrypt sha1" or command in "encrypt sha 1" or command in "enc sha1" or command in "enc sha 1":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        encrypt_sha1()
        action()

    elif command in "encrypt caesar" or command in "enc caesar":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        caesar()
        action()

    elif command in "encrypt base64" or command in "encrypt base 64" or command in "enc base64" or command in "enc base 64":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        encrypt_base64()
        action()

    elif command in "encrypt ascii" or command in "enc ascii":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        ascii()
        action()

    elif command in "encrypt reverse" or command in "enc reverse":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        reverse()
        action()

    elif command in "decrypt caesar" or command in "dec caesar":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        dekrip_caesar()
        action()

    elif command in "decrypt base64" or command in "decrypt base 64" or command in "dec base64" or command in "dec base 64":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        dekrip_base64()
        action()

    elif command in "decrypt ascii" or command in "dec ascii":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        dekrip_ascii()
        action()

    elif command in "decrypt reverse" or command in "dec reverse":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        dekrip_reverse()
        action()

    elif command in "pes":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        pes()
        sleep(1)
        action()

    elif command in "pes setting":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        pes_setting()
        sleep(1)
        action()

    elif command in "cpuz" or command in "cpu z":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        cpuz()
        sleep(1)
        action()

    elif command in "gns 3" or command in "gns3":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        gns3()
        sleep(1)
        action()

    elif command in "disk manage":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        diskmanage()
        sleep(1)
        action()

    elif command in "eagle get" or command in "eagleget":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        eagle()
        sleep(1)
        action()

    elif command in "office" or command in "word" or command in "excel" or command in "power point":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        office()
        sleep(1)
        action()

    elif command in "game":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        print("Here i found... ")
        game()
        action()

    elif command in "dota2" or command in "dota 2":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        dota()
        sleep(1)
        action()

    elif command in "cs" or command in "csgo":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        cs()
        sleep(1)
        action()

    elif command in "dirt3" or command in "dirt 3":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        dirt3()
        sleep(1)
        action()

    elif command in "grid2" or command in "grid 2":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        grid2()
        sleep(1)
        action()

    elif command in "assasins" or command in "black flag":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        assasin()
        sleep(1)
        action()

    elif command in "dead space3" or command in "dead space 3":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        dead_space()
        sleep(1)
        action()

    elif command in "information" or command == "?" or command == "help":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        info()
        action()

    elif command in "notepad":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        notepad()
        sleep(1)
        action()

    elif command in "translate":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        translate()
        sleep(1)
        action()

    elif command in "maps" or command in "google maps":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        maps()
        sleep(1)
        action()

    elif command in "decryptor":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        decryptor_full()
        action()

    elif command in "konversi suhu":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        konversi_suhu()
        action()

    elif command in "konversi celcius" or command in "celcius":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        konversi_celcius()
        action()

    elif command in "konversi reamur" or command in "reamur":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        konversi_reamur()
        action()

    elif command in "konversi kelvin" or command in "kelvin":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        konversi_kelvin()
        action()

    elif command in "konversi fahrenheit" or command in "fahrenheit":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        konversi_fahrenheit()
        action()

    elif command in "update" or command in "windows update":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        win_update()
        action()

    elif command in "portscan" or command in "port scan":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        portscan()
        action()

    elif command in "netscan" or command in "network scan":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        networkScan()
        action()

    elif command in "track" or command in "tracker":
        print(f"{name} : ", end="")
        sleep(1)
        print(choice(agree))
        sleep(1)
        tracker()
        action()

    elif command in keluar:
        sleep(1)
        answer = f"Thank You Very Much Mr. {master}, Bye bye :)"
        loop(answer)

    else:
        sleep(2)
        answer = "For now I still can't answer that, sorry :)\n"
        loop(answer)
        sleep(1)
        action()