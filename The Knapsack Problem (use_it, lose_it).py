def knapsack(capacity, items):
    if not items or not capacity: #Base Cases
        return 0
    if capacity < items[0][0]: #if the first item doesn't fit in the bag
        return knapsack(capacity, items[1:])
    else:
        use_it = items[0][1] + knapsack(capacity - items[0][0], items[1:]) #Keep item
        lose_it = knapsack(capacity, items[1:])
        return max(use_it, lose_it)
def testCode(x):

      return lambda t : t + 30 % x == (x - 2)

fun = testCode(7)

print(fun(4))
