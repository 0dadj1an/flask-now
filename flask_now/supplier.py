import subprocess


class Supplier(object):
    def __init__(self, package_list):
        self.__package_list = package_list
        self.__process_result = False

    def create_requirements(self):
        try:
            with open("requirements.txt", "a") as file:
                file.write("flask\n")
                for package in self.__package_list:
                    if package == "frozen":
                        file.write("frozen-flask \n")
                    else:
                        file.write("flask-" + package + "\n")

            self.__package_list.append("flask")
            self.__process_result = True
        except:
            self.__process_result = False
            raise ParserException(
                "Cannot create or open: requirements.txt file")

    def install_requirements(self):
        if len(self.__package_list) > 0:
            process = subprocess.Popen(
                "pip install -r requirements.txt", shell=True, stdout=subprocess.PIPE)
            print("Installing requirements...")
            process.wait()
            if process.returncode == 0:
                self.__process_result = True
                process = subprocess.Popen(
                    "pip freeze > requirements.txt", shell=True, stdout=subprocess.PIPE)
                print("Freezing requirements...")
                process.wait()
                if process.returncode == 0:
                    self.__process_result = True
                else:
                    print(
                        "An error occured while freezing requirements\nError:\n", process.stdout)
                    print(
                        "You can manually freeze installed requirements by using following command: 'pip freeze > requirements.txt'")
            else:
                self.__process_result = False
                print(
                    "An error occured while installing requirements\nError:\n", process.stdout)
        else:
            self.__process_result = True

    def supply(self):
        self.create_requirements()
        self.install_requirements()

        return self.__process_result
