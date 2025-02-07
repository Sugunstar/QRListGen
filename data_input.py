print("enter data")
f=open('file.txt','a')
print("enter 'END' to end inputing data")

flag = 0
st=""
while (flag != 1):
    st=""
    st=input()
    f.write(st)
    f.write('\n')
    if(st == "END"):
        flag=1

    