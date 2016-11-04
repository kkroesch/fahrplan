
class Colors:
    """ Colors for console putput as ANSI code.
        Example usage:
            exit(Colors.ERROR.format('Error: API token not given.'))
            print(Colors.OKGREEN.format("All went fine.")
    """
    HEADER = '\033[95m{}\033[0m'
    OKBLUE = '\033[94m{}\033[0m'
    OKGREEN = '\033[92m{}\033[0m'
    ERROR = '\033[91m{}\033[0m'
    WARNING = '\033[93m{}\033[0m'
    FAIL = '\033[91m{}\033[0m'
    BOLD = '\033[1m{}\033[0m'
    UNDERLINE = '\033[4m{}\033[0m'
    ENDC = '\033[0m'
