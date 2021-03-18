from random import *
beichushu=input("第一个数的位数=")
n=eval(beichushu)

fuhao=input("符号(加法,减法,乘法,除法中选一个)=")

chushu=input("第二个数的位数=")
j=eval(chushu)

timushu=input("题目数量=")
t=eval(timushu)

yushu=-1

timu="题目：\n"
daan="答案：\n"
for i in range(t):
    diergeshu=randint(10**(j-1),10**j-1)
    diyigeshu=randint(10**(n-1),10**n-1)
    while diyigeshu==1:
        diyigeshu=randint(10**(n-1),10**n-1)
    if fuhao=="加法":
        jieguo=diyigeshu+diergeshu
        dayinfuhao="＋"
    elif fuhao=="减法":
        jieguo=diyigeshu-diergeshu
        dayinfuhao="－"
    elif fuhao=="乘法":
        jieguo=diyigeshu*diergeshu
        dayinfuhao="×"
    elif fuhao=="除法":
        jieguo=diyigeshu//diergeshu
        yushu=diyigeshu%diergeshu
        dayinfuhao="÷"
    timu+=str(diyigeshu)+dayinfuhao+str(diergeshu)+" = "+"\n"
    if yushu!=-1:
        dayinyushu="......"+str(yushu)
    else:
        dayinyushu=""
    daan+=str(diyigeshu)+dayinfuhao+str(diergeshu)+" = "+str(jieguo)+dayinyushu+"\n"
print(timu)
print(daan)
