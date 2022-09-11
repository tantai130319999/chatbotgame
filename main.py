from ppadb.client import Client as AdbClient

import os

import pyscreeze

import threading

import time

with open('data/message.txt', encoding = 'utf-8') as file:
    listdata = file.read()
_message = listdata.splitlines()
with open('data/NumEmu.txt', encoding = 'utf-8') as file:
    listdata = file.read()
NumEmu = listdata.splitlines()
with open('data/NumRE.txt', encoding = 'utf-8') as file:
    listdata = file.read()
NumRE = listdata.splitlines()
# main auto
def main(thutu,message):
    os.system('adb devices')
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    device = client.device(devices[thutu].serial)
    device.on_keyboar()
    while True:
        device.input_tap(250,260)
        time.sleep(1)
        for a in range(10):
            device.input_tap(120,165)
        for a in range(int(NumRE[0])):
            device.input_tap(320,165)
        device.input_tap(220,230)
        vaogame = 0
        while vaogame == 0:
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result)
            kiemtra = pyscreeze.locate(r'data/vaoban.png',r'data/screen' + str(thutu) + '.png', confidence=.65)
            if kiemtra != None:
                vaogame = 1
            kiemtra = pyscreeze.locate(r'data/delay.png',r'data/screen' + str(thutu) + '.png', confidence=.65)
            if kiemtra != None:
                device.input_tap(220,200)   
                time.sleep(1)
                device.input_tap(250,260)
                time.sleep(1)
                for a in range(10):
                    device.input_tap(120,165)
                for a in range(int(NumRE[0])):
                    device.input_tap(320,165)
                device.input_tap(220,230)
        result = device.screencap()
        with open("data/screen" + str(thutu) + ".png", "wb") as fp:
            fp.write(result)
        kiemtra = pyscreeze.locate(r'data/dangxem.png',r'data/screen' + str(thutu) + '.png', confidence=.65)    
        if kiemtra != None:
            # dangxem = 0
            # while dangxem == 0:
                for m in message:
                    device.input_tap(33,258)
                    time.sleep(0.25)
                    device.input_tap(140,172)
                    time.sleep(0.25)
                    device.input_text2(m)
                    device.input_tap(323,99)
                    time.sleep(0.5)
                    result = device.screencap()
                    with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                        fp.write(result)
                    kiemtra = pyscreeze.locate(r'data/dangxem.png',r'data/screen' + str(thutu) + '.png', confidence=.65)   
                    if kiemtra == None: 
                       break
                device.input_keyevent(4)
                timban = 0
                while timban == 0:
                    result = device.screencap()
                    with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                        fp.write(result)
                    kiemtra = pyscreeze.locate(r'data/timban.png',r'data/screen' + str(thutu) + '.png', confidence=.65)   
                    if kiemtra != None: 
                        timban = 1
        else:
            device.input_keyevent(4)
            timban = 0
            chat = 0
            times = 0
            while timban == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtra = pyscreeze.locate(r'data/timban.png',r'data/screen' + str(thutu) + '.png', confidence=.65)   
                if kiemtra != None: 
                    timban = 1
                times += 1
                if chat == 0 and timban == 0 and times == 10:
                    for m in message:
                        device.input_tap(33,258)
                        time.sleep(0.25)
                        device.input_tap(140,172)
                        time.sleep(0.25)
                        device.input_text2(m)
                        device.input_tap(323,99)
                        time.sleep(0.5)
                    chat = 1
# end main auto
# os.chdir(path[0])
# os.system('NoxConsole.exe adb -index:0 -command:devices')
# al = os.popen('NoxConsole.exe adb -index:0 -command:devices').read()
# listdevi = []
# for a in range(1,len(al.splitlines())):
#     if al.splitlines()[a] != '':
#         devi = al.splitlines()[a][:al.splitlines()[a].find('\t')]
#         listdevi.append(devi)
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# for a in range(int(NumEmu[0])):
#     os.system('adb connect ' + listdevi[a])
for a in range(int(NumEmu[0])):
    thread = []
    t = threading.Thread(target=main, args=(a,_message))
    thread.append(t)
for i in thread:
    i.start()
