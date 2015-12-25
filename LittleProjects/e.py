import math

def e(accuracy):
    return sum(1.0 / math.factorial(i) for i in range(accuracy))

if __name__ == "__main__":
    print e(100)
