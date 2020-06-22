from essentials import *
import re
import requests
from bs4 import BeautifulSoup
#from automate import *
import sys
#from urllib.request import urlopen

recursivelim=5
if len(sys.argv)>2:
    username=sys.argv[1]
    recursivelim=int(sys.argv[2])
elif len(sys.argv)>1: username=sys.argv[1]
else:
    print('**username needed**\nTry python3 gitcrawler.py <username> <[OPTIONAL] recursivelimit>')
    exit(1)
namelist=set()
f=open('gitTree.htm','w')
f.write(begin)
def generateTree(username,reclim):
    global document
    global namelist
    if reclim>=recursivelim or len(namelist)>100000: return
    nlist=[]
    namelist.add(username)
    url='https://github.com/%s?tab=following'%username
    html=requests.get(url)
    f.write(li+username+xcode+ul)
    bs=BeautifulSoup(html.text,'html.parser')
    nlist=[i.text for i in bs.find_all('span',{'class':re.compile('^link-gray(\spl-1)?$')})]
    for i in nlist:
        if i not in namelist:
            #print(i)
            generateTree(i,reclim+1)
    f.write(xul)
    f.write(xli)


#obj=Wauto()
x=requests.get('https://github.com/%s'%username)
if x.status_code==404:
    print('Specified username doesn\'t exist')
    exit(1) 
generateTree(username,0)
f.write(end)
f.close()
#obj.send()
