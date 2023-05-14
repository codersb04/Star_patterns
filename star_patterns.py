#print star traingle
print("-----Triangle-------")
row = 7
for i in range(1, row, 1):
    for j in range(0,i):
        print('*',end='')
    print()

print("------diamond---------")
#print star diamond
row1 = 5
for i in range(1, row1+1):
    for j in range (1, row1-i+1):
        print(' ',end='')
    for k in range(1, 2*i):
        print('*',end='')
    print()
for i in range(row1-1,0,-1):
    for j in range (1, row1-i+1):
        print(' ',end='')
    for k in range(1, 2*i):
        print('*',end='')
    print()

print("------Hollow Square---------")
#print hollow star
row2=5
for i in range(row2):
    for j in range(row2):
        if i==0 or i==row2-1 or j==0 or j==row2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print("-------Solid Square---------")
#print solid square of star
rows=6
for i in range (rows):
    for j in range(rows):
        print('*',end='')
    print()

print("-------Hollow diamond--------")
#print hollow of star
row1 = 5
for i in range(1, row1+1):
    for j in range (1, row1-i+1):
        print(' ',end='')
    for k in range(1, 2*i):
        if k==1 or k== 2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(row1-1,0,-1):
    for j in range (1, row1-i+1):
        print(' ',end='')
    for k in range(1, 2*i):
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print("------Parellelogram--------")
#print star in the shape of parellelogram
row =5
for i in range(1,row+1):
    for j in range(1, row-i+1):
        print(' ', end='')
    for k in range(1,row+1):
        print('*',end='')
    print()

print("-------Shape of Arrow-----------")
#print star in the shape of arrow
row=6
for i in range(1,row):
    for j in range(i):
        print('*',end='')
    print()
for i in range(row,1,-1):
    for j in range(i):
        print('*',end='')
    print()


print("-------Shape of Heart-----------")
#print star in the shape of heart
row=7
for i in range(row):
    for j in range(row):
        if i==0 and j%3 != 0 or i ==1 and j%3==0 or i-j==2 and i+j==8:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print("-------Shape of tower-----------")
#print star in the shape of tower
n=5
x=[]
for i in range(1,n+1):
    a=""
    for j in range(1,(n*2-1)+1):
        if j in range((n-(i-1)),(n+(i-1)+1)):
            a=a+"*"
        else:
            a=a+" "
    print(a)
print()