'log_helper.py'

from datetime import datetime
import json
import csvmapper
from locustic_config import LocusticConfig

class LogHelper:
    'Log helper is responsible for parsing the Locust CSV output to JSON format.'
    locust_csv_fields = ('Method', 'Name', '# requests', '# failures', 'Median response time',
                         'Average response time', 'Min response time', 'Max response time',
                         'Average Content Size', 'Requests/s')
    locust_csv_file_path = ''

    def __init__(self):
        self.locust_csv_file_path = LocusticConfig.LOCUST_CSV_LOG_FILE_PATH
        if self.locust_csv_file_path is '':
            raise Exception('LOCUST_CSV_LOG_FILE_PATH cannot be empty!')

    def parse_log_to_json(self, log_path):
        'Parse CSV log file and return JSON string.'
        parser = csvmapper.CSVParser(log_path,
                                     csvmapper.mapper.FieldMapper(self.locust_csv_fields),
                                     hasHeader=True)
        json_converter = csvmapper.converter.JSONConverter(parser)
        print(json_converter)
        return json_converter.doConvert(pretty=False)

    def prepare_elastic_insert_query(self, log):
        'Map json result to elastic insert query.'
	
	json_result = ''

	for json_log in json.loads(log):
	     json_body = {
                "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "Method": json_log['Method'],
                "Name": json_log['Name'],
                "Requests": json_log['# requests'],
                "Failures": json_log['# failures'],
                "Median response time": json_log['Median response time'],
                "Average response time": json_log['Average response time'],
                "Min response time": json_log['Min response time'],
                "Max response time": json_log['Max response time'],
                "Average Content Size": json_log['Average Content Size'],
                "Requests/Sec": json_log['Requests/s'],
             }
	     
 	     json_result = json_body	

		

        print(json_result)
        return json_body
