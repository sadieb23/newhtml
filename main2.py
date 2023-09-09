import random
import time

#fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

#generate a random number between 15 and 35 (inclusive)
n = random.randint(15, 35)

#record the start time
start_time = time.time()

#calculate the nth Fibonacci number
result = fibonacci(n)

#record the end time
end_time = time.time()

#calculate the elapsed time
elapsed_time = end_time - start_time

#prints result and execution time
print(f"f({n}) = {result}")
print(f"f({n}) took {elapsed_time:.6f} seconds")

#used chatgpt for help 