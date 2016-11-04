SBB API Client
==============

CLI interface for searching train connections using SBB's OpenData API.

Getting Started
---------------

Install requirements and invoke script

		pyvenv env
		source env/bin/activate
		pip install -r requirements.txt
		./sbb.py -h


Testing
-------

The `test` directory has a sample JSON answer and a script to fiddle around without live API connection. Invoke with

		PTYHONPATH=. python test/test.py

