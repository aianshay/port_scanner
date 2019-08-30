from socket import *
import time
import threading
from queue import Queue

def port_scan(ip:str, timeout:float, i:int):
    target_ip = gethostbyname(ip + str(i) + '.115')
    socketa = socket()
    socketa.settimeout(timeout)
    
    return socketa.connect_ex((target_ip,873)),target_ip

if __name__ == '__main__':
    target_191 = '10.191.'   
    target_194 = '10.194.'

    start_time = time.time()

    count = 0

    for i in range(1,110):      
        teste_191 = port_scan(target_191, 0.5, i)

        if(teste_191[0] == 0):
            print ('\nHost: ', teste_191[1],'\nPort 873: OPEN')  
            count += 1
        else:
            teste_194 = port_scan(target_194, 2, i)

            if(teste_194[0] == 0) :
                print ('\nHost: ', teste_194[1],'\nPort 873: OPEN')  
                count += 1

print('\nTime taken:', time.time() - start_time)
print('Number of NAS found:', count)
