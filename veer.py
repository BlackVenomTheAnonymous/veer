import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from khan import menu

    menu()

elif bit == '32bit':

    from khan import menu

    menu()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')

    os.system('exit')

 

