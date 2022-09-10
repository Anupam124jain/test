def get_si(p, r, t):
    
    si = p * r * t/100

    return si

#inut parms
p = 8000
r = 6
t = 1

#get si result
si = get_si(p, r, t)

print(si)