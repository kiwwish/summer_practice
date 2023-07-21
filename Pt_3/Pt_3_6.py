print(dict((x, int(str(bin(x))[2:len(str(bin(x)))])) for x in range(1, 10+1)))
