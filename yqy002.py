from random import *
timu=""
daan=""
for i in range(20):
    liangweishu=randint(10,99)
    siweishu=randint(1000,9999)
    shang=siweishu//liangweishu
    yushu=siweishu%liangweishu
    timu+=str(siweishu)+" / "+str(liangweishu)+" = "+"\n"
    daan+=str(siweishu)+" / "+str(liangweishu)+" = "+str(shang)+"......"+str(yushu)+"\n"
print(timu)
print(daan)
