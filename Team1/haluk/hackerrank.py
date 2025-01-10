# Find Digits



sayi=int(input())
rakamlar=[]
count=0
for rakam in str(sayi):
    if rakam !='0':
        rakamlar.append(int(rakam))
result= list(map(lambda x: sayi%x==0,rakamlar))
for i in result:
    if i is True:
        count+=1
    elif i is False:
        count+=0
print(count)


# Capitalize



s= input('Bir metin giriniz :')
def solve(s):
    if s[0].isdigit():
        return s
    else:
        return s.title()

print(solve(s))