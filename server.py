import socket as sc
import time
import pandas as pd
import numpy as np
from misc import *

try:
    x=pd.read_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
except:
    file_path=input(str('Enter CSV File Path: '))
    x=pd.read_csv(file_path)

CMsgs1=x.CMsgs.dropna()       
read(x.CMsgs)

x_copy=CMsgs1.copy()
x.drop(columns=['CMsgs'], inplace=True)
x.SMsgs=x.SMsgs.dropna().reset_index().drop(columns='index')
check(0, x_copy)

i=input(str("Wait to read? (y/n): "))
if i=='y':
    time.sleep(20)
    
else:
    pass

sc.setdefaulttimeout(10)
s = sc.socket()
host = sc.gethostname()
print(f"Server starts on host: {host}")

port = 8080
s.bind((host, port))

print("")
print("Server bound to host and port successfully")
print("")
print("Server is waiting for incoming connection")
print("")


try:
    s.listen(1)
    conn, addr = s.accept()


    sc.setdefaulttimeout(None)
    print(f"{addr} has connected to the server and is now online")
    print("")



    while 1:
        
        message = input(str('>>'))
        if message not in np.array(('/e', '/h', '/a', '/c', '/v')):
            message = message.encode()
            
            conn.send(message)
            print("Message has been sent")
            print("")
            
            
            inc_msg = conn.recv(1024)
            inc_msg = inc_msg.decode()
            print(f"Client: {inc_msg}")
            print()

        else:
            if message == '/e':
                conf = input(str('y/n: '))
                if conf=='y':
                    exit()

            elif message == '/h':
                print("Welcome to the Server side Chat Monitor! This utilises csv and socket modules to provide a smooth experience of a private chat! Don't mind the kinks... ")
                print("There are just 5 commands in our command line. They are as follows:")
                print("/e -- Exits the application")
                print("/h -- The command used to get here. It's the command for help, if you didnt get it yet")
                print("/a -- Gives a formatted automatic reply")
                print("/c -- Clears the cache/backup chats")
                print("/v -- To view the backup chats again")
                print("")
                

            elif message == '/a':
                msg = 'Server is very busy! Will reply shortly!'
                msg = msg.encode()
                conn.send(msg)
                inc_msg = conn.recv(1024)
                inc_msg = inc_msg.decode()
                print(f"Client: {inc_msg}")
                print()

            elif message == '/c':
                conf = input('Clear ALL backup messages?(y/n): ')
                if conf == 'y':
                    x.drop(columns=['CMsgs', 'SMsgs'], inplace=True)
                    try:
                        x.to_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
                    except:
                        x.to_csv(file_path)

            elif message == '/v':
                C_cache = x.CMsgs.copy()
                C_cache.dropna(inplace=True)
                iterate(C_cache)
                

except:
    cont = input("Save messages offline?(y/n): ")
    temp_ser = pd.Series(dtype = 'object') 
    temp_df = pd.DataFrame(columns=['SMsgs', 'CMsgs'])

    while cont == 'y':
        message = pd.Series(input(str('>>')))
        temp_ser = temp_ser.append(message)
        cont=input(str('Continue? (y/n): '))

    temp_df['SMsgs'] = temp_df['SMsgs'].append(temp_ser, ignore_index=True)

    x = x.append(temp_df, ignore_index=True)

try:
    y=pd.read_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
except:
    y=pd.read_csv(file_path)

a=check(1, x_copy, ser1=y.CMsgs)
c=y.CMsgs.copy()
for i in range(len(c)):
    if a[i]==True:
        c.drop(i, inplace=True)
    else: continue

y.CMsgs=c.dropna().reset_index().drop(columns='index')

x.CMsgs=y.CMsgs.dropna().reset_index().drop(columns='index')

try:
    x.SMsgs=y.SMsgs.append(temp_df['SMsgs'], ignore_index=True)
except:
    x.SMsgs=y.SMsgs.dropna().reset_index().drop(columns='index')
rem_na(x.CMsgs, x.SMsgs)
x.dropna(thresh=1, inplace=True)
x.set_index('SMsgs', inplace = True)

try:
    x.to_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
except:
    x.to_csv(file_path)
try:
    del temp_df, temp_ser
except: pass

s.close()
exit()



