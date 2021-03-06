import codecs
try:
    from setuptools import setup, find_packages
    extra_setup = dict(
        install_requires=['requests'],
    )
except ImportError:
    from distutils.core import setup
    extra_setup = {}

setup(
    name='readthedocs-sphinx-ext',
    version='0.5.16',
    author='Read the Docs, Inc',
    author_email='dev@readthedocs.com',
    url='http://github.com/rtfd/readthedocs-sphinx-ext',
    license='BSD',
    description='Sphinx extension for Read the Docs overrides',
    package_dir={'': '.'},
    packages=find_packages('.'),
    long_description=codecs.open("README.rst", "r", "utf-8").read(),
    # trying to add files...
    include_package_data=True,
    package_data={
        '': ['_static/*.js', '_static/*.js_t', '_static/*.css', '_templates/*.tmpl'],
    },
    **extra_setup
)
