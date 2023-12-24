from string import ascii_lowercase
import doctest

def clear_text(text:str):
    """
    Clear text
    >>> clear_text('text') == 'text'
    True
    >>> clear_text('TexT') == 'text'
    True
    >>> clear_text('te.xT') == 'text'
    True
    >>> clear_text('TФФффext') == 'text'
    True
    >>> clear_text('TeЯ..xT') == 'text'
    True
    """
    result = ''
    for i in text:
        if i.lower() in ascii_lowercase + ' ':
            result += i
    return result.lower()

if __name__ == '__main__':
    doctest.testmod(verbose=True)