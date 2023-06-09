import websocket
import json
import threading
import sys
import time
import sched
import datetime
import os
import json
from pathlib import Path
import platform
from .consumers import save_record


connected = True
name = ''


def send_msg(mssg, dest):
    global wsapp
    msg = {'message': mssg,
           'username': name,
           'destination': dest}
    jmsg = json.dumps(msg)
    wsapp.send(jmsg)
    # print(f"Sent: {msg}")


def on_open(wsapp):
    print(f"Connected as: {name} @ {time.ctime()}")
    inputThead = threading.Thread(target=useInput, args=())
    inputThead.setDaemon(True)
    inputThead.start()


def on_close(wsapp, close_status_code, close_msg):
    global connected
    print('disconnected from server')
    if connected:
        print("Retry : %s" % time.ctime())
        time.sleep(10)
        __create_ws()  # retry per 10 seconds


def on_error(wsapp, error):
    print(error)


def on_message(wsapp, message):
    msg = json.loads(message)
    if msg['destination'] == name or msg['destination'] == "all":
        print(f"Rec: {message}")
        print("enter DEST (q to close): ")
        if 'mlevels' in msg['message']:
            save_record(msg['message'])


def __create_ws():
    global wsapp
    global connected
    while connected:
        try:
            websocket.enableTrace(False)
            wsapp = websocket.WebSocketApp("ws://synapse.viewdns.net:8000/ws/term/?",
                                           header={
                                               "username": name,
                                               "message": "connected",
                                               "destination": " "
                                           },
                                           on_message=on_message,
                                           on_error=on_error,
                                           on_close=on_close,
                                           )
            wsapp.on_open = on_open
            wsapp.run_forever(
                skip_utf8_validation=True, ping_interval=10, ping_timeout=8)
        except Exception as e:
            print("Websocket connection Error  : {0}".format(e))
        if connected:
            print("Reconnecting websocket  after 10 sec")
            time.sleep(10)


f = Path('name.json')
if f.is_file():
    f = open('name.json')
    data = json.load(f)
    name = data['client']['deviceName']
else:
    val = input("Enter Client Device Name: ")
    data = {"client": {"deviceName": val}}
    with open('name.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    name = name = data['client']['deviceName']
    f.close()
    # todo figure out why the client needs to be restarted when name is assigned
#########################################################################


def useInput():
    global connected
    time.sleep(2)
    dest = ""
    send_msg("connected", dest)
    while connected:
        dest = input("enter DEST (q to close): ")
        if dest == 'q':
            connected = False
            print("Disconecting...")
            send_msg("close", dest)
            time.sleep(1)
            wsapp.close()
            print("Closing...")
        else:
            smsg = input("enter msg (q to close): ")
            if smsg == 'q':
                connected = False
                print("Disconecting...")
                send_msg("close", dest)
                time.sleep(1)
                wsapp.close()
                print("Closing...")
            else:
                send_msg(smsg, dest)
                time.sleep(.3)
def startClient():
    try:
        __create_ws()
    except Exception as err:
        print(err)
        print("connect failed")

if __name__ == "__main__":
    try:
        __create_ws()
    except Exception as err:
        print(err)
        print("connect failed")