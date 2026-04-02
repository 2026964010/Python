import math
print("각도\tsin값\tcos값")
for degree in range(0, 91, 10):
    radian = 3.14 * degree / 180.0
    s = math.sin(radian)
    c = math.cos(radian)
    print(f"{degree}\t{s:.3f}\t{c:.3f}")