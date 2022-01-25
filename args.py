"""
This module have some
functions for use, for get
and work with the arguments
of the program.
"""

import optparse
import os
from datetime import datetime
from messages.help import (
        PATH_MESSAGE,
        FILENAME_MESSAGE,
        YEAR_MESSAGE,
        CSS_MESSAGE
)


# functions for configuration
get_year_current = lambda:str(datetime.now().year)
get_path_installation = lambda:os.getcwd() + '/pages/'

def get_args():
    """
    Return a tuple
    with the args passed
    in the execution
    of index file
    """

    parser = optparse.OptionParser()

    # creating options
    parser.add_option('-p', '--path', dest = 'path', default = get_path_installation(), help = PATH_MESSAGE)
    parser.add_option('-f', '--file', dest = 'filename', default = 'page.html' , help = FILENAME_MESSAGE)
    parser.add_option('-y', '--year', dest = 'year', default = get_year_current(), help = YEAR_MESSAGE)
    parser.add_option('-c', '--css', dest = 'css_name', default = './css/calendar.css', help = CSS_MESSAGE)

    options, args = parser.parse_args()

    del args # delete for not use

    return options
