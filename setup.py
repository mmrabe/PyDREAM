from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pydream',
      version='1.0',
      description='A Python implementation of the MT-DREAM(ZS) algorithm from Laloy and Vrugt 2012, implemented by Erin Shockley, modified to switch multiprocessing and likelihood reevaluation on or off.',
      long_description=readme(),
      classifiers=['Programming Language :: Python :: 2'],
      url='https://github.com/LoLab-VU/PyDREAM',
      author='Maximilian M. Rabe',
      author_email='maximilian.rabe@uni-potsdam.de',
      packages=['pydream'],
      install_requires=['numpy', 'scipy', 'multiprocess'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True
      )