"""
Project Title:  Programming Journal
Author: Shawn Norris
Location: Carrollton, Missouri, USA

"""

import json
import random
import sys
import os
from datetime import date
from datamanager import DataManager


def main():
    """Loop program until user exits

    :return: None
    """

    print("---Welcome to your programming journal---")

    while True:
        display_menu()
        get_user_choice()


def display_menu():
    """Display menu of user choices

    :return: None
    """

    print(
        """
        What do you want to do?
        
        1. New journal entry
        2. Search all entries
        3. Read all entries
        4. Exit
        """
    )


def get_user_choice():
    """Get user's entry from menu choices and call assigned functions
    :return: None
    """

    user_input = input("Make your choice: ")
    # os.system('clear')

    match user_input:
        case "1":
            user_entry = input("\nWhat did you learn today? \n")
            dm.insert_entry(date=date.today(), entry=user_entry)
        case "2":
            user_query = input("\nEnter search term: ")
            search_results = dm.search_entries(query=user_query)
            display_entries(entries=search_results)
        case "3":
            all_entries = dm.select_all_entries()
            display_entries(entries=all_entries)
        case "4":
            quote = get_quote()
            sys.exit(f"\n{quote['text']}\n"
                     f"--{quote['author']}\n\n")


def get_quote():
    """Load a funny quote about programming from a JSON file

    :return: dict of quote: author
    """

    with open('quotes.json') as fin:
        data = json.load(fin)
        quote = random.choice(data)

    return quote


def display_entries(entries):
    """Display entries from journal database

    :param entries: list of dates, journal entries
    :return: None
    """

    if entries:
        for row in entries:
            print(f"\n{row[0]}\n")
            print(f"{row[1]}\n")
    else:
        print()
        print("No entries found")


if __name__ == "__main__":
    dm = DataManager()
    main()
