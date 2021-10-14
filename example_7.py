a=input('Enter: ').split()
a1=int(a[0])
a2=int(a[1])
if a1>1 and a1<5:
    print (a1,'  рубля')
    if a2>1 and a2<5:
        print (a2, ' копейки')
    elif a2>4 or a2==0:
        print (a2, ' копеек')
    elif a2==1:
        print (a2, ' копейка')
elif a1>4 or a1==0:
    print (a1,' рублей')
    if a2>1 and a2<5:
        print (a2, ' копейки')
    elif a2>4 or a2==0:
        print (a2, ' копеек')
    elif a2==1:
        print (a2, ' копейка')
elif a1==1:
    print (a1, ' рубль')
    if a2>1 and a2<5:
        print (a2, ' копейки')
    elif a2>4 or a2==0:
        print (a2, ' копеек')
    elif a2==1:
        print (a2, ' копейка')


