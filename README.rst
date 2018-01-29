locustic
========

Locustic is a simple Python scheduled worker which collects Locust load testing data and send to Elastic.


Usage
-----

Just configure to LocusticConfig class

.. code-block:: python

    class LocusticConfig:
        'Locustic configuration'
        ELASTIC_HOST = ''
        ELASTIC_PORT = ''
        ELASTIC_USER_NAME = ''
        ELASTIC_PASSWORD = ''
        ELASTIC_DATABASE = ''
        DELAY_IN_SEC = 5
        LOCUST_CSV_LOG_FILE_PATH = ''
