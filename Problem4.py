from NumberTests import isPrime
from NumberTests import fibonacciSequence

def main():
    total = 0
    for p in range(2, 2000000):
       if isPrime(p):
          total = total + p
    print(total)
          

if __name__ == '__main__':
  main()