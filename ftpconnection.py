Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import ftplib
... session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
... file = open('data.txt','rb')                  # file to send
... session.storbinary('STOR data.txt', file)     # send the file
... file.close()                                    # close file and FTP
