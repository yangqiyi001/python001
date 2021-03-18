from random import *
beichushu=input("被除数位数=")
n=eval(beichushu)

chushu=input("除数位数=")
j=eval(chushu)

timushu=input("题目数量=")
t=eval(timushu)

timu="题目：\n"
daan="答案：\n"
for i in range(t):
    liangweishu=randint(10**(j-1),10**j-1)
    siweishu=randint(10**(n-1),10**n-1)
    while siweishu==1:
        siweishu=randint(10**(n-1),10**n-1)
    shang=siweishu//liangweishu
    yushu=siweishu%liangweishu
    timu+=str(siweishu)+" / "+str(liangweishu)+" = "+"\n"
    daan+=str(siweishu)+" / "+str(liangweishu)+" = "+str(shang)+"......"+str(yushu)+"\n"
print(timu)
print(daan)
