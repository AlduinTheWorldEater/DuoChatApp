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

SMsgs1=x.SMsgs.dropna()
read(x.SMsgs)

x_copy=SMsgs1.copy()
x.drop(columns='SMsgs', inplace=True)
x.CMsgs=x.CMsgs.dropna().reset_index().drop(columns='index')

check(0, x_copy)

s = sc.socket()
host = input(str("Please enter hostname of the server: "))
try:
    
    port = 8080
    s.connect((host, port))
    print("Connected to chat server")

    while 1:
        inc_msg = s.recv(1024)
        inc_msg = inc_msg.decode()
        print(f"Server: {inc_msg}")
        print("")

        msg = input(str(">>"))
        if msg not in np.array(('/e', '/h', '/a', '/cs', '/cc', '/v')):
            msg = msg.encode()
            s.send(msg)
            print("Message has been sent")
            print("")
        else:
            if msg == '/e':
                conf = input(str('y/n: '))
                if conf == 'y':
                    exit()
            elif msg == '/h':
                print("Welcome to the Client side Chat Monitor! This utilises csv and socket modules to provide a smooth experience of a private chat! Don't mind the kinks... ")
                print("There are just 6 commands in our command line. They are as follows:")
                print("/e -- Exits the application")
                print("/h -- The command used to get here. It's the command for help, if you didnt get it yet")
                print("/a -- Gives a formatted automatic reply")
                print("/cs -- Clears the Server side cached messages")
                print("/cc -- Clears the Client side cached messages")
                print("/v -- To view the cached messages for the client")

                msg = input('>>')
                s.send(msg.encode())
                print("Message has been sent")
                print("")
                
            elif msg == '/a':
                msg = 'Client is not looking at his computer! Please repeat the message!'
                msg = msg.encode()
                s.send(msg)

            elif msg == '/cs':
                x.SMsgs = x.SMsgs.drop([i for i in range(0, len(x.SMsgs))])
                try:
                    x.to_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
                except:
                    x.to_csv(file_path)
                print("All Server side message cache cleared")
                msg=input('>>')
                s.send(msg.encode())
                print("Message has been sent")
                print("")

            elif msg == '/cc':
                x.CMsgs = x.CMsgs.drop([i for i in range(0, len(x.CMsgs))])
                try:
                    x.to_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
                except:
                    x.to_csv(file_path)
                print("Client side message cache cleared")
                msg=input('>>')
                s.send(msg.encode())
                print("Message has been sent")
                print("")

            elif msg == '/v':
                conf = input('You want to view the Server message cache?(y/n): ')
                if conf == 'y':
                    S_cache = x.SMsgs.copy()
                    S_cache.dropna(inplace=True)
                    iterate(S_cache)
                else: continue
                msg = input('>>')
                s.send(msg.encode())
                print("Message has been sent")
                print("")
    
               
                
except:
    cont=input('Save messages offline?(y/n): ')
    temp_ser = pd.Series(dtype='object')
    temp_df = pd.DataFrame(columns=['SMsgs', 'CMsgs'])

    while cont == 'y':
        msg=pd.Series(input(str('>>')))
        temp_ser = temp_ser.append(msg)
        cont = input(str('Continue? (y/n): '))

    temp_df['CMsgs'] = temp_df['CMsgs'].append(temp_ser, ignore_index=True)
    
    x=x.append(temp_df, ignore_index=True)
try:
    y=pd.read_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
except:
    y=pd.read_csv(file_path)

a=check(1, x_copy, ser1=y.SMsgs)
c=y.SMsgs.copy()

for i in range(len(c)):
    if a[i]==True:
        c.drop(i, inplace=True)
    else: continue

y.SMsgs=c.dropna().reset_index().drop(columns='index')

x.SMsgs=y.SMsgs.dropna().reset_index().drop(columns='index')

try:
    x.CMsgs=y.CMsgs.append(temp_df['CMsgs'], ignore_index=True).dropna().reset_index().drop(columns='index')
    
except:
    x.CMsgs=y.CMsgs.dropna().reset_index().drop(columns='index')

rem_na(x.SMsgs, x.CMsgs)

x.dropna(thresh=1, inplace=True)

x.set_index('SMsgs', inplace=True)
try:
    x.to_csv(r'C:\Users\Aniru\OneDrive\Documents\Temp.csv')
except:
    x.to_csv(file_path)

try:
    del temp_df, temp_ser
except: pass

s.close()
exit()
        

