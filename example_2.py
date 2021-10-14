a=input('Enter string: ')
aa=a.split()

aa.reverse()
aa.append('!')
aa.insert(0,'!')
a=''.join(aa)

print (a)

