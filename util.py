class Map(dict):
    """ Access JSON objects with 'dot notation'
        
        From: http://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
        Example:
            m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


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
