from typing import List
from setuptools import find_packages, setup

def get_requirements(file_path: str) -> List[str]:
    # Function to read requirements from a file and clean them up
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file if line.strip() and not line.strip().startswith('-e')]
    return requirements

setup(
    name='ML_PROJECT',  # Adjusted to use underscores instead of spaces
    version='0.0.1',
    author='Jaya Sri Raman',
    author_email='jayasriraman2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
