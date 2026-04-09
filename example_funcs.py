def add(a, b):
    return a + b
  

def multiply(a, b):
    return a * b
  
  
def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b
    

if __name__ == '__main__':
    print(add(3, 5))
    print(multiply(5, 3))
    print(subtract(5, 3))
    print(divide(10, 2))
    try:
        divide(10, 0)
    except ValueError as e:
        print(e)