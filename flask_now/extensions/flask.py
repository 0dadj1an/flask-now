from .base import BaseSimpleExtension, BaseMvcExtension


class FlaskSimpleExtension(BaseSimpleExtension):
    def __init__(self):
        super().__init__()

    def run_imports(self):
        write_this = ["from flask import Flask \n"]
        super().writer(self.run_path, "a+", write_this)

    def run_variables(self):
        write_this = ["flask_app = Flask(__name__)"]
        super().writer(self.run_path, "a+", write_this)

    def run_methods(self):
        write_this = ['flask_app.config.from_pyfile("config.py")\n\n',
                      '@flask_app.route("/")',
                      'def index():',
                      '{}return "<h1>Hello World!</h1>"'.format(self.indent),
                      'if __name__ == "__main__":',
                      '{}flask_app.run()'.format(self.indent)]
        super().writer(self.run_path, "a+", write_this)


class FlaskMvcExtension(BaseMvcExtension):
    def __init__(self):
        super().__init__()

    def model_imports(self):
        write_this = ['# Your models here.']
        super().writer(self.model_path, "a+", write_this)

    def model_variables(self):
        pass

    def model_methods(self):
        pass

    def controller_imports(self):
        write_this = ['from project import flask_app, render_template\n']
        super().writer(self.controller_path, "a+", write_this)

    def controller_methods(self):
        write_this = ['@flask_app.route("/")',
                      'def index():',
                      '{}return render_template("index.html")\n'.format(self.indent)]
        super().writer(self.controller_path, "a+", write_this)

    def controller_variables(self):
        pass

    def default_css(self):
        super().writer(self.static_css_path, "a+")

    def default_js(self):
        super().writer(self.static_js_path, "a+")

    def index_html(self):
        write_this = ['<h1>Flask is fun!</h1>']
        super().writer(self.templates_index_path, "a+", write_this)

    def init_imports(self):
        write_this = ['from flask import Flask, render_template\n']
        super().writer(self.init_path, "a+", write_this)

    def init_variables(self):
        write_this = ['flask_app = Flask(__name__)',
                      'flask_app.config.from_pyfile("config.py")\n',
                      'from project import controller']
        super().writer(self.init_path, "a+", write_this)

    def run_imports(self):
        write_this = ['from project import flask_app\n']
        super().writer(self.run_path, "a+", write_this)

    def run_variables(self):
        write_this = ['if __name__ == "__main__":',
                      '{}flask_app.run()'.format(self.indent)]
        super().writer(self.run_path, "a+", write_this)

    def run_methods(self):
        pass

    def init_methods(self):
        pass
