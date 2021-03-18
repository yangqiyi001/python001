code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
      "--","-.","---",".--.","--.-",".-.","...","-",
      "..-","...-",".--","-..-","-.--","--..",]
message=input("请输入电报：")
message+=" "
chars=""
output=""
for letter in message:
    if letter!=" ":
        chars=chars+letter
    else:
        for index in range(26):
            if code[index]==chars:
                output+=chr(ord('A')+index)
        chars=""
print("英文原文是",output)                                                                                                    
