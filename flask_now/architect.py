from .writer import Writer


class Architect(object):
    def __init__(self, architecture, package_list):
        self.__architecture = architecture
        self.__package_list = package_list

    def __create_mvc_architecture(self):
        self.__create_mvc_app()

    def __create_simple_app(self):
        writer = Writer()
        writer.create_config_file_simple(filename="config.py")
        writer.create_simple_run()
        writer.create_build_now(self.__architecture, self.__package_list)

    def __create_mvc_app(self):
        # Create config file
        writer = Writer()
        writer.create_config_file(filename="project/config.py")
        writer.create_run_py(filename="run.py")
        writer.create_init_py(filename="project/__init__.py")
        writer.create_contoller_py(filename="project/controller.py")
        writer.create_model_py(filename="project/models.py")
        writer.create_style(filename_css="project/static/css/style.css",
                            filename_js="project/static/js/script.js")
        writer.create_templates(filename="project/templates/index.html")
        writer.create_build_now(self.__architecture, self.__package_list)

    def build(self):
        if self.__architecture.lower() == "mvc":
            self.__create_mvc_architecture()
        else:
            self.__create_simple_app()
