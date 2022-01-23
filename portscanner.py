import socket
import datetime
import os


print(''' 
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
\n                         By: João Assalim

''')

ports_opened = []
ports = [21, 23, 25, 80, 110, 143, 443, 445, 8080 ]


def scan_ports(adress):

    print(f'[*] Starting scanning {adress} in ports {ports}\n')

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((adress, port))
        if result ==0:
            print(f'[+] Port {port} open')
            ports_opened.append(f'[+] Port {port} open\n')
        else:
            print(f'[-] Port {port} closed')

def save_scan():

    title = f'Scan {adress} - {datetime.datetime.now().date()}'

    if not os.path.isdir(f'{os.getcwd()}\\{title}.txt'):
        create_file = open(f'{title}.txt', 'w')

    create_file.write(f'{title}: \n')
    for i in ports_opened:
        create_file.write(i)
    

if __name__ == '__main__':
    adress = input('Adress to scan: ')
    
    try:
        scan_ports(adress)
        save = input('Save Scan? [Y]es or [N]o: ').upper()
        
        if save.startswith('Y') or save == 'Y':
            save_scan()

    except valueError as e:
        print('Error', e)
