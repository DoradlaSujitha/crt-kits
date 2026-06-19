#1.square of alphabet AAAAA BBBBB CCCCC DDDDD EEEEE FFFFFF GGGGGGG HHHHHHHH IIIIIIIII JJJJJJJJJJ KKKKKKKKKKK LLLLLLLLLLLL MMMMMMMMMMMMM NNNNNNNNNNNN OOOOOOOOOOOOO PPPPPPPPPPPPP QQQQQQQQQQQQQ RRRRRRRRRRRRRR SSSSSSSSSSSSSS TTTTTTTTTTTTTT UUUUUUUUUUUUUU VVVVVVVVVVVVVV WWWWWWWWWWWWWWW XXXXXXXXXXXXXXX YYYYYYYYYYYYYYYY ZZZZZZZZZZZZZZZZ
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()

#2.square of alphabet AAAA BBBBB CCCCC DDDDD EEEEE FFFFFF GGGGGGG HHHHHHHH IIIIIIIII JJJJJJJJJJ KKKKKKKKKKK LLLLLLLLLLLL MMMMMMMMMMMMM NNNNNNNNNNNN OOOOOOOOOOOOO PPPPPPPPPPPPP QQQQQQQQQQQQQ RRRRRRRRRRRRRR SSSSSSSSSSSSSS TTTTTTTTTTTTTT UUUUUUUUUUUUUU VVVVVVVVVVVVVV WWWWWWWWWWWWWWW XXXXXXXXXXXXXXX YYYYYYYYYYYYYYYY ZZZZZZZZZZZZZZZZ
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()

#3.square of alphabet A B C D A B C D A B C D A B C D A B C D
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()

#4.square of alphabet D C B A D C B A D C B A D C B A
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()

#5.square of alphabet  aaaa bbbb cccc dddd eeee ffff gggg hhhh iiii jjjj kkkk llll mmmm nnnn oooo pppp qqqq rrrr ssss tttt uuuu vvvv wwww xxxx yyyy zzzz
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()

#6.square of alphabet zzzz yyyy xxxx wwww vvvv uuuu tttt ssss rrrr qqqq pppp oooo nnnn mmmm llll kkkk jjjj iiii hhhh gggg ffff eeee dddd cccc bbbb aaaa
n = int(input("Enter a number: "))  
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()

#7.square of alphabet a b c d a b c d a b c d a b c d a b c d
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()

#8.square of alphabet d c b a d c b a d c b a d c b a d c b a
n = int(input("Enter a number: "))  
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()

#9.Rightangletriangle of alphabet A B B C C C D D D D E E E E E F F F F F F G G G G G G G H H H H H H H H I I I I I I I I I
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()

#10. Rightangletriangle of alphabet A  A B  B  B C  C  C  C D  D  D  D  D E  E  E  E  E  E F  F  F  F  F  F  F G  G  G  G  G  G  G  G H H H H H H H H H
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()

#11.Rightangletriangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))
for i in range(n):  
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()

#12.Rightangletriangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()

#13.Rightangletriangle of alphabet a b b c c c d d d d
n= int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()

#14. Rightangletriangle of alphabet a ab abc abcd 
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1): 
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()

#15.Rightangletriangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))
for i in range(n):  
    for j in range(i + 1):
        print(chr(100 - i), end=" ")
    print()

#16.Rightangletriangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(100 - j), end=" ")
    print()

#17.left angletriangle of alphabet a  bb ccc dddd
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()

#18.left angletriangle of alphabet a a b  a b c  a b c d
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + j), end=" ")
    print()

#19.left angletriangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + n - i - 1)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()

#20.left angletriangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + n - j - 1), end=" ")
    print()

#21.left angletriangle of alphabet A BB CCC DDDD
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(65 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()

#22.left angletriangle of alphabet A A B  A B C  A B C D
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

#23.left angletriangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(65 + n - i - 1)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()

#24.left angletriangle of alphabet D DC DCB DCBA
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + n - j - 1), end=" ")
    print()

#25.Equalateral triangle of alphabet a bb ccc dddd
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + i), end=" ")
    print()

#26.Equalateral triangle of alphabet a a b  a b c  a b c d
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + j), end=" ")
    print()

#27.Equalateral triangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))  
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(96 + n - i), end=" ")
    print()

#28.Equalateral triangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(96 + n - j), end=" ")
    print()

#29.Equalateral triangle of alphabet A BB CCC DDDD
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")
    print()

#30.Equalateral triangle of alphabet A A B  A B C  A B C D
n = int(input("Enter a number: "))  
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

#31.Equalateral triangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))  
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()

#32.Equalateral triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()

#33.downward triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    print("  " * i, end=" ")          
    for j in range(n - i):
        print(chr(68 - i) , end=" ")
    print()

#34.downward triangle of alphabet ABCD ABC AB A
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()

#35.downward triangle of alphabet AAAA BBB CC D
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(65 + i) , end=" ")
    print()

#36.downward triangle of alphabet DCBA DCB DC D
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(68 - j), end=" ")
    print()

#37.downward triangle of alphabet aaaa bbb cc d
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(97 + i) , end=" ")
    print()

#38.downward triangle of alphabet dcba dcb dc d
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(97 + n - j - 1), end=" ")
    print()

#39.downward triangle of alphabet abcd abc ab a
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(97 + j), end=" ")
    print()

#40.downward triangle of alphabet dddd ccc bb a
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(97 + n - i - 1) , end=" ")
    print()

#41.downward triangle of stars **** *** ** *
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print("*", end=" ")
    print()

#42.downward  equalateral triangle of stars DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(68 - i), end=" ")
    print()

#43.downward  equalateral triangle of stars ABCD ABC AB A
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()

#44.downward  equalateral triangle of stars AAAA BBB CC D
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(65 + i), end=" ")
    print()

#45.downward  equalateral triangle of stars DCBA DCB DC D
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(68 - j), end=" ")
    print()

#46.downward  equalateral triangle of stars dddd ccc bb a
n = int(input("Enter a number: "))  
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(97 + n - i - 1), end=" ")
    print()

#47.downward  equalateral triangle of stars abcd abc ab a
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(97 + j), end=" ")
    print()

#48.downward  equalateral triangle of stars aaaa bbb cc d
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(97 + i), end=" ")
    print()

#49.downward  equalateral triangle of stars dcba dcb dc d
n = int(input("Enter a number: "))
for i in range(n): 
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(97 + n - j - 1), end=" ")
    print()

#50.square pattern of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65 
for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#51.square pattern of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#53.rigtangle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#54.rigtangle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#55.downward triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#56.downward triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#57.left angle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#58.left angle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#59.downward left angle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4 
ch = 65
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#60.downward left angle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#61.downward equalateral triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#62.downward equalateral triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#63.equalateral triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#64.equalateral triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):  
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#65.combinations of number and stars 1*** 22** 3333* 4444
n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------")

#66.combinations of number and stars 1*** 12** 123* 1234
n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------------------")

#67.equalateral triangle of alphabets a bbb ccccc dddddd
n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    print(chr(97 + i) * (2 * i + 1))
print("--------------------------------")

#68.equalateral triangle of alphabets a aba abcbc abcdcba
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(97 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(97 + j), end="")
    print()
print("----------------------")

#example of word pattern
n="Hello"
for i in range(len(n)):
    for j in range(len(n)):
        print(n[i], end=" ")
    print()
print("-----------------")

#69. square Word pattern
n = "python"
for i in range(len(n)):
    for j in range(len(n)):
        print(n[i], end=" ")
    print()
print("------------------------------")

#70.rigth angel triangel of word pattern
n = "python"
for i in range(len(n)):
    for j in range(i + 1):
        print(n[j], end=" ")
    print()
print("---------------------------")

#71.rigthangle triangle of word pattern p yy ttt hhhh ooooo nnnnnn
n = "python"
for i in range(len(n)):
    for j in range(i + 1):
        print(n[i], end=" ")
    print()
print("--------------------------")

#72.square of python
n = "python"
rev = n[::-1]
for ch in rev:
    for i in range(len(n)):
        print(ch, end=" ")
    print()
print("-------------------------")

#73.downwrd triagnle of word pattern 
n = "python"
for i in range(len(n), 0, -1):
    for j in range(i):
        print(n[j], end=" ")
    print()
print("-----------------------------------")

#74.right angle triangle of a word pattern
n = "python"
for i in range(1, len(n) + 1):
    for j in range(i):
        print(n[j], end=" ")
    print()
print("--------------------------------")

#75.downward triangle of word pattern
word = "python"
rev = word[::-1]   # python -> nohtyp
n = len(rev)
for i in range(n):
    for j in range(n - i):
        print(rev[i], end=" ")
    print()

#76.downward left angle triangle of word pattern
word = "python"
n = len(word)
for i in range(n):
    print("  " * i, end="")
    for j in range(i, n):
        print(word[j], end=" ")
    print()
print("-------------------------")

#77.palindrom words in a sentence 
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    if word.lower() == word.lower()[::-1]:
        print(word)
print("-------------------------------")

#78.convert normal sentence to snake_case
sentence = input("Enter a sentence: ")
snake_case = sentence.lower().replace(" ", "_")
print(snake_case)
print("-----------------------------")

#79.reacple the word with asterisks
sentence = input("Enter a sentence: ")
target = input("Enter the target word: ")
result = sentence.replace(target, "*" * len(target))
print(result)
print("--------------------------")

#80.count of non palindromes.
sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:
    if word.lower() != word[::-1].lower():
        count += 1
print("Count of non-palindrome words:", count)
