string1="silent"
string2="listen"


def anagram(x, y):
    if len(x) == len(y):
        if sorted(x) == sorted(y):
            print("yes it is an anagram")
        else:
            print("no its not an anagram")
    else:
        print("NO")


anagram(string1, string2)

print(sorted(string1))
print(sorted(string2))
string3 = "MALAYALAM"

print(string3)
print(sorted(string3, reverse=True))


'''def palindrome(x):
    for i in range(0, int(len(x))//2):
        if x[i] != x[len(x)-i-1]:
            print("not Palindrome")
    else:
        print(" Palindrome")
a=3
b=6
print(a//b)

palindrome(string3)'''

i="greating"
print(i[2:3]
