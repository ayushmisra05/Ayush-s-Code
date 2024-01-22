def change(amount, coins):
    if not coins:
        return float("inf")
    elif amount <= 0:
        return 0
    elif coins[-1] > amount:
        return change(amount, coins[0:-1])
    else:
        use_it = 1 + change(amount - coins[-1], coins)
        lose_it = change(amount, coins[0:-1])
        return min(use_it, lose_it)
