import pkg_resources
import subprocess
import sys

def install_missing_requirements(requirements_file='requirements.txt'):
    with open(requirements_file) as f:
        required = f.read().splitlines()
    try:
        pkg_resources.require(required)
    except pkg_resources.DistributionNotFound:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
