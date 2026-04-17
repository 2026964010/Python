def getIntRange(a, b, msg):
    while True:
        v = int(input(f"{msg}({a}부터 {b}사이의 값): "))
        if a <= v <= b: return v