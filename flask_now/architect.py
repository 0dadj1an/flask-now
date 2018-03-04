from .extensions.now import NowMvcExtension, NowSimpleExtension
from .extensions.flask import FlaskMvcExtension, FlaskSimpleExtension


class Architect(object):
    def __init__(self, architecture, package_list):
        self.__architecture = architecture
        self.__package_list = package_list

    @staticmethod
    def create_mvc_app():
        now_mvc = NowMvcExtension()
        flask_mvc = FlaskMvcExtension()

        # Now extension creates config
        now_mvc.config()

        # Flask creates run
        flask_mvc.run_imports()
        flask_mvc.run_variables()
        flask_mvc.run_methods()

        # Flask creates models
        flask_mvc.model_imports()
        flask_mvc.model_variables()
        flask_mvc.model_methods()

        # Flask creates controller
        flask_mvc.controller_imports()
        flask_mvc.controller_variables()
        flask_mvc.controller_methods()

        # Flask creates statics
        flask_mvc.default_css()
        flask_mvc.default_js()

        # Flask creates templates
        flask_mvc.index_html()

        # Flask creates __init__
        flask_mvc.init_imports()
        flask_mvc.init_variables()
        flask_mvc.init_methods()

    @staticmethod
    def create_simple_app():
        now_simple = NowSimpleExtension()
        now_simple.config()

        flask_simple = FlaskSimpleExtension()
        flask_simple.run_imports()
        flask_simple.run_variables()
        flask_simple.run_methods()

    def build(self):
        if self.__architecture.lower() == "mvc":
            self.create_mvc_app()
        else:
            self.create_simple_app()
