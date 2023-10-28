
#coding=utf-8
import os, sys, platform

os.system('rm -rf KLVIN')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf KLVIN')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KLVIN'):
        os.system('curl -L https://github.com/K3V1N-XD/NXT/blob/main/KLVIN?raw=true -o KLVIN') 
        os.system('chmod 777 KLVIN;./KLVIN')
    else:
        os.system('chmod 777 KELVIN;./KELVIN')
