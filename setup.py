from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='imio.wsresponse.core',
    version=version,
    description="",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='',
    author_email='',
    url='https://github.com/IMIO/imio.wsresponse.core',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['imio', 'imio.wsresponse'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'collective.zamqp',
        'five.grok',
        'imio.amqp',
        'imio.dataexchange.core',
        'plone.api',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    """,
)
