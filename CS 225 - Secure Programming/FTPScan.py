
# The script scan for vulernabilitis in FTP servers
# The script uses the socket module to connect to the server
import socket
socket.setdefaulttimeout(100)
s = socket.socket()
# The script attempt to connect to the IP using port 21
s.connect(("127.0.0.1",21))
ans = s.recv(1024)
if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print ("[+] FreeFloat FTP Server is vulnerable.")
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print ("[+] 3CDaemon FTP Server is vulnerable.")
elif ("Ability Server 2.34" in banner):
    print ("[+] Ability FTP Server is vulnerable.")
elif ("Sami FTP Server 2.0.2" in banner):
    print ("[+] Sami FTP Server is vulnerable.")
else:
    print ("[-] FTP Server is not vulnerable.")

#"modules can exploit a stack based buffer overflow on Sami FTP Server 2.0.1.
#The vulnerability exists in the processing of LIST commands.
#In order to trigger the vulnerability, the "Log" tab must be viewed
#in the Sami FTP Server managing application, in the target machine.
#On the other hand, the source IP address used to connect with the FTP Server is needed.
#If the user can't provide it, the module will try to resolve it.
#This module has been tested successfully on Sami FTP Server 2.0.1 over Windows XP SP3."
#Source: Rapid7 => https://www.rapid7.com/db/modules/exploit/windows/ftp/sami_ftpd_list
# https://www.cvedetails.com/vulnerability-list/vendor_id-2048/product_id-3494/version_id-395129/Karjasoft-Sami-Ftp-Server-2.0.1.html   
