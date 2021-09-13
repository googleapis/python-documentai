Python Client for Cloud Document AI API
==================================================

|GA| |pypi| |versions|

`Cloud Document AI API`_: Service to parse structured information from unstructured or
semi-structured documents using state-of-the-art Google AI such as natural
language, computer vision, translation, and AutoML.

- `Client Library Documentation`_
- `Product Documentation`_

.. |GA| image:: https://img.shields.io/badge/support-ga-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-service-directory.svg
   :target: https://pypi.org/project/google-cloud-service-directory/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-documentai.svg
   :target: https://pypi.org/project/google-cloud-documentai/
.. _Cloud Document AI API: https://cloud.google.com/document-understanding/docs/
.. _Client Library Documentation: https://googleapis.dev/python/documentai/latest
.. _Product Documentation: https://cloud.google.com/document-understanding/docs/

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud Document AI API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud Document AI API.:  https://cloud.google.com/document-understanding/docs/
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-documentai


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-documentai

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Document AI API
   API to see other available methods on the client.
-  Read the `Cloud Document AI API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Document AI API Product documentation:  https://cloud.google.com/document-understanding/docs/
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst

Running tests
-------------

Prerequisites
~~~~~~~~~~~~~

1. `Install pyenv`_ for your platform

2. Install the latest versions of python version 3.6, 3.7, 3.8, and 3.9 via pyenv.

   .. code-block:: console

      pyenv install 3.9.${3_9_LATEST_PATCH}
      pyenv install 3.8.${3_8_LATEST_PATCH}
      pyenv install 3.7.${3_7_LATEST_PATCH}
      pyenv install 3.6.${3_6_LATEST_PATCH}

   For example:

   .. code-block:: console

      pyenv install 3.9.7
      pyenv install 3.8.12
      pyenv install 3.7.11
      pyenv install 3.6.14

.. _Install pyenv: https://github.com/pyenv/pyenv#installation

Setup virtual envionrment
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Change directories to the root of this repo

2. Create a 3.8 Python virtual enviornment via pyenv:

   .. code-block:: console

      pyenv virtualenv 3.8.${3_8_LATEST_PATCH} docai-venv

   For example:

   .. code-block:: console

      pyenv virtualenv 3.8.12 docai-venv

3. Acitivate the virtual enviornment and use Python versions 2.7, 3.6, 3.7, and 3.9:

   .. code-block:: console

      pyenv local docai-venv \
         3.9.${3_9_LATEST_PATCH} \
         3.8.${3_8_LATEST_PATCH} \
         3.7.${3_7_LATEST_PATCH} \
         3.6.${3_6_LATEST_PATCH}

   For example:

   .. code-block:: console

      pyenv local docai-venv 3.9.7 3.8.12 3.7.11 3.6.14

4. Install the required library dependencies and test dependencies in the virtual enviornment:

   .. code-block:: console

      pip install google-cloud-documentai nox

Running tests with nox
~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Nox is directory dependent. Nox will only run tests contained in the current directory
   and subdirectories. To ensure all tests are run, make sure to run Nox from the root of
   this repo.

Run all tests:

1. Change directory to the root of the repo

2. Run Nox:

   .. code-block:: console

      nox

Run system tests:

.. code-block:: console

   nox -s system

Run unit tests:

.. code-block:: console

   nox -s unit

Run tests for a specific version of Python:

.. code-block:: console

   nox -s py-3.8

Run documentation tests:

.. code-block:: console

    nox -s docs
