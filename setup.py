from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""
    try:
        with open('requirements.txt', 'r') as file:
            requirements = file.readlines()
        return [req.strip() for req in requirements if req.strip() and not req.startswith('#') and not req.startswith('-e')]

    except FileNotFoundError:
        print(f"Error: The file requirements.txt was not found.")
        return []

"""print("Reading requirements from requirements.txt...")
requirements = get_requirements()
print(f"Requirements found: {requirements}")"""

setup(
    name='Network_Security',
    version='0.0.1',
    packages=find_packages(),
    author='DEEPAK MITTAL',
    author_email='dmittal9925.dm@gmail.com', 
    install_requires=get_requirements(),
)
