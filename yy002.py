print('A')
print(ord('A'))
print('B')
print(ord('B'))
print('a')
print(ord('a'))
print('2')
print(ord('2'))
message=input("请输入英文：")
message=message.upper()
print(message)
code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
      "--","-.","---",".--.","--.-",".-.","...","-",
      "..-","...-",".--","-..-","-.--","--..",]
#print(ord('A')-ord('A'))
#print(code[ord('A')-ord('A')])
#print(ord('B')-ord('A'))
#print(code[ord('B')-ord('A')])
#print(ord('I')-ord('A'))
#print(code[ord('I')-ord('A')])


output=""
for letter in message:
    value=ord(letter)-ord('A')
    if value>=0 and value<26:
        output+=code[value]+" "
    else:
        output+="1"
print("莫尔斯电码是",output)        
