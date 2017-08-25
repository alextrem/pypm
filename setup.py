"""
setup file for this package
"""
import versioneer
from setuptools import setup, find_packages

cmdclass = versioneer.get_cmdclass()

setup(
        name='pypm',
        version=versioneer.get_version(),
        description='Powermanagement command creator',
        url='http://www.github.com/alextrem/pypm',
        author='Alexander Geissler',
        author_email='alextrem@web.de',
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
        cmdclass=cmdclass,
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=['numpy',
                          'scipy',
                          'matplotlib'],
        extras_require={
            'dev': ['check-manifest'],
            'test': ['coverage'],
            },
        entry_points={
            'console_scripts': [
                'pm=pm:main',
                ],
            },
        )
