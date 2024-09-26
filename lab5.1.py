import math

def f(x):
    if x > 12.1:
        result = math.log(abs(x - 1)) + math.log10(abs(x**(0.7 * x)) + 2)
    elif -5.7 <= x <= 12.1:
        result = math.e * 4 * x**7 + 2 - x**(1/3)
    elif x < -5.7:
        result = 4.27 * x + 4.33 * x**2 + math.sin(x + 1)
    
    return result

x = float(input("x:"))
print("f(x)=", f(x))