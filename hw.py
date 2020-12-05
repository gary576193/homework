import re
import sys

flag=1
#n=input()
n=sys.argv[1]
s=set()
list1=[]

if re.search('[0-9]',n) is None:
    x='缺少數字'
    s.add(x)
    flag=0

if re.search('\W',n) is None:
    if re.search('_',n) is None:
        x='缺少符號'
        s.add(x)
        flag=0

if re.search('[a-z]',n) is None:   
    x='缺少字母'
    s.add(x)
    flag=0
        
if len(n)<8:
    x='長度少於8'
    s.add(x)
    flag=0

if len(n)>16:
    x='長度大於16'
    s.add(x)
    flag=0 

if re.search('[A-Z]',n) is None:   
    x='缺少字母大寫'
    s.add(x)
    flag=0       

for i in range(len(n)-1):
    if ord(n[i])+1 == ord(n[i+1]) or ord(n[i])+33 == ord(n[i+1]):
        flag=0
        x='數字或字母連續'
        s.add(x)
        flag=0 
        
if flag==1:
    print('Success')
else:
    print('Fail')
    for i in s:
        print(i)
