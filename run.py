
#coding=utf-8
import os, sys, platform

os.system('rm -rf KEVIN')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf KEVIN')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KEVIN'):
        os.system('curl -L https://github.com/K3V1N-XD/NXT/blob/main/KEVIN?raw=true -o KEVIN') 
        os.system('chmod 777 KEVIN;./KEVIN')
    else:
        os.system('chmod 777 KEVIN;./KEVIN')
