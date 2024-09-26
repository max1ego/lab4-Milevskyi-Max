def will_fit(a, b, c, m, n):
   
    min_hole_side = min(m, n)
    max_hole_side = max(m, n)
    
    orientations = [
        (a, b),  
        (a, c),  
        (b, c)   
    ]
    
    for width, height in orientations:
        if min(width, height) <= min_hole_side and max(width, height) <= max_hole_side:
            return True
    
    return False

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
m = float(input("m: "))
n = float(input("n: "))

if will_fit(a, b, c, m, n):
    print("Брусок пройде через отвір.")
else:
    print("Брусок не пройде через отвір.")
