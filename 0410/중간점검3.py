

def get_rect_area(w, h):
    return w * h


def main():
    w = int(input("w: "))
    h = int(input("h: "))

    area = get_rect_area(w, h)
    return area

print(main())