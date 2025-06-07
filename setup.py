from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirments = []
    with open (file_path) as file_obj:
        requirment = file_obj.readlines()
        requirment= [req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments

setup(
name = "mlproject",
version = '0.0.1',
auther = 'Shaurya',
auther_email = 'shaurya6037@gmail.com',
packages = find_packages(),
install_requires = ['pandas','numpy','seaborn']

)