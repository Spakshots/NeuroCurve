import importlib.util
import subprocess
import sys

'''Checking if a package is installed and available in sys.path'''
def is_package_installed(pkg_name):
    return importlib.util.find_spec(pkg_name) is not None

'''Installs packages listed in the given requirements.txt file using pip'''
def install_requirements(requirements_file='requirements.txt'):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])

'''Parses through the requirement.txt file and returns a list of packages required to run the code'''
def get_required_packages(requirements_file='requirements.txt'):
    with open(requirements_file) as f:
        packages = []
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                pkg = line.split('==')[0]
                packages.append(pkg)
        return packages