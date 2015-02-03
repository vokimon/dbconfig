# python-configdb

[![Build Status](https://travis-ci.org/vokimon/python-configdb.png?branch=master)](https://travis-ci.org/vokimon/configdb)

Quick way to store db connection details out of sources.

  import configdb
  import ooop
  ooop.OOOP( configdb.configdb(required="user pwd dbname") )
  ...

By default, attributes are taken from a YAML file at system
defined user configuration location. From the key (profile) 'default'.
If the file is not there, it is created with a yaml file
with null values. You have to fill them.

To change the profile you can use the 'profile' keyword or
`CONFIGDB_PROFILE` environ.

https://github.com/vokimon/python-configdb


