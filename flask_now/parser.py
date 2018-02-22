import sys


class ParserException(Exception):
    pass


class Parser(object):

    def __init__(self):
        self.__architecture = ""
        self.__package_list = []

    def __read_package_list(self):
        if len(sys.argv) > 0:
            for package in sys.argv:
                if package[0] == "-":
                    self.__architecture = package[1:]
                else:
                    self.__package_list.append(package)

    def parse(self):
        self.__read_package_list()
        return sys.argv[0], self.__architecture, self.__package_list
