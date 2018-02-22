
class Validator(object):

    def __init__(self, package_list):
        self.__validator_result = False
        self.__package_list = package_list
        self.__valid_packages = ["admin", "ask", "assets", "autoindex", "babel", "bootstrap", "bcrypt", "cache", "celery", "classy", "cors",
                                 "couchdb", "couchdbkit", "creole", "dance", "dashed", "debugtoolbar", "exceptional", "filling",
                                 "flatpages", "fluiddb", "gae-mini-profiler", "genshi", "gravatar", "heroku", "htmlbuilder",
                                 "lesscss", "lettuce", "limiter", "login", "mail", "mako", "migrate", "misaka", "mongoalchemy",
                                 "mongokit", "oauth", "openid", "pewee", "ponywhoosh", "principal", "pymongo", "queryinspect",
                                 "raptor", "rest-jsonapi", "restful", "restless", "script", "seasurf", "security", "shelve",
                                 "sijax", "sqlalchemy", "sse", "static-compress", "stormpath", "testing", "themes", "uploads",
                                 "user", "via", "weasyprint", "webtest", "wtf", "xml-rpc", "zen", "zodb", "frozen"]
                                 
    def validate(self, main_file, architecture):
        self.__package_list.remove(main_file)
        if architecture == "mvc":
            self.__validator_result = True
            if len(self.__package_list) == 0:
                print(
                    "No extension will be added. Just creating a simple, extensionless flask app")
            else:
                print("Creating simple app with following extensions: ",
                      str(self.__package_list))
        else:
            architecture = "simple"
            self.__validator_result = True
            if len(self.__package_list) == 0:
                print("Creating extensionless flask app with " +
                      architecture + " architecture pattern.")
            else:
                print("Creating flask app with " + architecture +
                      " architecture pattern and with following extensions " + str(self.__package_list))

        for package in self.__package_list:
            if not package in self.__valid_packages:
                self.__validator_result = False
                raise ParserException(
                    "There is no extension called: " + str(package) + " in now-flask.")

        return self.__validator_result, self.__package_list
