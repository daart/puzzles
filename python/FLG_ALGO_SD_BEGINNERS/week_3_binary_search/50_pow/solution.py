def pow(x, n):

    def helper_recursive(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = helper_recursive(x * x, n // 2)

        return x * res if n % 2 else res
    
    res = helper_recursive(x, abs(n))

    return res if n >= 0 else 1 / res

