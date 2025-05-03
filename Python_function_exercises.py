#1- Verilen bir kelimeyi belirtilen kez ekrana yazdiran python fonksiyonu yazınız.
#1. Print a Word Multiple Times
def print_word(word, count):
    for i in range(count):
        print(word)

print_word("Hello", 3)


#2- Verilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyonunu yazınız.
#2. Prime Numbers Between Two Numbers
# A prime number is only divisible by 1 and itself.Examples: 2, 3, 5, 7, 11...
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):    #loop through all numbers from 2 up to square root of num. +1 because range is exclusive at the end,it stops before the last number. 
        if num %i == 0:   #check if num is divisible by i
            return False
    return True 

def find_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
find_primes(10, 20)

#3- Saati saniyeye çeviren bir fonksiyon yazınız.
#3. Convert Time to Seconds

def convert_to_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes *60 + seconds
    return total_seconds
print(convert_to_seconds(1, 30, 15))


#4- Matematik, Fizik ve Kimya derslerinin Vize ve Final ortalamalarina gore 
# (Vize nin %40 i , Finalin %60 i) ogrencinin derslerden hangi not ile gectigini veya kaldigini gosteren bir program yaziniz.
#4. Calculate Student Grades (Vize 40%, Final 60%)

def calculate_grade(vize, final):
    average = vize * 0.4 + final * 0.6

    if average >= 85:
        grade = "AA"
    elif average >= 70:
        grade = "BB"
    elif average >= 55:
        grade = "CC"
    elif average >= 45:
        grade = "DD"
    else:
        grade = "FF"
    if average >= 45:
        status = "Passed"
    else:
        status = "Failed"

    print(f"Average: {average:.2f} - Grade: {grade} - Status: {status}")  #:.2f floating point (decimal) numbers

calculate_grade(60, 70)