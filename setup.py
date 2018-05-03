"""
setup file for this package
"""
import sys
import versioneer
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='pypm',
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
      cmdclass={
          '': versioneer.get_cmdclass(),
          'test': PyTest
      },
      packages=find_packages(exclude=['docs', 'tests']),
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
      tests_require=['pytest',
                     'sphinx_rtd_theme', ],
      )
