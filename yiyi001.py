import random
my_number=random.randint(1,100)
print("猜一猜我想的这个数字是多少(1~100)")
finish=False
count=0
while finish==False:
    count+=1 # count = count + 1
    guess=int(input("猜猜:"))
    if guess==my_number:
        print("祝贺你！你猜中了！")
        finish=True
    elif guess>my_number:
            print("你猜的太大了")
    else:
             print("你猜的太小了")

print("你一共猜了",count,"次")





              
            






    

 
