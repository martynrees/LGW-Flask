# Webex Calling Local Gateway (LGW) Config Generator

This Flask application will use a Jinja2 template to generate the configuration required for an CSR1k ios-xe router to be able to register to your Webex Calling tenant and provide local SIP PSTN gateway access.
The configuration provided is an example only and may require additional configuration in order to work with individual SIP providers.

The solution is built on Python, Jinja2, Flask, WTForms and Bootstrap.

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
Browse to http://docker-ip:5000 
```

The web interface takes in a range of attributes to generate an ios-xe config that will register a CSR1k virtual appliance to Webex Calling as a LGW.
A valid AX licence for the required BW and smart account is required to licence the appliance. If left unlicenced then the CSR1k will run in demo mode with limited BW, which may be appropriate for initial PoC testing.
Ensure that all fields are completed correctly and once submitted the application will return an example config that will register the CUBE to Wbx Calling.

It is assumed that the user has knowledge (and appropriate access) to completed the LGW configuration through WCH. References can also be found here:
```
https://help.webex.com/en-us/32gfts/Webex-Calling-Configuration-Workflow#Overview-of-Webex-Calling
```