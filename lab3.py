###############################################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 3
#
###############################################################
def change(amount, coins):
    """
    Given a coin amount of money and a list of coin values, this would find the least number of coins that
    makes up that amount of money depending on the currency you provide in the list. For example, the US
    standard currency for coins is: [1, 5, 10, 25, 50]. Calling change(48, [1,5,10,25,50]) would return 6
    since the least amount of coins needed to reach this number is 6 (1 quarter, 2 dimes, 3 pennies).
    """
    if amount <= 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[-1] > amount:
        return change(amount, coins[0:-1])
    else:
        use_it = 1 + change(amount - coins[-1], coins)
        lose_it = change(amount, coins[0:-1])
        return min(use_it, lose_it)
