# Webex Calling Local Gateway (LGW) Config Generator

This Flask application will use a Jinja2 template to generate the configuration required for an CSR1k ios-xe router to be able to register to your Webex Calling tenant and provide local SIP PSTN gateway access.
The configuration provided is an example only and may require additional configuration in order to work with individual SIP providers.

There are two ways that this application can be run.
1. As a python virtual environment.
```
mkdir lgw
cd lgw
git clone git@github.com:martynrees/Wbx-Calling-LGW.git
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
python3 server.py
Browse on your local machine to http://127.0.0.1:5000
```
2. As a Docker container.
```
mkdir lgw
cd lgw
git clone git@github.com:martynrees/Wbx-Calling-LGW.git
docker build -t lgw .
docker run -d -p 5000:5000 lgw
Browse on your local machine to http://127.0.0.1:5000 (also accessable from other machines)
```
