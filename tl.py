from tlassets import *
from tlexc import *


class Test:
    def __init__(self, func, returns) -> None:
        """Create test."""
        if func != returns:
            print(f'{Fore.RED}* Test failed. *{Fore.WHITE}\n {Fore.BLUE} [] {func} != {returns} [] {Fore.WHITE} \n{Fore.RED}* Test failed. *{Fore.WHITE}\n')

        elif func == returns:
            print(f'{Fore.GREEN}* Test passed. *{Fore.WHITE}\n {Fore.BLUE} [] {func} == {returns} [] {Fore.WHITE} \n{Fore.GREEN}* Test passed. *{Fore.WHITE}\n')

        else:
            print('\n* Test. *\nError.\n* Test. *\n')

class TestsLanguage:
    version = 1.0

    def __init__(self, sourcefile: str) -> None:
        """Main class of language. Constructor."""
        self.breaks = True
        self.codes = {'bad': 1, 'good': 0, 'unknown': 2}
        self.kwd = ('#use', '@', '$', ';')
        self.kwdd = {'include': self.kwd[0], 'create': self.kwd[1], 'commentary': self.kwd[2], 'end': self.kwd[3]}
        self.pointer = ' => '
        self.nwl = '\n'
        self.empty = ''

        if not exists(sourcefile) or not sourcefile.endswith('.tl'):
            self.srcf = None

            exc(Exceptions.TLException, 'invalid file', self.breaks)

        elif exists(sourcefile) and sourcefile.endswith('.tl'):
            self.srcf = sourcefile

    @staticmethod
    def delcache() -> int:
        """Delete cache. (__pycache__)."""
        if exists('__pycache__'):
            rmtree('__pycache__')

        return 0

    def readsrc(self) -> Union[None, str]:
        """Read a source from file."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            with open(self.srcf, 'r') as src:
                return src.read()

    def getlines(self) -> Union[None, list]:
        """Get lines from source file."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            _l = self.readsrc().split(self.nwl)

            for l in _l:
                if l.rstrip().lstrip() != self.empty:
                    if not l.endswith(self.kwdd['end']):
                        exc(Exceptions.TLSyntaxError, 'missing semicolon', self.breaks)

            lines = [line.rstrip().lstrip() for line in self.readsrc().split(f'{self.kwdd["end"]}{self.nwl}')]

            if lines == []:
                return []

            else:
                if lines[-1] == self.empty:
                    lines.pop()

                if lines[-1][-1] == self.kwdd['end']:
                    lines[-1] = lines[-1][:-1]

                return lines

    def getincludes(self) -> Union[None, list]:
        """Get includes from source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            lines = self.getlines()
            includes = [line for line in lines if str(line).startswith(self.kwdd['include'])]

            if includes == []:
                return []

            else:
                if includes[-1][-1] == self.kwdd['end']:
                    includes[-1] = includes[-1][:-1]

                return includes

    def getmodules(self) -> Union[None, list]:
        """Get all imported modules from source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            includes = self.getincludes()
            modules = []

            if includes == []:
                return []

            else:
                for include in includes:
                    modules.append(include.split(' ')[1][1:][:-1])

                return modules

    def getltests(self) -> Union[None, list]:
        """Get language tests from source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            lines = self.getlines()
            tests = [line for line in lines if str(line).startswith(self.kwdd['create'])]

            return tests

    def getteststree(self) -> Union[None, list]:
        """Get tree of tests from source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            tests = self.getltests()
            tree = {}

            for test in tests:
                test = str(test[1:])
                returns = test.split(self.pointer)

                tree[returns[0]] = returns[1]

            return tree

    def getcomments(self) -> Union[None, list]:
        """Get commentaries from source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            lines = self.getlines()
            comments = [line for line in lines if self.iscom(line)]

            return comments

    def parsetests(self) -> Union[None, list]:
        """Get tests as string."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            tree = self.getteststree()
            parsed = []

            for func in tree:
                parsed.append(f'Test({func}, {tree[func]})')

            return parsed

    def getdata(self) -> Union[None, list]:
        """Parse all source."""
        if self.srcf is None:
            return None

        elif self.srcf is not None:
            data = [self.getlines(), self.getincludes(), self.getmodules(), self.getltests(), self.getteststree(), self.getcomments(), self.parsetests()]

            return data

    def iscom(self, string: str) -> bool:
        """Is string a commentary."""
        return string.startswith(self.kwdd['commentary'])

    def execcode(self, code: str) -> None:
        """Exec a line, or big code."""
        try:
            return exec(code)
        except SyntaxError as SynErr:
            exc(Exceptions.TLSyntaxError, str(SynErr), self.breaks)

        except NameError as NmErr:
            exc(Exceptions.TLNameError, str(NmErr), self.breaks)

        except Exception as Exc:
            exc(Exceptions.TLException, str(Exc), self.breaks)

    def run(self) -> Union[None, int]:
        """Run file. Main function of class."""
        if self.srcf is None:
            return self.codes['bad']

        elif self.srcf is not None:
            modules = self.getmodules()
            tests = self.parsetests()
            instance = ''

            for module in modules:
                instance += f'from {module} import *{self.nwl}'

            for test in tests:
                instance += f'{test}{self.nwl}'

            instance += self.nwl

            self.execcode(instance)

            return self.codes['good']

@register
def clch():
    """Clean cache."""
    TestsLanguage.delcache()
