from setuptools import setup, find_packages

version = '0.1.dev0'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read()
    ])

setup(
    name='rediscounter',
    version=version,
    description="Counters in Redis",
    long_description=long_description,
    # Get strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='',
    author='Maurits van Rees',
    author_email='m.van.rees@zestsoftware.nl',
    url='',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
          'PasteDeploy',
          'WSGIFilter',
          'redis',
          ],
    entry_points={
        'paste.filter_app_factory': [
            'filter = rediscounter.filter:CounterFilter.paste_deploy_middleware',
            ],
        'paste.app_factory': [
            'app = rediscounter.app:app_factory',
            ],
            },
    )
