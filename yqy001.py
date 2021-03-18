from random import *
timu=""
daan=""
for i in range(20):
    liangweishu=randint(10,99)
    sanweishu=randint(100,999)
    ji=liangweishu*sanweishu
    timu+=str(liangweishu)+" * "+str(sanweishu)+" = "+"\n"
    daan+=str(liangweishu)+" * "+str(sanweishu)+" = "+str(ji)+"\n"
print(timu)
print(daan)
