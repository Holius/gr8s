from setuptools import setup, find_packages

setup(
    name='gr8s',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[],
)
