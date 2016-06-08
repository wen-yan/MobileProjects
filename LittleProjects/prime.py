from math import sqrt, ceil

n = 1000000

def primes(limit):
    sieve = [False] * (limit + 1)

    def toggle(i):
        sieve[i] = True if sieve[i] == False else False

    def clean(i):
        if sieve[i] == True:
            sieve[i] = False

    def isPrime(i):
        return sieve[i]

    sqrtLimit = int(ceil(sqrt(limit)))

    for i in xrange(sqrtLimit):
        for j in xrange(sqrtLimit):
            ii = i * i
            jj = j * j

            # n = 4*i^2 + j^2
            n = 4 * ii + jj
            if n <= limit:
                m = n % 12
                if m == 1 or m == 5:
                    toggle(n)

            # n = 3*i^2 + j^2
            n -= ii
            if n < limit and n % 12 == 7:
                toggle(n)

            # n = 3*i^2 - j^2
            if i > j:
                n = n - 2 * jj
                if n < limit and n % 12 == 11:
                    toggle(n)

    for i in xrange(5, sqrtLimit):
        if isPrime(i):
            k = i * i
            for j in xrange(k, limit, k):
                clean(j)

    result = [2, 3] + [x for x in xrange(len(sieve)) if isPrime(x) and x >= 5]
    return result

def printPrimes():
    result = primes(n)
    j = 0
    for i in result:
        print "%8d" % i,
        j += 1

        if j % 8 == 0:
            print

def test(n):
    result = primes(n)
    index = 0
    found = []
    for x in xrange(2, n):
        xsqrt = int(ceil(sqrt(x)))

        isPrime = True
        for y in found:
            if y > xsqrt:
                break
            if x % y == 0:
                isPrime = False
                break

        if isPrime:
            found.append(x)
            if x != result[index]:
                print "error !!! %d is prime, but result is %d" % (x, result[index])
                return
            index += 1
    print "test success."
    
#test(n)
printPrimes()
    