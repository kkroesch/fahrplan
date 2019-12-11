SBB API Client
==============

CLI interface for searching train connections using [SBB's OpenData API](http://sbb.xiala.net/).

Getting Started
---------------

Install requirements and invoke script:

		pyvenv env
		source env/bin/activate
		pip install -r requirements.txt
		./sbb.py conn DEPARTURE-ID DESTINATION-ID

Find station IDs by entering the first few letters of the station's name

		./sbb.py id Dull

Sample Output:

![screenshot](https://raw.githubusercontent.com/kkroesch/sbb-api/master/doc/screenshot.png)

Testing
-------

The `test` directory has a sample JSON answer and a script to fiddle around without live API connection. Invoke with

		PTYHONPATH=. python test/test.py

