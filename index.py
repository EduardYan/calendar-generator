#!/usr/bin/python3

"""
This is a program for generate
html calendars fast.

Example Use:
---------------------------------------

For see alls the commands and your defaults values.
python3 index.py -h

python3 index.py -p ~/mypages -f mypage.html -y 2022 -c ./css/calendar.css
python3 index.py -p ~/mypages

"""

import calendar
import os
from models.page import Page
from args import get_args
from messages.success import PAGE_SAVE
from messages.errors import PROBLEM_TO_SAVE, YEAR_INVALID


def save_page(PATH:str, FILENAME:str, PAGE_CONTENT:bytes) -> None:
    """
    Save the content passed
    for parameter.
    """

    # to string
    PAGE_CONTENT = PAGE_CONTENT.decode()

    # concatenation with /FILENAME for not problems
    with open(PATH + f'/{FILENAME}', 'w') as f:
        f.write(PAGE_CONTENT)
        f.close()


def fix_page(PATH:str) -> None:
    """
    Fix the page
    deleting the first line
    a or modified other lines, for not xml page.
    """

    with open(PATH, 'r') as f:
        lines = f.readlines()
        f.close()

    with open(PATH, 'w') as f:
        first_line = lines[0]

        # assing the new value for not xml document
        lines[1] = '<!DOCTYPE html>\n'

        for line in lines:
            # validating for not write this two lines
            if line != first_line:
                f.write(line)

        f.close()


def generate_calendar() -> calendar.HTMLCalendar:
    """
    Return a tuple
    with the model of calendar to use.
    """

    # generating
    html_calendar = calendar.HTMLCalendar()

    return html_calendar


def main(PATH:str, FILENAME:str, YEAR:str, CSS_NAME:str) -> None:
    """
    Principal
    function for execute the program.
    """

    # validating the year
    if not YEAR.isdigit():
        print('-------------------------------------------------------')
        print(YEAR_INVALID)
        print('-------------------------------------------------------')

    else:
        # creating models
        html_calendar = generate_calendar()

        page_content = html_calendar.formatyearpage(
                # setting for the calendar
                theyear = int(YEAR),
                css = CSS_NAME
        )

        page = Page(page_content)

        try:
            save_page(PATH, FILENAME, page.content)
            print('-----------------------------------')
            print(PAGE_SAVE.format(PATH = PATH))
            print('-----------------------------------')
            fix_page(PATH + f'/{FILENAME}') # fixing
        except FileNotFoundError:
            print('-----------------------------------------------------------')
            print(PROBLEM_TO_SAVE)
            print('-----------------------------------------------------------')


if __name__ == '__main__':

    # getting options
    options = get_args()
    PATH_TO_SAVE = options.path
    FILENAME = options.filename
    YEAR = options.year
    CSS_NAME = options.css_name

    # executing main
    main(
            PATH_TO_SAVE,
            FILENAME,
            YEAR,
            CSS_NAME
    )
