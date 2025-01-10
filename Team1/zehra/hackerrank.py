# Complete the solve function below.
#https://www.hackerrank.com/challenges/capitalize/problem
#Bonus Question 2

def solve(s):
    x = s.split(" ")
    z = []
    for i in x:
        y = i.capitalize()
        z.append(y)
    f = " ".join(z)

    return f



