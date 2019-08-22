from setuptools import setup

setup(name='pythonCalculator',
      version='1.0',
      description='console calculator',
      author='Oleg Slutski',
      author_email='st.alehs@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['calculator'],
      entry_points = {
        #'console_scripts': ['oleg=calculator.main:af'],
        'console_scripts': ['pycalc=calculator.main:main'],
        },
     )
     
