#!/usr/bin/env python3

from collections import namedtuple

MyExpense = namedtuple('MyExpense', ('type_', 'amount'))


def summarize_expenses(min_amount, input):
    expenses = {}
    for expense in input:
        if expense.amount >= min_amount:
            if not expense.type_ in expenses:
                expenses[expense.type_] = 0
            expenses[expense.type_] = expenses[expense.type_] + expense.amount

    for (expense, amount) in sorted(expenses.items(), key=lambda e: e[1], reverse=False):
        print(expense.type_, amount)

# test data
# TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
foo = [MyExpense('food', 4), MyExpense('food', 3), MyExpense('car', 3), MyExpense('dog', 1)]
summarize_expenses(2, foo)
