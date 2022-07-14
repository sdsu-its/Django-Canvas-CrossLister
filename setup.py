from setuptools import setup

setup(
    name='Canvas Crosslister',
    url='https://github.com/sdsu-its/Canvas-CrossLister',
    author='Mirza Ishraq Yeahia',
    author_email='myeahia@sdsu.edu',
    packages=['application'],
    install_requires=['setuptools','canvasapi','Django==4.0.6'],
    version='0.1',
    license='MIT',
    description='An application to combine multiple Canvas course.',
)
