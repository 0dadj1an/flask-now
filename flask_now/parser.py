from argparse import ArgumentParser

class Parser(object):

    def __init__(self):
        self.__architecture = ""
        self.__package_list = ['flask']
        self.__valid_packages = ["admin", "ask", "assets", "autoindex", "babel", "bootstrap", "bcrypt", "cache", "celery", "classy", "cors",
                                 "couchdb", "couchdbkit", "creole", "dance", "dashed", "debugtoolbar", "exceptional", "filling",
                                 "flatpages", "fluiddb", "gae-mini-profiler", "genshi", "gravatar", "heroku", "htmlbuilder",
                                 "lesscss", "lettuce", "limiter", "login", "mail", "mako", "migrate", "misaka", "mongoalchemy",
                                 "mongokit", "oauth", "openid", "pewee", "ponywhoosh", "principal", "pymongo", "queryinspect",
                                 "raptor", "rest-jsonapi", "restful", "restless", "script", "seasurf", "security", "shelve",
                                 "sijax", "sqlalchemy", "sse", "static-compress", "stormpath", "testing", "themes", "uploads",
                                 "user", "via", "weasyprint", "webtest", "wtf", "xml-rpc", "zen", "zodb", "frozen"]
        self.__valid_architectures = ["mvc", "simple"]

    def parse(self):
        argument_parser = ArgumentParser("Read the docs: http://flask-now.readthedocs.io/en/latest/")
        argument_parser.add_argument("architecture", nargs=1, choices=self.__valid_architectures, help="Architectural type of your project: http://flask-now.readthedocs.io/en/latest/#supported-architectural-patterns")
        argument_parser.add_argument("extensions", nargs="+", choices=self.__valid_packages, help="Desired extensions:")
        arguments = argument_parser.parse_args()
        self.__architecture = arguments.architecture[0]
        self.__package_list.append(arguments.extensions)

        return self.__architecture, self.__package_list
