from fabric.api import *
from fabric.contrib.files import exists
from fabric.context_managers import cd,lcd 

env.user = 'connor'
env.hosts = ['connorgoldberg.com']

domain = 'connorgoldberg.com'
subdom = 'www'

def push():
    local('jekyll build')
    local('zip -r _site _site')
    run('rm -f /var/www/%s/_site.zip' % (domain))
    run('rm -rf /var/www/%s/_site' % (domain))
    put('_site.zip', '/var/www/%s/_site.zip' % (domain))
    run('unzip /var/www/%s/_site.zip -d /var/www/%s' % (domain, domain))
    run('rm -rf /var/www/%s/%s' % (domain, subdom))
    run('mv /var/www/%s/_site /var/www/%s/%s' % (domain, domain, subdom))

#Pushes the entire _static folder to the static directory on the server
def push_static():
	local('rm -rf _static.zip')
	local('zip -r _static _static')
	run('rm -rf /var/www/%s/_static.zip /var/www/%s/static' % (domain,domain))
	put('_static.zip', '/var/www/%s/_static.zip' % (domain))
	run('unzip /var/www/%s/_static.zip -d /var/www/%s' % (domain, domain))
	run('mv /var/www/%s/_static /var/www/%s/static' % (domain, domain))

"""
Pushes a single file from the _static folder to the static directory on the server.
Syntax in command line:
$ fab push_file:<filename>
"""

def push_file(fileName):
	#sets working directories to the static directories
	with lcd('_static'), cd('/var/www/%s/static/' % domain):
		
		local('mkdir temp')
		local('cp %s temp' % fileName)
		local('zip -r temp temp')
		if exists('%s' % (fileName)):
			#Then the file already exists in the static directory on the server
			run('rm %s' % fileName)
		put('temp.zip', '/var/www/%s/static/temp.zip' % domain)
		run('unzip -j temp.zip')

		#clean up local temp stuff
		run('rm temp.zip')
		local('rm -rf temp temp.zip')

def push_resume():
		with lcd('_static'):
		
			run('rm /var/www/%s/www/Resume.pdf' % domain)
			run('rm /var/www/%s/static/Resume.pdf' % domain)
			put('Resume.pdf', '/var/www/%s/static/Resume.pdf' % domain)
			run('cp /var/www/%s/static/Resume.pdf /var/www/%s/www/Resume.pdf' % (domain,domain))
