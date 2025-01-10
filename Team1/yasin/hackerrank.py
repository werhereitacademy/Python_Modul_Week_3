#1- HACKERRANK: FIND DIGITS
def sayi_bul(sayi):
    sonuc =0
    for rakam in str(sayi):
        rakam = int(rakam)
        if rakam == 0:
            continue
        if sayi % rakam == 0:
            sonuc += 1
    return sonuc

print(sayi_bul(123))

#2-HACKERRANK: CAPITALIZE
def solve(user_name):
    return user_name.title()
    
user_name = "chris alan"
result = solve(user_name)

print(result)