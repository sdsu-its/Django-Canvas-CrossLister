from setuptools import setup

setup(
    name='canvasCrosslister',
    url='https://github.com/sdsu-its/Canvas-CrossLister',
    author='Mirza Ishraq Yeahia',
    author_email='myeahia@sdsu.edu',
    packages=['canvasCrosslister'],
    install_requires=['setuptools','canvasapi'],
    version='0.1',
    license='MIT',
    description='An application to combine multiple Canvas course.',
)
