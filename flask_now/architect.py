import os
import base64


class ArchitectException(Exception):
    pass


class Architect(object):
    def __init__(self, architecture):
        self.__architecture = architecture
        self.__indent = "    "

    def __identify(self):
        if self.__architecture.lower() == "mvc":
            self.__create_mvc_architecture()

        else:
            self.__create_simple_app()

    def __create_mvc_architecture(self):
        self.__create_mvc_app()

    def __create_simple_app(self):
        self.__create_config_file("config.py")
        self.__create_simple_run()

    def __create_config_file(self, filename):
        if self.__architecture == "mvc":
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                random_bytes = os.urandom(64)
                token = base64.b64encode(random_bytes).decode('utf-8')
                file.write("DEBUG=True\n")
                file.write("SECRET_KEY=" + '"' + token + '"\n')
                file.write('SERVER_NAME="127.0.0.1:5000"\n')
            except:
                raise ArchitectException("Error while creating config.py")

    def __create_init_py(self, filename):
        # Create init file
        with open(filename, "w+") as file:
            try:
                file.write("from flask import Flask, render_template\n\n")
                file.write("app = Flask(__name__)\n")
                file.write('app.config.from_pyfile("config.py")\n\n\n')
                file.write('from project import controller\n')
            except:
                raise ArchitectException("Error while creating __init__.py")

    def __create_contoller_py(self, filename):
        # Create simple controller
        with open(filename, "w+") as file:
            try:
                file.write('from project import app, render_template\n\n')
                file.write('@app.route("/")\n')
                file.write("def index():\n")
                file.write(self.__indent +
                           'return render_template("index.html")\n\n')
            except:
                raise ArchitectException("Error while creating controller.py")

    def __create_run_py(self, filename):
        with open(filename, "w+") as file:
            try:
                file.write("from project import app\n\n")
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise ArchitectException("Error while creating run.py")

    def __create_model_py(self, filename):
        with open(filename, "w+") as file:
            try:
                file.write('# Your models here.\n')
            except:
                raise ArchitectException("Error while creating model.py")

    def __create_style(self, filename_css, filename_js):
        # Create static/css
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                file.write('\n')
            except:
                raise ArchitectException("Error while creating static/css")

        # Create static/js
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                file.write('\n')
            except:
                raise ArchitectException("Error while creating static/js")

    def __create_templates(self, filename):
        # Create a simple template
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            file.write('<h1>Flask is fun.</h1>')

    def __create_mvc_app(self):
        # Create config file
        self.__create_config_file(filename="project/config.py")
        self.__create_run_py(filename="run.py")
        self.__create_init_py(filename="project/__init__.py")
        self.__create_contoller_py(filename="project/controller.py")
        self.__create_model_py(filename="project/models.py")
        self.__create_style(filename_css="project/static/css/style.css",
                            filename_js="project/static/js/script.js")
        self.__create_templates(filename="project/templates/index.html")

    def __create_simple_run(self):
        with open("run.py", "w+") as file:
            try:
                file.write("from flask import Flask\n\n")
                file.write("app = Flask(__name__)\n")
                file.write('app.config.from_pyfile("config.py")\n\n\n')
                file.write('@app.route("/")\n')
                file.write("def index():\n")
                file.write(self.__indent +
                           'return "<h1>Hello World!</h1>"\n\n')
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise ArchitectException("Error while creating run.py")

    def build(self):
        self.__identify()
