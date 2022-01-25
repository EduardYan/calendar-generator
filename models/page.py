"""
This file have a model
for the page
"""

class ContentPageError(TypeError):
    """
    Execption if the content
    for create a page not is valid,
    or not is a bytes values.
    """
    pass


class Page:
    """
    Create a new page
    with this properties:

    -----
    content:bytes
    -----

    """
    def __init__(self, content:bytes) -> None:

        if type(content) not in [bytes]:
            # launching in case not is bytes
            raise ContentPageError(f'The content passed for create a page must be bytes not -- {type(content)} --')

        # values
        self.content = content


    def __str__(self) -> str:
        return 'This is a page'
