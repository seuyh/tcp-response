import telnetlib
import time

connect = telnetlib.Telnet('localhost', 9879)
connect.write(b'0002 C1 01:13:026.877 00\n')
time.sleep(1)

