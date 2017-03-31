#!/usr/bin/env python3

from collections import namedtuple, defaultdict

MyExpense = namedtuple('MyExpense', ('type_', 'amount'))


def sum_expenses(min_amount, input):
    expenses = defaultdict(int)
    for expense in input:
        if expense.amount >= min_amount:
            expenses[expense.type_] += expense.amount

    for expense, amount in sorted(expenses.items(), key=lambda x: x[1], reverse=False):
        print(expense, amount)

# test data
# TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
foo = [MyExpense('food', 4), MyExpense('food', 3), MyExpense('car', 3), MyExpense('dog', 1)]
sum_expenses(2, foo)
