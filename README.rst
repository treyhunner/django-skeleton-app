django-skeleton-app
===================

This repository contains tips for creating a new open source Django app.

This repository should not be copied verbatim.  Instead start building your
repository from the ground up, using the files here as a guideline.  Remember
that you can always add more to your repository later.

Descriptions of the Files
-------------------------

README.rst
~~~~~~~~~~

The README file is displayed on Github and should be used to generate the long description for the package which is displayed on PyPI.

CHANGES.rst
~~~~~~~~~~~

The CHANGES file will record version numbers and dates and the changes between each version.

LICENSE
~~~~~~~

If you don’t specify an open source license for your code, all rights will be reserved by default and no one can legally use your code without explicit permission.

setup.py
~~~~~~~~

The setup.py file is used to install the Python package, upload it to PyPI, and is generally used for running commands related to your Python project.

Some things that must be changed in the example file:

- PyPI package name (often hyphenated)
- Python package name
- Author name and email
- The short description
- The project URL
- Installation requirements (remove if there are none)
- Test requirements (remove if there are none)
- Classifier troves (Python versions, license, and environment)
- MANIFEST.in

The MANIFEST file specifies the files that should be included when creating and installing a Python package. The example MANIFEST.in file includes all reStructuredText files. This will ensure the README and CHANGES files so the setup.py file works correctly. The rst files in the docs directory will also be included.

Test files
~~~~~~~~~~

You need test files. Even if you have no tests for your package initially you at least need to create the files that will store the tests. This will make creating tests much easier once you do want to add some.

The tests files you should create:

- runtests.py: stores a function that runs your tests. Change the setup.py file as needed to reflect the name of this file and the function it contains.
- tox.ini: notes your tox settings as well as your pep8/flake8 settings. Tox is used to run your tests against multiple Python environments.
- .coveragerc: stores your settings for coverage.py, the test coverage analyzer
- .travis.yml: configuration file for Travis CI (runs your tests each time you push to your git repository)

Empty Package Files
~~~~~~~~~~~~~~~~~~~

- packagename/init.py: This should contain the __version__ variable
- packagename/tests/init.py: This should be empty
- packagename/tests/models.py: A models.py file is needed for Django apps
- packagename/tests/tests.py: This will contain the tests eventually

.editorconfig
~~~~~~~~~~~~~

PEP8 checkers usually handle enforcing Python file formatting, but I like including an EditorConfig file to specify the indentation I use for my INI and YAML files.

AUTHORS.rst
~~~~~~~~~~~

You may be the only author now, but eventually someone may discover your project and submit a pull request. The least you could do is honor that person with a listing in the authors file.

.gitignore
~~~~~~~~~~

This is a requirement for nearly all Git repositories.

CONTRIBUTING.rst
~~~~~~~~~~~~~~~~

This file should explain to new contributors the steps they should take while submitting an issue or pull request. Github shows a link to this file when creating a new issue or pull request on your repository.

Sphinx Documentation
~~~~~~~~~~~~~~~~~~~~

Incomplete documentation is usually better than missing documentation. Use Sphinx to create a skeleton documentation directory so it will be easy to add documentation later.

Makefile
~~~~~~~~

It’s nice to have shortcut commands for installing tox and coverage, building documentation, and running tests while generating coverage reports.
