# Python virtual environment

* A Python virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
* It allows you to work on a specific project without affecting other projects or the system level Python installation.

## virtual environment

* install virtualenv package using command `pip3 install --python virtualenv`
* create virtualenv using command `virtualenv myenv`
* activate environment using command `source myenv/bin/activate`
* verify python version using `python --version`

## install dependent packages using pip

* **requests** : `pip install requests`
* **flask**: `pip install flask`
* **mysql-connector-python**: `pip install mysql-connector-python`

## deactivate virtual env

* use command `deactivate` to stop using the virtualenv.

### Reference: https://virtualenv.pypa.io/en/latest/
