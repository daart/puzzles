def fill_baskets(fruits):
    counter, l = 0, 0
    basket = {}

    for r in range(len(fruits)):
        # increment if key matched, or set 0 as default
        basket[fruits[r]] = basket.get(basket[fruits[r]], 0) + 1

        while len(basket) > 2:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0:
                del basket[fruits[l]]
            l += 1
        counter = max(counter, r - l + 1)
    return counter