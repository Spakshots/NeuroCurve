import importlib.util
import subprocess
import sys

'''Checking if a package is installed and available in sys.path'''
def is_package_installed(pkg_name):
    name_map = {
        "scikit-learn": "sklearn"
    }
    import_name = 'sklearn' if pkg_name == 'scikit-learn' else name_map.get(pkg_name, pkg_name)
    found = importlib.util.find_spec(import_name) is not None
    #print(f"Checking: {pkg_name} -> import '{import_name}' => {True if found else False}")
    return found

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

def loadup(requirements_file='requirements.txt'):
    required_packages = get_required_packages(requirements_file)
    missing = []
    for pkg in required_packages:
        if(is_package_installed(pkg) != True):
            missing.append(pkg)
    if missing:
        print(f"Missing packages detected: {missing}")
        print("Installing missing packages...")
        install_requirements(requirements_file)
    else:
        print("All required packages are already installed. 👍")
