from distutils.core import setup

setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/basil-chatha/titanic_datascience',
    author='Basil Chatha',  # Substitute your name
    author_email='basil.chatha8@gmail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
    install_requires=[
        'pypandoc>=1.4',
        'pytest>=4.3.1',
        'pytest-runner>=4.4',
        'click>=7.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
)
