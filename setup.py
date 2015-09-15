from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='jts_datashape',
    version=__version__,
    description="A library to convert JSON Table Schema <--> DataShape",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='schema jsontableschema jts data datashape odo',
    author='Femto Trader',
    author_email='femto.trader@gmail.com',
    url='http://github.com/okfn/jts-datashape',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=['datashape'],
    tests_require=[
        'nose',
        'coverage',
        'wheel'
    ]
)
