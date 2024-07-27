import os
st = str(input("Enter the operations:"))
if st == 'create':
    def create():
        f= open('hello7.txt','w')
        f.writelines("hello developer")
    create()
elif st == 'read':  
    def read():
        f=open('hello7.txt','r')
        print(f.readlines())
        
    read()
    
    

os.rename('hello7.txt','dev.txt')


