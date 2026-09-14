def fizzbuzz(n):
    l = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')

        else:
            l.append(str(i))

    return l

res1 = fizzbuzz(3)
print(res1)
res2 = fizzbuzz(5)
print(res2)
res3 = fizzbuzz(15)
print(res3)