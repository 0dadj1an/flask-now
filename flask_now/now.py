from .parser import Parser
from .architect import Architect
from .supplier import Supplier

def build():
    parser = Parser()
    architecture, package_list = parser.parse()
    supplier = Supplier(package_list)
    if supplier.supply():
        architect = Architect(architecture, package_list)
        architect.build()

def main():
    build()
