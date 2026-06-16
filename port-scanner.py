import socket
import sys
import pyfiglet
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)
print("=" * 50)
print("By: Dwarf".center(90))
print("=" * 50)
print()

target = input("Please enter host to scan: ")
host = socket.gethostbyname(target)

try:
    file = open("Port-scanner.txt", "w")
except FileExistsError:
    print("File already exists. Please delete the file and try again.")
    sys.exit()


date = datetime.date(datetime.now())
t1 = datetime.now()

print("Start time: {}".format(t1.strftime("%H:%M:%S")))
file.write("Start time: {}\n".format(t1.strftime("%H:%M:%S")))

try:

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        result = sock.connect_ex((host, port))
        if result == 0 :
            try:
                print("Port No : {} Open Protocol Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
                file.write("\n Port No : {} Open Protocol Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
            except:
                print("Port No : {} Open Protocol Service Name: {}".format(port, "Unknown"))
                file.write("\n Port No : {} Open Protocol Service Name: {}".format(port, "Unknown"))

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    file.write("\n\nHostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    file.write("\n\nCouldn't connect to server")
    sys.exit()



t2 = datetime.now()
print("End time: {}".format(t2.strftime("%H:%M:%S")))
file.write("\n\nEnd time: {}".format(t2.strftime("%H:%M:%S")))

total = t2 - t1
print("Total time : {}".format(total))
file.write("\n\nTotal time : {}".format(total))