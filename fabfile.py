from fabric.api import *
from fabric.contrib.files import exists
from fabric.context_managers import cd,lcd

env.user = 'connor'
env.hosts = ['connorgoldberg.com']

domain = 'connorgoldberg.com'
subdom = 'www'

def push_site():
	local('cp _static/Resume.pdf .')
	local('jekyll build')
	local('rm Resume.pdf')
	local('zip -r _site _site')
	run('rm -f /var/www/%s/_site.zip' % (domain))
	run('rm -rf /var/www/%s/_site' % (domain))
	put('_site.zip', '/var/www/%s/_site.zip' % (domain))
	run('unzip /var/www/%s/_site.zip -d /var/www/%s' % (domain, domain))
	run('rm -rf /var/www/%s/%s' % (domain, subdom))
	run('mv /var/www/%s/_site /var/www/%s/%s' % (domain, domain, subdom))

def push():
	push_site()
	push_static()

#Pushes the entire _static folder to the static directory on the server
def push_static():
	local('zip -r _static _static')
	run('rm -rf /var/www/%s/_static.zip /var/www/%s/static' % (domain,domain))
	put('_static.zip', '/var/www/%s/_static.zip' % (domain))
	run('unzip /var/www/%s/_static.zip -d /var/www/%s' % (domain, domain))
	run('mv /var/www/%s/_static /var/www/%s/static' % (domain, domain))
	local('rm -rf _static.zip')

"""
Pushes a single file from the _static folder to the static directory on the server.
Syntax in command line:
$ fab push_file:<filename>
"""

def push_file(fileName):
	#sets working directories to the static directories

	with lcd('_static'), cd('/var/www/%s/static/' % domain):
		
		if exists('%s' % (fileName)):
			#Then the file already exists in the static directory on the server
			confirm = prompt('Warning: File: %s already exists. Do you wish to proceed? [y/n]: ' % fileName)
			if (confirm == 'y'):
				run('rm %s' % fileName)
			else: 
				print("Aborted by user.")
				local('rm -rf temp temp.zip')
				return 0

		local('mkdir temp')
		local('cp %s temp' % fileName)
		local('zip -r temp temp')

		put('temp.zip', '/var/www/%s/static/temp.zip' % domain)
		run('unzip -j temp.zip')

		#clean up local temp stuff
		run('rm temp.zip')
		local('rm -rf temp temp.zip')

def remove_file(fileName):
	#sets working directories to the static directories

	with cd('/var/www/%s/static/' % domain):
		
		if exists('%s' % (fileName)):
			#Then the file already exists in the static directory on the server

			confirm = prompt('Warning: About to remove: %s. Do you wish to proceed? [y/n]: ' % fileName)
			if (confirm == 'y'):
				run('rm %s' % fileName)
			else: 
				print("Aborted by user.")
		else:
			print("File does not exist.")

def push_resume():
		with lcd('_static'):
			run('rm /var/www/%s/www/Resume.pdf' % domain)
			run('rm /var/www/%s/static/Resume.pdf' % domain)
			put('Resume.pdf', '/var/www/%s/static/Resume.pdf' % domain)
			run('cp /var/www/%s/static/Resume.pdf /var/www/%s/www/Resume.pdf' % (domain,domain))

#Pushes the entire _static folder to the static directory on the server
def push_private():
	local('zip -r _private _private')
	run('rm -rf /var/www/%s/private' % domain)
	put('_private.zip', '/var/www/%s/_private.zip' % (domain))
	run('unzip /var/www/%s/_private.zip -d /var/www/%s' % (domain, domain))
	run('mv /var/www/%s/_private /var/www/%s/private' % (domain, domain))
	run('rm -rf /var/www/%s/_private.zip' % domain)
	local('rm -rf _private.zip')

def push_file_private(fileName):
	#sets working directories to the static directories

	with lcd('_private'), cd('/var/www/%s/private/' % domain):
		
		local('mkdir temp')
		local('cp %s temp' % fileName)
		local('zip -r temp temp')
		if exists('%s' % (fileName)):
			#Then the file already exists in the static directory on the server
			run('rm %s' % fileName)
		put('temp.zip', '/var/www/%s/private/temp.zip' % domain)
		run('unzip -j temp.zip')

		#clean up local temp stuff
		run('rm temp.zip')
		local('rm -rf temp temp.zip')

def remove_file_private(fileName):
	#sets working directories to the static directories

	with cd('/var/www/%s/private/' % domain):
		
		if exists('%s' % (fileName)):
			#Then the file already exists in the static directory on the server

			confirm = prompt('Warning: About to remove: %s. Do you wish to proceed? [y/n]: ' % fileName)
			if (confirm == 'y'):
				run('rm %s' % fileName)
			else: 
				print("Aborted by user.")
		else:
			print("File does not exist.")