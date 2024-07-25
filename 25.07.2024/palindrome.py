str = input("Enter the String: ")
rev = ''
for i in str:
    rev = i +rev
if (rev == str):
    print(str,"Is a Palindrome")
else:
    print(str,"Not a palindrome")
        
print("Reverse String: ",rev)
