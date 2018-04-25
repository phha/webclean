from setuptools import find_packages, setup

setup(
    name='webclean',
    version='0.0.2',
    author='Philipp Hack',
    author_email='philipp.hack@gmail.com',
    url='http://github.com/phha/click_config_file',
    description='Clean up web articles',
    license='MIT',
    py_modules=['webclean'],
    install_requires=[
        'click',
        'newspaper3k',
    ],
    entry_points='''
        [console_scripts]
        webclean=webclean:webclean
    ''',
)
