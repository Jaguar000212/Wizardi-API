import os
from setuptools import setup

requires = (
        "flask",
        "requests",
        "openai"
        )

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Wizardi API",
    version = "1.0.0",
    author = "Jaguar000212",
    author_email = "jaguar000212@gmail.com",
    description = ("Api for Wizardi, the discord bot by Jaguar000212"),
    license = "BSD",
    keywords = "wizardi-api",
    url = "http://api.jaguar000212.tech/",
    packages=['api','templates'],
    # namespace_packages = ['package_name'],
    install_requires=requires,
    # long_description=read('README.md'),
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)