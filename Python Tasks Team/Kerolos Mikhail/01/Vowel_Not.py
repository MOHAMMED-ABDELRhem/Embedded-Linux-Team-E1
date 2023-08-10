# This program test a letter if it is vowel or not

Letter = input("Please enter letter : ")

Vowels = ('a','A','e','E','i','I','o','O','u','U')
Flag = 1

for i in Vowels:

    if Letter == i:
        print("Letter " + Letter + " is vowel")
        Flag = 0
        break

    else:
        pass

if Flag == 1:
    print("Letter " + Letter + " is  not vowel")
