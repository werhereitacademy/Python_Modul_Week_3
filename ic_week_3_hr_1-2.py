def sayi_rakam_bolen(n):
    """
    Bu fonksiyon, verilen bir sayının rakamlarının verilen sayıyının tam bölemleri sayısını verir.
   
    """
    adet = 0
    for i in str(n):
        if i != '0' and n % int(i) == 0:
            adet += 1
    return adet

 #   count = 0
  #  for digit in str(n):
  #      if digit != '0':
   #         if n % int(digit) == 0:
    #            count += 1
    #return count

print(sayi_rakam_bolen(1012))


def naam(s):
    words = s.split(" ")
    capitalized_words = [w[0].upper() + w[1:] if w else "" for w in words]
    return " ".join(capitalized_words)

print(naam("ahmet 12mehmet  ali"))


