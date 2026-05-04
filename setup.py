from setuptools import setup, find_packages

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.3',
        'Werkzeug==2.3.7',
    ],
)