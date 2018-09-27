.. 

nerdypython
======================

Quickstart
----------

To bootstrap the project::

    virtualenv nerdypython
    source nerdypython/bin/activate
    cd path/to/nerdypython/repository
    pip install -r requirements.pip
    pip install -e .
    cp nerdypython/settings/local.py.example nerdypython/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
