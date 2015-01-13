#!/usr/bin/env python3

from namespace import namespace
"""
TODO:
- Detectar que no existe en el path
- Generar uno vacio
- Default path en windows
- Default path en linux
"""
import os

# Kludge in order to use FileNotFoundError in Python2
try: FileNotFoundError
except NameError:
	FileNotFoundError=IOError

def defaultDbConfigFile() :
	return

def dbconfig(config=None, configfile=None):
	schema = config or os.environ.get('SE_DATABASE', 'default')
	result = namespace.load(configfile)[schema]
	return result


import unittest
class dbconfig_test(unittest.TestCase):
	def addFile(self, file) :
		self.toRemove.append(file)
	def setUp(self) :
		self.toRemove=[]
		self.data = namespace(
			default = namespace(
				user='myuser',
				server='myserver',
				password='mypassword',
				),
			alternative=namespace(
				user='otheruser',
				server='otherserver',
				password='otherpassword',
				),
			)
		self.data.dump('config.yaml')
		self.addFile('config.yaml')

	def tearDown(self):
		for f in self.toRemove:
			os.unlink(f)

	def test_dbconfig_notExisting(self) :
		with self.assertRaises(FileNotFoundError) :
			dbconfig(configfile='nonexistingconfig')

	def test_dbconfig_takesDefaultData(self) :
		config=dbconfig(configfile='config.yaml')
		self.assertDictEqual(config, self.data.default)

	def test_dbconfig_explicitConfig_takesAlternativeData(self) :
		config=dbconfig(config='alternative',configfile='config.yaml')
		self.assertDictEqual(config, self.data.alternative)

	def test_dbconfig_environment_takesAlternativeData(self) :
		os.environ['SE_DATABASE']='alternative'
		config=dbconfig(configfile='config.yaml')
		self.assertDictEqual(config, self.data.alternative)
		del os.environ['SE_DATABASE']



if __name__ == '__main__':
	import sys
	sys.exit(unittest.main())


