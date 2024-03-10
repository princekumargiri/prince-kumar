def fibonacci(limit):
    fib_list = [0, 1]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > limit:
            break
        fib_list.append(next_fib)
    return fib_list


