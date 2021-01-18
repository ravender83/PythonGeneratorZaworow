import sys


def otworz(sciezka):
    try:
        with open(sciezka, 'r', encoding='windows-1250') as _f:
            _txt = _f.read()
            return _txt
    except IOError as e:
        print(f'I/O error({e.errno}): {e.strerror}')
        return e
    except:  # handle other exceptions such as attribute errors
        print('Unexpected error:', sys.exc_info()[0])
        return None
