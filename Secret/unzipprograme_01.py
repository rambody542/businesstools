import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
  for len in range (min_len, max_len+1):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
      passwd = '  '.join(attempt)
      print(passwd)
      try:
        zFile.extractall(pwd = passwd.encode())
        print(f"Secret Password is {passwd}.")
        return 1
      except:
        pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'Secret\secret123.zip')

min_len = 3
max_len = 3

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
  print("Success of finding secret password")
  
else:
  print("Failture of finding secret password")