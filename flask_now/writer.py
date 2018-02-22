import os
import json
import base64


class WriterException(Exception):
    pass


class Writer(object):

    def __init__(self):
        self.__build_now = {}
        self.__indent = "    "

    def create_run_py(self, filename):
        with open(filename, "w+") as file:
            try:
                file.write("from project import app\n\n")
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise WriterException("Error while creating run.py")

    def create_simple_run(self):
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
                raise WriterException("Error while creating run.py")

    def create_build_now(self, architecture, package_list):
        self.__build_now["pattern"] = architecture
        self.__build_now["extensions"] = package_list
        with open("build.now", "w+") as file:
            file.write(str(self.__build_now))

    def create_config_file_simple(self, filename):
        self.__config_writer(filename)

    def create_config_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.__config_writer(filename)

    def __config_writer(self, filename):
        with open(filename, "w+") as file:
            try:
                random_bytes = os.urandom(64)
                token = base64.b64encode(random_bytes).decode('utf-8')
                file.write("DEBUG=True\n")
                file.write("SECRET_KEY=" + '"' + token + '"\n')
                file.write('SERVER_NAME="127.0.0.1:5000"\n')
            except:
                raise WriterException("Error while creating config.py")

    def create_init_py(self, filename):
        # Create init file
        with open(filename, "w+") as file:
            try:
                file.write("from flask import Flask, render_template\n\n")
                file.write("app = Flask(__name__)\n")
                file.write('app.config.from_pyfile("config.py")\n\n\n')
                file.write('from project import controller\n')
            except:
                raise WriterException("Error while creating __init__.py")

    def create_contoller_py(self, filename):
        # Create simple controller
        with open(filename, "w+") as file:
            try:
                file.write('from project import app, render_template\n\n')
                file.write('@app.route("/")\n')
                file.write("def index():\n")
                file.write(self.__indent +
                           'return render_template("index.html")\n\n')
            except:
                raise WriterException("Error while creating controller.py")

    def create_model_py(self, filename):
        with open(filename, "w+") as file:
            try:
                file.write('# Your models here.\n')
            except:
                raise WriterException("Error while creating model.py")

    def create_style(self, filename_css, filename_js):
        # Create static/css
        os.makedirs(os.path.dirname(filename_css), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                file.write('\n')
            except:
                raise WriterException("Error while creating static/css")

        # Create static/js
        os.makedirs(os.path.dirname(filename_js), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                file.write('\n')
            except:
                raise WriterException("Error while creating static/js")

    def create_templates(self, filename):
        # Create a simple template
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                file.write('<h1>Flask is fun.</h1>')
            except:
                raise WriterException(
                    "Error while creating templates/index.html")
