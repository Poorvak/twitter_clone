import subprocess
import os

google_app_server_command = 'python dev_appserver.py --port={port_number} code_src'
def run_server(port_number=None, datastore_file_name=None):
	if not port_number:
		port_number = 8080
	#datastore_path = file(datastore_path, 'r+') if os.path.exists(datastore_path) else file('tmp/app_datastore', 'w')

	subprocess.call(google_app_server_command.format(port_number=port_number), shell=True)

if __name__ == '__main__':
	run_server(port_number=8080)