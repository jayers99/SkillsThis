#!/usr/bin/python3

"""module docstring"""

__version__ = "0.1.0"

class JobSearch(dict):
    """my method doc string"""

    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

    def __iter__(self):
        pass

class JobSiteSearch(dict):
    """my method doc string"""

    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

    def __iter__(self):
        pass

class JobSiteDefinition(dict):
    """my method doc string"""

    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

class JobListing(dict):
    """my method doc string"""

    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

def main():
    """docstring"""
    pass

if __name__ == "__main__":
    main()
