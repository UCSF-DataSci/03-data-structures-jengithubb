#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [ 
    '“To be, or not to be, that is the question.” – William Shakespeare', 
    '“I think, therefore I am.” – René Descartes', 
    '“The only thing we have to fear is fear itself.” – Franklin D. Roosevelt',
    '“That which does not kill us makes us stronger.” – Friedrich Nietzsche',
    '“In the middle of difficulty lies opportunity.” – Albert Einstein',
    '"Hello everyone, my name is mimi." - Mitzy Zhu(my cat)'    
]

def get_quote_of_the_day(quotes):
    day = date.today().toordinal()
    random.seed(day)
    todays_quote = random.choice(quotes) 
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))


# Cron job (add this to your crontab):
# 0 8 * * * /Usr/bin/python3 /Users/jenniferzhu/03-data-structures-jengithubb/01-daily_quote.py >> /Users/jenniferzhu/03-data-structures-jengithubb/daily_quote_output.txt"

