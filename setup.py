from setuptools import setup

setup(
    name='myapp',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
