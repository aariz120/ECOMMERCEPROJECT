from setuptools import find_packages, setup

setup(
    name= "ECOMMERCEPROJECT",
    version= '0.0.0',
    author= "Aariz Mobin",
    author_email="aariz120@gmail.com",
    packages= find_packages(),
    install_requires=['langchain-astradb','langchain','langchain-openai','datasets','pypdf','python-dotenv','flask']
    
)