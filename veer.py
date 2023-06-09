import os, sys, platform

 

os.system('rm -rf khan.cython-311.so  khan.cython-311.so')

 

try:

    if sys.argv[1]=='update':

        os.system('rm -rf khan.cython-311.so  khan.cython-311.so')

except:

    pass

 

 

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('Sarfraz.so'):

        os.system('curl -L https://github.com/veerkhanoo776/veer/blob/main/khan.cpython-311.so?raw=true -o khan.cython-311.so') 

        import khan

    else:

        import khan

 

elif bit == '32bit':

    if not os.path.isfile('khan.cython-311.so'):

        os.system('curl -L https://github.com/veerkhanoo776/veer/blob/main/khan.cpython-311.so?raw=true -o khan.cython-311.so') 

        import khan

    else:

        import khan



    





















    


























    

    




















 

