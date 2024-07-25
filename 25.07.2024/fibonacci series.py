n = int(input("Enter the number : "))
n1,n2 = 0,1
print('fibonacci ser10ies')
for i in range (2,n):
    n3 = n1 +n2
    n1 = n2
    n2 = n3
    print(n3 , end=" ")
