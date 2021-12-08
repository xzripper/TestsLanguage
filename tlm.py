from tl import TestsLanguage
from sys import argv


imp = 3

if len(argv) == imp:
    file = argv[1]
    prexc = argv[2].lower()

    src = TestsLanguage(file)

    if prexc == 'y':
        print(f'Exit code: {src.run()};')

    elif prexc == 'n':
        src.run()

    else:
        src.run()

elif argv == ['tlm.py', '--version'] or argv == ['tlm.py', '--vrs']:
    print(f'Version of language: {TestsLanguage.version};')

elif argv == ['tlm.py', '--information'] or argv == ['tlm.py', '--info']:
    print(f'Simple language for tests on Python. Version is {TestsLanguage.version};')

elif len(argv) != imp:
    print('Missing some important arguments. Example: "tl #Additionally: <Version>, <Information> <@File> <@PrintExitCode: N>".')
