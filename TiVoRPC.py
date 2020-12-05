from pypresence import Presence
import time
import socket
import json
import sys

## Load Config File
with open ('config.json') as config:
    configjson = json.load(config)
    print("Config Loaded")
    
## TiVo TCP Config
TCP_IP = configjson['tivo_ip']
TCP_PORT = 31339
BUFFER_SIZE = 30

## RPC Config
client_id = configjson['client_id']
large_image = configjson['large_image']
RPC = Presence(client_id)
RPC.connect()

pcn = ''

## Get Current Channel
def getChan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data = s.recv(BUFFER_SIZE)
    s.close()
    ccn = ''.join(filter(str.isdigit, str(data)))[1:]
    return ccn

## Get Channel Name From Number
def getName(num):
    num = int(num)
    with open('virgin_channel_guide.json') as guide:
        data = json.load(guide)
        for i in data['channels']:
            if i['num'] == num:
                return (i['name'])
        return False

## RPC Updater 
def updateRPC():
    global pcn
    ccn = getChan()
    name = getName(ccn)
    if ccn == pcn:
        return("No need to update, sleeping for 5 seconds")
    elif ccn.isnumeric() == False:
        return("Error while grabbing current channel, ensure that TiVo IP is correct or that multiple instances aren't running")
    else:
        pcn = ccn
        if name == False:
            return RPC.update(state="Channel " + ccn, large_image=large_image, large_text="Channel " + ccn, start=time.time())
        else:
            return RPC.update(state="Channel " + ccn, details=name, large_image=large_image, large_text="Channel " + ccn, start=time.time())
        

## The Magic Stuffs
while True:
    try:
        print(updateRPC())
        time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
        RPC.close()
        sys.exit()
