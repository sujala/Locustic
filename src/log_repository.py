'log_repository.py'

from elasticsearch import Elasticsearch
from locustic_config import LocusticConfig
from log_helper import LogHelper

class LogRepository:
    'Log repository.'
    elastic_client = None

    def __init__(self):
        locustic_config = LocusticConfig()
        self.elastic_client = Elasticsearch()
                                         
    def add_log(self, log):
        'Add a log to Elastic'
        mapped_log = LogHelper().prepare_elastic_insert_query(log)
	res = self.elastic_client.index(index="index_name", doc_type="doc_type", body=mapped_log)
	print(res)
