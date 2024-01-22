############################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 lab 4
############################################

def knapsack(capacity, items):
    if items == [] or capacity <= 0:
        return [0, []]
    if items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use_it = knapsack(capacity - items[0][0], items[1:])
        use_it[0] = use_it[0] + items[0][1]
        use_it[1] = [items[0]] + use_it[1]
        lose_it = knapsack(capacity, items[1:])
        if use_it[0] > lose_it[0]:
            return use_it
        return lose_it

