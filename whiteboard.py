def movezero(a):
    c = 0
    while 0 in a:
        a.remove(0)
        c += 1
    while c > 0:
        a.append(0)
        c -= 1
    return a   


a = [0,0,1,0,2,0,4]
print(movezero(a))