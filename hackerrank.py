# # https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    # Write your code here
    str_n = str(n)
    dividers = 0
    for i in str_n:
        if i != "0" and n % int(i) == 0:
            dividers +=1
    return dividers

"""---------------------------------------------"""
# # https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    return_s = ""
    uppercase_ = True
    for i in s:
        if (i != " ") and not i.isnumeric() and uppercase_ :
            return_s += i.upper()
            uppercase_ = False
        elif i == " ":
            return_s += i
            uppercase_ = True
        else:
            return_s += i
            uppercase_ = False
    return return_s