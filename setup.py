from setuptools import setup, find_packages

setup(
        name='pypm',
        version='0.0.1',
        description='Powermanagement Logger and lala',
        url='github',
        author='Alexander Geissler',
        author_email='alexander.geissler@izt-labs.de',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Hardware',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            ],
        keywords='development powermanagement',
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=['numpy',
                          'scipy',
                          'matplotlib'],
        extras_require={
            'dev' : ['check-manifest'],
            'test' : ['coverage'],
            },
        entry_points={
            'console_scripts': [
                'pm=pm:main',
                ],
            },
        )
