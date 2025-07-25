# OpenFisca France Entreprises


This package models the tax and subsidy system for French firms on the subject of carbon tax.

- The rates are in the `parameters` folder.
- The formulas are in the `variables` folder.
- This country package comes also with *reforms* in the `reforms` folder. This is optional: your country may exist without defining any reform.
    - In this country, there is [a reform project](./openfisca_france_entreprises/reforms/modify_social_security_taxation.py) aiming to modify the social security taxation, deleting the first bracket, raising the intermediary ones and adding a new bracket with a higher tax rate of `40 %` for people earning more than `40000`. This reform project would apply starting from `2017-01-01`.

The files that are outside from the `openfisca_france_entreprises` folder are used to set up the development environment.

## Packaging your Country Package for Distribution

Country packages are Python distributions. You can choose to distribute your package automatically via the predefined continuous deployment system on GitHub Actions, or manually.

### Automatic continuous deployment on GitHub

This repository is configured with a continuous deployment system to automate the distribution of your package via `pip`.

#### Setting up continuous deployment

To activate the continuous deployment:

1. Create an account on [PyPI](https://pypi.org/) if you don't already have one.
2. Generate a token in your PyPI account. This token will allow GitHub Actions to securely upload new versions of your package to PyPI.
3. Add this token to your GitHub repository's secrets under the name `PYPI_TOKEN`.

Once set up, changes to the `main` branch will trigger an automated workflow to build and publish your package to PyPI, making it available for `pip` installation.

### Manual distribution

If you prefer to manually manage the release and distribution of your package, follow the guidelines provided by the [Python Packaging Authority](https://python-packaging-user-guide.readthedocs.io/tutorials/distributing-packages/#packaging-your-project).

This involves detailed steps on preparing your package, creating distribution files, and uploading them to PyPI.


## Install Instructions for Users and Contributors

This package requires [Python 3.9](https://www.python.org/downloads/release/python-390/). More recent versions should work, but are not tested.

All platforms that can execute Python are supported, which includes GNU/Linux, macOS and Microsoft Windows.

### Setting-up a Virtual Environment with venv

In order to limit dependencies conflicts, we recommend using a [virtual environment](https://www.python.org/dev/peps/pep-0405/) with [venv](https://docs.python.org/3/library/venv.html).

- A [venv](https://docs.python.org/3/library/venv.html) is a project specific environment created to suit the needs of the project you are working on.

To create a virtual environment, launch a terminal on your computer, `cd` into your directory of choice and follow the instructions below. Notice : Do NOT choose any of the directories that is part of this project as the destination! Reversely, do NOT install the openfisca country package directly in the folder for the virtual enviornment. They should be parallel of each other.

```sh
python -m venv .venv # create a new virtual environment in the “.venv” folder, which will contain all dependencies
source .venv/bin/activate # activate the venv
```

You can now operate in the venv you just created.

You can deactivate that venv at any time with `deactivate`.

:tada: You are now ready to install this OpenFisca Country Package!

Two install procedures are available. Pick procedure A or B below depending on how you plan to use this Country Package.

### A. Minimal Installation (Pip Install)

Follow this installation if you wish to:
- run calculations on a large population;
- create tax & benefits simulations;
- write an extension to this legislation (e.g. city specific tax & benefits);
- serve your Country Package with the OpenFisca Web API.

For more advanced uses, head to the [Advanced Installation](#advanced-installation-git-clone).

#### Install this Country Package with Pip Install

Inside your venv, check the prerequisites:

```sh
python --version  # should print "Python 3.9.xx".
```

```sh
pip --version  # should print at least 9.0.
# if not, run "pip install --upgrade pip"
```
Install the Country Package:

```sh
pip install openfisca_france_entreprises
```

:warning: Please beware that installing the Country Package with `pip` is dependent on its maintainers publishing said package.

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To learn how to use OpenFisca, follow our [tutorials](https://openfisca.org/doc/).
- To serve this Country Package, serve the [OpenFisca Web API](#serve-your-country-package-with-the-openFisca-web-api).

Depending on what you want to do with OpenFisca, you may want to install yet other packages in your venv:
- To install extensions or write on top of this Country Package, head to the [Extensions documentation](https://openfisca.org/doc/contribute/extensions.html).
- To plot simulation results, try [matplotlib](http://matplotlib.org/).
- To manage data, check out [pandas](http://pandas.pydata.org/).

### B. Advanced Installation (Git Clone)

Follow this tutorial if you wish to:
- create or change this Country Package's legislation;
- contribute to the source code.

#### Clone this Country Package with Git

First, make sure [Git](https://www.git-scm.com/) is installed on your machine.

Set your working directory to the location where you want this OpenFisca Country Package cloned.

Inside your venv, check the prerequisites:

```sh
python --version  # should print "Python 3.9.xx".
```

Clone this Country Package on your machine:

```sh
git clone git://github.com/pzuldp/openfisca-france-entreprises.git
cd openfisca-france-entreprises.git
pip install --upgrade pip build twine
pip install --editable .[dev] --upgrade
```

You can make sure that everything is working by running the provided tests with `make test`.

> [Learn more about tests](https://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To write new legislation, read the [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html) section to know how to write legislation.
- To contribute to the code, read our [Contribution Guidebook](https://openfisca.org/doc/contribute/index.html).

## Serve this Country Package with the OpenFisca Web API

If you are considering building a web application, you can use the packaged OpenFisca Web API with your Country Package.

To serve the Openfisca Web API locally, run:

```sh
openfisca serve --port 5000 --country-package openfisca_france_entreprises
```

Or use the quick-start Make command:

```
make serve-local
```

To read more about the `openfisca serve` command, check out its [documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API specification](https://www.openapis.org/) of your API.

:tada: This OpenFisca Country Package is now served by the OpenFisca Web API! To learn more, go to the [OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).

You can test your new Web API by sending it example JSON data located in the `situation_examples` folder.

```sh
curl -X POST -H "Content-Type: application/json" \
  -d @./openfisca_france_entreprises/situation_examples/couple.json \
  http://localhost:5000/calculate
```
