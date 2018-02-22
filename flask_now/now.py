from .parser import Parser
from .architect import Architect
from .validator import Validator
from .supplier import Supplier

def build():
    parser = Parser()
    main_file, architecture, package_list = parser.parse()
    validator = Validator(package_list)
    if validator.validate(main_file=main_file, architecture=architecture):
        supplier = Supplier(package_list)
        if supplier.supply():
            architect = Architect(architecture, package_list)
            architect.build()


def main():
    build()
