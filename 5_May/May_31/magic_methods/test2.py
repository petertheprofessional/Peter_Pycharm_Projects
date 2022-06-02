import time

x, y, mod = 999, 888, 44


start = time.time()
print((x ** y) % mod)
stop = time.time()
print('Elapsed time for (x ** y) % mod:', stop - start)


start = time.time()
print(pow(x, y, mod))
stop = time.time()
print('Elapsed time for pow(x, y, mod):', stop - start)