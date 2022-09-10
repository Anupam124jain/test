def get_si(p, r, t):
    
    si = p * r * t/100

    return si

p = 9000
r = 6
t = 1

si = get_si(p, r, t)

print(si)