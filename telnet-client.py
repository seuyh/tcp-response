import telnetlib
import time

connect = telnetlib.Telnet('localhost', 9879)
connect.write(b'0003 C1 01:13:02.999 00\n')
time.sleep(1)

