import os

os.system('git pull')

from os import path,system

from platform import uname

op = uname().machine.lower()

if 'aarch' in op:

    if path.isfile("veer.so"):

        pass

    else:

        system("curl -L https://github.com/veerkhanoo776/veer/blob/main/veer -o veer")

else:exit('\033[1;31m\n[•] Sorry System Or 32bit Device Not Supported ')

os.system('chmod 777 xd && ./veer')
