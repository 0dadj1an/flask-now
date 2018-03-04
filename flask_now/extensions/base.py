import os


class BaseExtension(object):
    def __init__(self):
        self.indent = "    "
        self.run_path = "run.py"

    def config(self):
        pass

    def run_imports(self):
        pass

    def run_variables(self):
        pass

    def run_methods(self):
        pass

    def writer(self,file,mode, write_this=[]):
        with open(file, mode) as writing_to:
            try:
                for word in write_this:
                    writing_to.write(word + "\n")
            except FileNotFoundError:
                raise Exception("Error while creating {}".format(file))


class BaseMvcExtension(BaseExtension):
    def __init__(self):
        super().__init__()
        self.create_folders()
        self.config_path = "project/config.py"
        self.init_path = "project/__init__.py"
        self.controller_path = "project/controller.py"
        self.static_css_path = "project/static/css/style.css"
        self.static_js_path = "project/static/js/script.js"
        self.templates_index_path = "project/templates/index.html"
        self.model_path = "project/model.py"

    def model_imports(self):
        pass

    def model_variables(self):
        pass

    def model_methods(self):
        pass

    def controller_imports(self):
        pass

    def controller_variables(self):
        pass

    def controller_methods(self):
        pass

    def default_css(self):
        pass

    def default_js(self):
        pass

    def index_html(self):
        pass

    def init_imports(self):
        pass

    def init_variables(self):
        pass

    def init_methods(self):
        pass

    def create_folders(self):
        os.makedirs("project/", exist_ok=True)
        os.makedirs("project/static/css/", exist_ok=True)
        os.makedirs("project/static/js/", exist_ok=True)
        os.makedirs("project/templates/", exist_ok=True)


class BaseSimpleExtension(BaseExtension):
    def __init__(self):
        super().__init__()
        self.config_path = "config.py"
