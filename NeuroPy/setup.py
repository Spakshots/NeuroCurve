import importlib.util
import subprocess
import sys

def is_package_installed(pkg_name):
    return importlib.util.find_spec(pkg_name) is not None

def install_requirements(requirements_file='requirements.txt'):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
