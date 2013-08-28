from fabric.api import *



def build():
	local('git checkout master')
	local('mkdir -p tmp')
	local('rsync -av web/ tmp/')
	local('rsync -av lib tmp/')
	local('ghp-import -pm "Updated the site" tmp/')
	local('rm -rf tmp')