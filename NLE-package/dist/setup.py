from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Neon light effect'
LONG_DESCRIPTION = 'Neon light effect using pyhton and photoshop'

setup(
    name="NeonLightEffect",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Avlis",
    author_email="gonca2000100@gmail.com",
    license='MIT',
    packages=find_packages(include=['NeonLightEffect']),
    keywords='Neon Light',
    install_requires=['Numpy','opencv-python','colour','comtypes'],
)