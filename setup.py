from setuptools import find_packages, setup
setup(
    name='pyprediktoredgeclient',
    packages=find_packages(include=['pyprediktoredgeclient']),
    setup_requires=[
        "pythonnet==3.0.0a2"
        ],
    package_data={
        "": ["dlls/*.dll", "app.runtimeconfig.json"],
    },
    version='0.9.5',
    description='A Python library to talk to Prediktor APIS/EDGE',
    author='Prediktor',
    license='MIT'
)