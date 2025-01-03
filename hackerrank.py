### Hacker Rank
#Question 1
#https://www.hackerrank.com/challenges/find-digits/problem
# Bir tamsayı d, tamsayı n'in böleni ise, n % d = 0 olduğunda bu durumu sağlar.
# Bir tamsayı verildiğinde, bu sayıyı oluşturan her bir rakamı kontrol edin ve bu rakamın n'in böleni olup olmadığını belirleyin. Sayı içinde geçen bölenlerin sayısını bulun.
# Örnek:
# makefile
# Kodu kopyala
# n = 124
# 1, 2 ve 4 rakamlarının her birinin 124 sayısının böleni olup olmadığını kontrol edin. 1, 2 ve 4, 124'ü bölebilir, bu nedenle sonuç 3 olacaktır.
# n = 111
# 1, 1 ve 1 rakamlarının her birinin 111 sayısının böleni olup olmadığını kontrol edin. 1, 1 ve 1, 111'i bölebilir, bu nedenle sonuç 3 olacaktır.
# n = 10
# 1 ve 0 rakamlarının her birinin 10 sayısının böleni olup olmadığını kontrol edin. 1, 10'u böler, ancak 0 bölemez. Bu yüzden sonuç 1 olacaktır.
# Fonksiyon Açıklaması
# Aşağıdaki fonksiyonu tamamlayın:
# python
# Kodu kopyala
# findDigits(n: int) -> int
# Parametreler:
# n: Kontrol edilecek tam sayı.
# Döndürülecek Sonuç:
# int: n sayısındaki rakamların, n'in böleni olduğu rakam sayısı.
# Girdi Formatı:
# İlk satırda bir tam sayı t bulunur, bu da test durumu sayısını belirtir.
# Sonraki t satırın her birinde bir tam sayı n bulunur.
# Kısıtlamalar:
# 1 ≤ t ≤ 15
# 0 ≤ n < 10^9
# Örnek Girdi:
# 2
# 12
# 1012
# Örnek Çıktı:
# 2
# 3
# Açıklama:
# 12 sayısı iki rakama ayrılır: 1 ve 2. 12 sayısı hem 1'e hem de 2'ye bölünebilir, bu yüzden sonuç 2'dir.
# 1012 sayısı dört rakama ayrılır: 1, 0, 1 ve 2. 1012 sayısı 1, 1 ve 2 ile tam bölünebilir, ancak 0 ile bölünemez, çünkü sıfıra bölme tanımsızdır. Bu yüzden sonuç 3'tür.
#Answer 1
import math  # Imports the 'math' module, though not used here
import os  # Imports the 'os' module to interact with the operating system
import random  # Imports the 'random' module, though not used here
import re  # Imports the 're' (regular expressions) module, though not used here
import sys  # Imports the 'sys' module, though not used here

# Complete the 'findDigits' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def findDigits(n):  # Defines the 'findDigits' function which takes 'n' (an integer) as a parameter.
    count = 0  # Initializes a variable 'count' to keep track of the valid digits divisible by 'n'.
    for digit in str(n):  # Converts the integer 'n' to a string and iterates over each digit as a character.
        d = int(digit)  # Converts the current character back to an integer.
        if d != 0 and n % d == 0:  # Checks if the digit is not zero and divides 'n' without a remainder.
            count += 1  # If both conditions are true, increments the count.
    return count  # Returns the count of digits that divide 'n'.

if __name__ == '__main__':  # Main function execution starts here.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Opens a file for writing the output (system/environment specified path).

    t = int(input().strip())  # Reads the number of test cases 't' from user input and converts it to an integer.

    for t_itr in range(t):  # Iterates through each test case 't_itr'.
        n = int(input().strip())  # For each test case, reads an integer 'n' from input.

        result = findDigits(n)  # Calls the 'findDigits' function and stores the result.

        fptr.write(str(result) + '\n')  # Writes the result of the function into the output file.

    fptr.close()  # Closes the file after writing all outputs.


#Question 2
#https://www.hackerrank.com/challenges/capitalize/problem
#Answer 2
import math  # Imports the 'math' module, though not used here.
import os  # Imports the 'os' module for file interaction.
import random  # Imports the 'random' module, though not used here.
import re  # Imports the 're' module, though not used here.
import sys  # Imports the 'sys' module, though not used here.

# Complete the solve function below.
def solve(name):  # Defines the 'solve' function, which accepts a string 'name' as input.
    return ' '.join(word.capitalize() for word in name.split())  # Splits the string by spaces, capitalizes the first letter of each word, and joins them back into a string.

if __name__ == '__main__':  # Main function execution starts here.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Opens a file for writing the output.

    s = input()  # Reads the input string 's'.

    result = solve(s)  # Calls the 'solve' function on 's' and stores the result.

    fptr.write(result + '\n')  # Writes the result into the output file.

    fptr.close()  # Closes the file after writing all outputs.

