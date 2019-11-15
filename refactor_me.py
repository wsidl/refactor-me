#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter
from sys import stdout
import io

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


def format_dict(input_dict, write_out=None):
    """Takes a dictionary and prints the results to the command line or other output stream

    Args:
        input_dict (dict): Values to output to command line
        write_out (io.IOBase): Output object that receives the formatted string, defaults writing to terminal
    """
    key_size = max([len(key) for key in input_dict.keys()])
    (write_out or stdout).write(
        ''.join([
            '{: <{}} {}\n'.format(key, key_size, value)
            for key, value in sorted(input_dict.items(), key=itemgetter(1))
        ])
    )


if __name__ == '__main__':
    # TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3), Expense('dog', 1))
    format_dict(sum_expenses(test_expenses, 2))
