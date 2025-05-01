def get_user_input():
    user_input_number = int(input("Give e number: "))
    return user_input_number

def split_number(number):
    digits = [int(digit) for digit in str(number)]
    return digits

# Call the function to get user input and print the result
number = get_user_input()
digits = split_number(number)
print(f"The digits of the number {number} are: {digits}")

def divisor(digits):
    divisors = []
    for i in digits :
        if i == 0:
            continue
        elif number % i == 0:
            divisors.append(i)
    return divisors

result = divisor(digits)
count_divisors = len(result)
if count_divisors > 0:
    print(f"The number {number} has {count_divisors} divisors.")    
else:
    print("The number is zero, so it has no divisors.")
