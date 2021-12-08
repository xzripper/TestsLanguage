class Exceptions:
    TLSyntaxError = 'TLSyntaxError'
    TLNameError = 'TLObjectUndefined'
    TLException = 'TLException'

def exc(exception: str, message: str, kill: bool) -> None:
    """Raise language exception."""
    print(f'\nAn exception raised;\n\t{exception}: {message};\n;Exc\n')

    if kill:
        exit(1)
