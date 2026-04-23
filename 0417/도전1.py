salaries = [200, 250, 300, 280, 500]
def modify(values, factor) :
    for e in values:
        e=e*factor
print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)

#값이 같다. 원소를 복사해 가져와서