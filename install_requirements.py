import subprocess

install_requirements = 'pip install --upgrade -r requirements.txt'

def req_install():
	subprocess.call(install_requirements, shell=True)

if __name__ == '__main__':
	req_install()