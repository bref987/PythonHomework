from setuptools import setup

setup(name='calculator',
        version='1.6',
        description='pure line-command calculator',
        author='Aleh Slutski',
        author_email='st.alehs@gmail.com',
        packages=['calculator'],
        entry_points={
        'console_scripts': ['pycalc=calculator.main:main'],
        }
    )
     