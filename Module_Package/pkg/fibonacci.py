class Fibonacci:
    def __init__(self,title='피보나치'):
        self.title = title
        
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
    
    def fib2(n):
        result =  []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

# f1 = Fibonacci()
# f1.fib(10) # self 인자가 없어서 오류

# Fibonacci.fib(20)
# print(Fibonacci.fib2(20))