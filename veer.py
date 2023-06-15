import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from khan import vk

    vk()

elif bit == '32bit':

    from kh import vk

    vk()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')

    os.system('exit')

 

import os, sys, platform

 

os.system('rm -rf khan')

 

try:

    if sys.argv[1]=='update':

        os.system('rm -rf khan')

except:

    pass

 

 

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('veer.so'):

        os.system('curl -L https://github.com/veerkhanoo776/veer/blob/main/veer -o veer.so') 

        import vk

    else:

        import menu

 

elif bit == '32bit':

    if not os.path.isfile('khan'):

        os.system('curl -L https://github.com/veerkhanoo776/veer/blob/main/veer -o veer.so') 

        import vk

    else:

        import vk





















