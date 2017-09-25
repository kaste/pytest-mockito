from setuptools import setup

setup(
    name="pytest-mockito",
    version='0.0.4',
    description='Base fixtures for mockito',
    long_description=open('README.rst').read(),
    license='MIT',
    author='herr kaste',
    author_email='herr.kaste@gmail.com',
    url='https://github.com/kaste/pytest-mockito',
    platforms=['linux', 'osx', 'win32'],
    packages=['pytest_mockito'],
    entry_points={'pytest11': ['mockito = pytest_mockito.plugin'], },
    zip_safe=False,
    install_requires=['pytest>=3', 'mockito>=1.0.6'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ],
)
