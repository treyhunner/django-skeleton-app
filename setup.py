from setuptools import setup, find_packages
from packagename import __version__


setup(
    name="package-name-as-shown-on-pypi",
    version=__version__,
    author="Your Name Here",
    author_email="youremail@example.com",
    url="https://github.com/yourusername/package-name-as-shown-on-pypi",
    description="Short package description",
    long_description='\n\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.4.2'],
    tests_require=['mock'],
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
)
