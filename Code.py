import pyautogui as win
from selenium import webdriver
import os, sys
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import smtplib, ssl
import requests
import json
from time import sleep
from Speak import speak2
import webbrowser
import ctypes
import base64
import hashlib
from googletrans import Translator
import googletrans

def setting():
    win.hotkey("win","i")

def file():
    win.hotkey("win","e")

def calc():
    win.hotkey("win", "r")
    win.typewrite("calc")
    win.hotkey("enter")

def task():
    win.hotkey("ctrl", "shift", "escape")

def reboot():
    win.hotkey("win", "r")
    win.typewrite("shutdown /r")
    win.hotkey("enter")

def shutdown():
    win.hotkey("win", "r")
    win.typewrite("shutdown /s")
    win.hotkey("enter")

def lock():
    ctypes.windll.user32.LockWorkStation()

def sign():
    win.hotkey("win", r)
    win.typewrite("shutdown /l")
    win.hotkey("enter")

def sleep1():
    os.popen("%windir%\\System32\\rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def defrag():
    os.popen("C:\\WINDOWS\\system32\\dfrgui")

def defragc():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\dfrgui")
    win.hotkey("enter", interval=0.2)
    win.click(button="left", x=950, y=420)

def defragd():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\dfrgui")
    win.hotkey("enter", interval=0.2)
    win.press("down")
    win.click(button="left", x=950, y=420)

def defrage():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\dfrgui")
    win.hotkey("enter", interval=0.2)
    win.press("down")
    win.press("down")
    win.click(button="left", x=950, y=420)

def control():
    os.popen("C:\\Windows\\System32\\control")

def clean():
    os.popen("C:\\WINDOWS\\system32\\cleanmgr")

def cleanc():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\cleanmgr")
    win.press("enter", interval=0.2)
    win.press("enter")

def cleand():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\cleanmgr")
    win.press("enter", interval=0.2)
    win.press("up")
    win.press("down")
    win.press("enter")

def cleane():
    win.hotkey("win", "r")
    win.typewrite("C:\\WINDOWS\\system32\\cleanmgr")
    win.press("enter", interval=0.2)
    win.press("up")
    win.press("down")
    win.press("down")
    win.press("enter")

def python():
    os.popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3\\bin\\pycharm64.exe")

def steam():
    os.popen("D:\\Steam\\Steam.exe")

def firefox():
    os.popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

def chrome():
    os.popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def web_steam():
    akun = input("Account : ")
    path = str(input("Path WebDriver: "))
    bot = webdriver.Chrome(path)
    bot.get("https://store.steampowered.com/")
    bot.maximize_window()
    login_link = bot.find_element_by_class_name("global_action_link").click()
    nick = input(bot.find_element_by_name("username"))
    pas = input(bot.find_element_by_name("password"))
    nick.clear()
    pas.clear()

    nick.send_keys(nick)
    pas.send_keys(pas)

    pas.send_keys(Keys.RETURN)

def cuaca():
    lokasi = input("Location : ").lower()
    if lokasi == "now":
        lokasi = "semarang"
    api_key = "a54de629f7cb1d48d53171b66bbcf7ef"
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={lokasi}"
    response = requests.get(url)
    x = response.json()
    if x["cod"] != "404" and "401":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        celcius = (current_temperature - 273.15) * 5 / 5
        suhu = round(celcius)
        weather_description = z[0]["description"]

        if lokasi == "semarang":
            sleep(2)
            print(f"The weather is {weather_description} here and the temperature is around {suhu} degrees Celsius")
            speak2(f"The weather is {weather_description} here and the temperature is around {suhu} degrees Celsius")
        else:
            sleep(2)
            print((f"The weather in {lokasi} is {weather_description} and the temperature is around {suhu} degrees Celsius"))
            speak2((f"The weather in {lokasi} is {weather_description} and the temperature is around {suhu} degrees Celsius"))

def wa():
    webbrowser.open("https://web.whatsapp.com/")

def spotify():
    win.hotkey("win", "r")
    win.typewrite("spotify")
    win.hotkey("enter")

def xampp():
    os.popen("C:\\xampp\\xampp-control.exe")

def encrypt_sha1():
    data = input("Input Data Do You Want to Encrypt : ")
    konvert = hashlib.sha1(data.encode())
    sleep(1)
    print(f"Encrypted Succesfully : {konvert.hexdigest()}")
    # print("FYI Encrypted Message SHA1 Called 'Hash'")

def caesar():
    data = input("Input Data Do You Want to Encrypt : ")
    data_enkripsi_caesar = ""

    key_lower = "abcdefghijklmnopqrstuvwxyz"
    key_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    offset = 4

    for i in data:
        if i in key_lower:
            l = (key_lower.index(i) + offset) % 26
            data_enkripsi_caesar += key_lower[l]

        elif i not in key_lower and i not in key_upper:
            data_enkripsi_caesar += i

        elif i in key_upper:
            l = (key_upper.index(i) + offset) % 26
            data_enkripsi_caesar += key_upper[l]

    sleep(1)
    print(f"Data Encrypted : {data_enkripsi_caesar}")

def encrypt_base64():
    data = input("Input Data Do You Want to Encrypt : ")

    data_enkripsi_base64 = base64.b64encode(data.encode())
    data_enkripsi_base64 = str(data_enkripsi_base64)
    sleep(1)
    print(f"Data Encrypted : {data_enkripsi_base64[2:-1]}")

def ascii():
    data = input("Input Data Do You Want to Encrypt : ")
    data_enkripsi = []
    for i in data:
        l = ord(i)
        data_enkripsi.append(l)

    data_kosong = ""

    for data_enkripsi_final in data_enkripsi:
        z = str(data_enkripsi_final)
        data_kosong += z + " "

    sleep(1)
    print(f"Data Encrypted : {data_kosong}")

def reverse():
    data = input("Input Data Do You Want to Encrypt : ")
    data_enkripsi_konversi_reverse = len(data) - 1
    data_enkripsi_reverse = ""

    while data_enkripsi_konversi_reverse >= 0:
        data_enkripsi_reverse += data[data_enkripsi_konversi_reverse]
        data_enkripsi_konversi_reverse -= 1

    sleep(1)
    print(f"Encrypted Succesfully : {data_enkripsi_reverse}")

def dekrip_caesar():
    data = input("Input Encrypted Data : ")
    data_dekripsi_caesar = ""

    key1 = "abcdefghijklmnopqrstuvwxyz"
    key2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    offset = 4

    for i in data:
        if i in key1:
            l = (key1.index(i) - offset) % 26
            data_dekripsi_caesar += key1[l]

        if i in key2:
            l = (key2.index(i) - offset) % 26
            data_dekripsi_caesar += key2[l]

        if i not in key1 and i not in key2:
            data_dekripsi_caesar += i

    sleep(1)
    print(f"Decrypting Succesfully : {data_dekripsi_caesar}")

def dekrip_base64():
    try:
        data = input("Input Encrpted Data : ")
        data_dekripsi_base64 = base64.b64decode(data)
        data_dekripsi_base64 = str(data_dekripsi_base64)

        sleep(1)
        print(f"Decrypting Succesfully : {data_dekripsi_base64[2:-1]}")

    except:
        print("Wrong Input !!! \nTry like this 'ZGltYXMgb2t2YQ=='")
        dekrip_base64()

def dekrip_ascii():
    try:
        data_input_dekripsi = input("Input Encrypted Data : ")
        data_input_dekripsi_split = data_input_dekripsi.split(" ")

        hasil_dekripsi = ""

        for i in data_input_dekripsi_split:
            l = int(i)
            l = chr(l)
            hasil_dekripsi += l

        sleep(1)
        print(f"Decrypting Succesfully : {hasil_dekripsi}")

    except:
        print("Wrong Input !!! \nTry like this '100 105 109 97 115 32 111 107 118 97' \nno space in start and end ")
        dekrip_ascii()

def dekrip_reverse():
    data_input_dekripsi_reverse = input("Input Encrypted Data : ")
    data_dekripsi_reverse = ""
    data_dekripsi_konversi_reverse = len(data_input_dekripsi_reverse) - 1

    while data_dekripsi_konversi_reverse >= 0:
        data_dekripsi_reverse += data_input_dekripsi_reverse[data_dekripsi_konversi_reverse]
        data_dekripsi_konversi_reverse -= 1

    sleep(1)
    print(f"Decryption Succesfuly : {data_dekripsi_reverse}")

def pes():
    os.popen("C:\\Pro Evolution Soccer 2017\\PES2017.exe")

def pes_setting():
    os.popen("C:\\Pro Evolution Soccer 2017\\Settings.exe")

def cpuz():
    os.popen("C:\\Program Files\\CPUID\\CPU-Z\\cpuz.exe")

def gns3():
    os.popen("C:\\Program Files\\GNS3\\gns3.exe")

def diskmanage():
    os.popen("C:\\Program Files\\MiniTool Partition Wizard 11\\partitionwizard.exe")

def eagle():
    os.popen("C:\\\Program Files (x86)\\EagleGet\\EagleGet.exe")

def office():
    os.popen("C:\\Users\\Dimas Okva\\AppData\Local\\Kingsoft\\WPS Office\\ksolaunch.exe")

def game():
    sleep(1)
    print("""
    1. Assansins Creed IV Black Flag 
    2. Dead Space 3
    3. Dirt 3
    4. Dota 2
    5. Counter Strike Global Offensive
    6. Grid 2
    """)
    game_file = input("Choose Game : ").lower()

    try:
        if game_file == "1" or game_file in "assasins creed iv black flag":
            os.popen("D:\\Game\\Assassin's Creed IV Black Flag Uplay Original\\Assassin's Creed IV Black Flag\\AC4BFSP.exe")
        elif game_file == "2" or game_file == "dead space 3":
            os.popen("D:\\Game\Dead Space 3 Complete Edition\\deadspace3.exe")
        elif game_file == "3" or game_file in "dirt 3" or game_file in "dirt3":
            os.popen("D:\\Game\\Dirt 3\\DiRT 3 Complete Edition\\dirt3_game.exe")
        elif game_file == "4" or game_file in "dota 2" or game_file in "dota2":
            os.popen("D:\\Steam\\steamapps\\common\\dota 2 beta\\game\\bin\\win64\\dota2.exe")
        elif game_file == "5" or game_file in "cs" or game_file in "counter strike":
            os.popen("D:\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe")
        elif game_file == "6" or game_file in "grid 2" or game_file in "grid2":
            os.popen("D:\\Steam\\steamapps\\common\\grid 2\\grid2.exe")
        else:
            print("Wrong Input !! I dont understand.....")
            game()

        sleep(1)
        print("Opening Game")

    except:
        game()

def dota():
    os.popen("D:\\Steam\\steamapps\\common\\dota 2 beta\\game\\bin\\win64\\dota2.exe")

def cs():
    os.popen("D:\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe")

def assasin():
    os.popen("D:\\Game\\Assassin's Creed IV Black Flag Uplay Original\\Assassin's Creed IV Black Flag\\AC4BFSP.exe")

def dead_space():
    os.popen("D:\\Game\Dead Space 3 Complete Edition\\deadspace3.exe")

def dirt3():
    os.popen("D:\\Game\\Dirt 3\\DiRT 3 Complete Edition\\dirt3_game.exe")

def grid2():
    os.popen("D:\\Steam\\steamapps\\common\\grid 2\\grid2.exe")

def loop(answer):
    for char in answer:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def info():
    print("\n1. ", end=" ")
    sleep(2)
    loop("Find the code yourself and understand it\n")
    sleep(1)
    print("2. ",end=" ")
    sleep(2)
    loop("Ask the maker himself, that is Mr. Dimas Okva S\n\n")
    sleep(1)

def notepad():
    os.popen("C:\\Windows\\system32\\notepad.exe")

def translate():
    try:
        text1 = input("Input Text : ")
        print("Use the country abbreviation for more https://id.wikipedia.org/wiki/ISO_3166-1")
        destinate1 = input("Translate in : ")
        tranlator = Translator()
        detect = tranlator.detect(text1)
        src_detect1 = detect.lang
        src_detect2 = googletrans.LANGUAGES[f"{src_detect1}"].title()

        if len(destinate1) > 0:
            destinate2 = googletrans.LANGUAGES[f"{destinate1}"].title()
        else:
            destinate1 = "id"
            destinate2 = googletrans.LANGUAGES[f"{destinate1}"].title()

        translated = tranlator.translate(text1, src=src_detect1, dest=destinate1)
        print(f"\nFrom {src_detect2} to {destinate2}\n{destinate2} : {translated.text}\n")

    except:
        print("Wrong Input!! Try only using 1 line when inputting data")

def maps():
    webbrowser.open("https://www.google.co.id/maps/")

def decryptor_full():
    import Decryptor
    Decryptor.decryptor()

def konversi_suhu():
    import KonversiSuhu

def konversi_celcius():
    try:
        celcius_input = float(input("Input Temperature in Celcius : "))
        celcius_fahrenheit = celcius_input * 9 / 5 + 32
        celcius_reamur = celcius_input * 4 / 5
        celcius_kelvin = celcius_input * 5 / 5 + 273.15
        print(f"""
Temperature in Fahrenheit  = {celcius_fahrenheit}
Temperature in Reamur      = {celcius_reamur}
Temperature in Kelvin      = {celcius_kelvin}
        """)
    except:
        print("Wrong Input !!")

def konversi_kelvin():
    try:
        kelvin_input = float(input("Input Temperature in Kelvin : "))
        kelvin_celcius = (kelvin_input - 273.15) * 5 / 5
        kelvin_reamur = (kelvin_input - 273.15) * 4 / 5
        kelvin_fahrenheit = (kelvin_input - 273.15) * 9 / 5 + 32
        print(f"""
Temperature in Celcius     = {kelvin_celcius} 
Temperature in Reamur      = {kelvin_reamur}
Temperature in Fahrenheit  = {kelvin_fahrenheit}
            """)
    except:
        print("Wrong Input !!")

def konversi_fahrenheit():
    try:
        fahrenheit_input = float(input("Input Temperature in Fahrenheit : "))
        fahrenheit_celcius = (fahrenheit_input - 32) * 5 / 9
        fahrenheit_reamur = (fahrenheit_input - 32) * 4 / 9
        fahrenheit_kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15
        print(f"""
Temperature in Celcius     = {fahrenheit_celcius}
Temperature in Reamur      = {fahrenheit_reamur}
Temperature in Kelvin      = {fahrenheit_kelvin}
            """)
    except:
        print("Wrong Input !!")

def konversi_reamur():
    try:
        reamur_input = float(input("Input Temperature in Reamur : "))
        reamur_fahrenheit = reamur_input * 9 / 4 + 32
        reamur_celcius = reamur_input * 5 / 4
        reamur_kelvin = reamur_input * 5 / 5 + 273.15
        print(f"""
Temperature in Fahrenheit  = {reamur_fahrenheit}
Temperature in Celcius     = {reamur_celcius}
Temperature in Kelvin      =  {reamur_kelvin}
        """)
    except:
        print("Wrong Input !!")

def win_update():
    win.hotkey("win", "r")
    win.typewrite("ms-settings:windowsupdate")
    win.hotkey("enter")

def portscan():
    import Port_Scanner
    Port_Scanner.port()

def networkScan():
    import Network_Scanner
    Network_Scanner.netscan()

def tracker():
    import IP_Tracker
    IP_Tracker.track()
