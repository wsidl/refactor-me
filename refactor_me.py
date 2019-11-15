#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter

Expense = namedtuple('Expense', ('category', 'amount'))


def sum_expenses(expenses, min_amount=0):
    """Aggregates all Expense entries into a categorized list of sums

    Args:
        expenses (iter(Expense)): Iterable of Expenses to be summed
        min_amount (int): Minimum value to match to be included with the result

    Returns:
        dict: Category-grouped results of summed values
    """
    aggregated_expenses = defaultdict(int)
    for category, amount in expenses:
        if amount >= min_amount:
            aggregated_expenses[category] += amount
    return aggregated_expenses


def print_expenses(expenses):
    """Takes a dictionary and prints the results to the command line

    Args:
        expenses (dict): Values to output to command line
    """
    for expense, amount in sorted(expenses.items(), key=itemgetter(1)):
        print(expense, amount)


if __name__ == '__main__':
    # TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3), Expense('dog', 1))
    print_expenses(sum_expenses(test_expenses, 2))
