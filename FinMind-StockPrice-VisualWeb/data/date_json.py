import os, sys
import time
import json
 
if len(sys.argv) ==2:
    f1 = sys.argv[1]
else:
    print('usage: date_json.py fcode.csv ')
    sys.exit(1)
 
if not os.path.exists(f1):
    print("Error: %s not found." % f1)
    sys.exit(1)
 
fn,ext = os.path.splitext(f1)
if len(fn) !=4:
    print('Error: len(%s) !=6' % fn)
    sys.exit(1)
if ext !='.csv':
    print('Error: %s is not .csv' % f1)
    sys.exit(1)
 
fp = open(f1,'r')
fp.readline()
 
f2 = fn +'.json'
fp2 = open(f2,'w')
fp2.write('{"code":1,"msg":"OK","data":')
ts=0  # timestamp
jz = float('0.0')
alist =[]
for line in fp:
    date,jz,lljz = line.strip().split(',')
    time1 = time.strptime(date, "%Y/%m/%d")
    ts = int(time.mktime(time1))*1000
    jz = float(jz)
    alist.append([ts,jz])
#
json.dump(alist,fp2)
fp2.write('}')
fp2.close()
fp.close()