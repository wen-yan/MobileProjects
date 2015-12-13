def fib(n):
    def pow(n):
        if n<=1:
            return [1,1,1,0]
        if n%2==1:
            t=pow(n-1)
            return [t[0]+t[1],t[0],t[2]+t[3],t[2]]

        t=pow(n/2)
        result = [t[0]*t[0]+t[1]*t[2],
        t[0]*t[1]+t[1]*t[3],
        t[2]*t[0]+t[3]*t[2],
        t[2]*t[1]+t[3]*t[3]]
        return result
    t=pow(n)
    return t[0]
print fib(10000)