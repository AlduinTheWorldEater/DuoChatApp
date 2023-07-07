import time
import pandas as pd
import os
import matplotlib.pyplot as plt



def iterate(x):
    for i in x: print(i)

def read(y):
    
    if len(y)>0:
        for i in range(0, len(y)): 
            if y.isna()[i] == False:
                print(y.pop(i))
                

def check(x, ser, ser1=None):    
    try:
        if x==0:
            global temp
            temp=ser.copy().dropna()            

        else:
            try:
                global sert
                sert=ser1.copy()
                x1=len(temp)
                x2=len(sert)
                if x1>=x2:
                    i=pd.RangeIndex(0, x1)
                    sert=sert.reindex(i)
                else:
                    i=pd.RangeIndex(0, x2)
                    temp=temp.reindex(i)

                temp1=temp==sert
                return temp1
            except: pass
    except: pass
    
def rem_na(*sers):
    for ser in sers:
        ser=ser.dropna().reset_index().drop(columns='index')

class raw_data:
    def __init__(self):
        self.data = []
    def CPU():
        CPU_Pct = str(os.popen('wmic cpu get loadpercentage').read()).strip()[-3:].strip()
        try:
            CPU_Pct = int(CPU_Pct)
        except:
            CPU_Pct = 0
        return CPU_Pct
    def RAM(mode = None):
        if mode == None:
            RAM_kbytes = float(os.popen('wmic os get freephysicalmemory').read().strip()[-9:].strip())
            return RAM_kbytes
        elif mode in ('MB', 'mb', 'mB', 'Mb'):
            RAM_kbytes = float(os.popen('wmic os get freephysicalmemory').read().strip()[-9:].strip())
            RAM_Mb = RAM_kbytes/1024
            return RAM_Mb
        
        else:
            raise AttributeError

Cpu_data = []
Ram_data = []
RamM_data = []
time_arr = []
def graph_create_plot(col_size):
        fig, axs = plt.subplots(1, col_size)
        plt.subplots_adjust(wspace=1, hspace=1)
        return fig, axs

class graphing:
    def __init__(self):
        self.data = []

    def graph_plot(i, axs=graph_create_plot(3)[1]):
        tm = time.strftime('%H:%M:%S')
        global Cpu_data
        global Ram_data
        global RamM_data
        global time_arr
        time_arr.append(tm)
        try:
            Cpu_data.append(raw_data.CPU())
            axs[0].set_xlabel('Time')
            axs[0].set_ylabel('CPU Usage')
            axs[0].set_title('CPU vs Time plot')
            try:
                axs[0].plot(time_arr, Cpu_data, color = 'blue')
            except Exception as e: print(e)
            
        except Exception as e: print(e, 'THIS IS ERROR!')  
    
        try:
            Ram_data.append(raw_data.RAM())
            axs[1].set_xlabel('Time')
            axs[1].set_ylabel('RAM availability (in kilobytes)')
            axs[1].set_title('RAM(kb) vs Time plot', pad = 10)
            try:
                axs[1].plot(time_arr, Ram_data, color = 'red')
            except Exception as e: print(e)
        except: print('This is Error2')
    
        try:
            RamM_data.append(raw_data.RAM(mode = 'MB'))
            axs[2].set_xlabel('Time')
            axs[2].set_ylabel('RAM availability (in Megabytes)')
            axs[2].set_title('RAM(Mb) vs Time plot')
            try:
                axs[2].plot(time_arr, RamM_data, color = 'magenta')
            except Exception as e: print(e)
        except: print('This is Error 3')

        for i in range(3):
            for tick in axs[i].get_xticklabels():
                tick.set_rotation(75)
        
        try:
            Cpu_data = Cpu_data[-10:]
            Ram_data = Ram_data[-10:]
            RamM_data = RamM_data[-10:]
            time_arr = time_arr[-10:]
            axs[0].set_xlim(left = time_arr[-10], right = time_arr[-1])
            axs[1].set_xlim(left = time_arr[-10], right = time_arr[-1])
            axs[2].set_xlim(left = time_arr[-10], right = time_arr[-1])
            
        except: pass

       

        

        
        

        
