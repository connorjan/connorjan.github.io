from fabric.api import *

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

def push_static():
	local('rm -rf _static.zip')
	local('zip -r _static _static')
	run('rm -rf /var/www/%s/_static.zip /var/www/%s/static' % (domain,domain))
	put('_static.zip', '/var/www/%s/_static.zip' % (domain))
	run('unzip /var/www/%s/_static.zip -d /var/www/%s' % (domain, domain))
	run('mv /var/www/%s/_static /var/www/%s/static' % (domain, domain))

