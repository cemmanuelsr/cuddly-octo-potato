from setuptools import setup

setup(
    name='dev_aberto_caioesr',
    version='0.1',
    packages=['dev_aberto'],
    author='Caio Emmanuel',
    author_email='caioemmanuelsr@gmail.com',
    install_requires=['requests'],
    scripts=['scripts/hello.py']
)
