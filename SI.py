if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit()

p = eval(sys.argv[1])
r = eval(sys.argv[2])
t = eval(sys.argv[3])

si = (p * r * t) / 100

print("Simple Interest =", si)