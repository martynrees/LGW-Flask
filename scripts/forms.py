from wtforms import Form, StringField, IntegerField, validators

class lgw_form(Form):
    router_name = StringField('Router Name:', [validators.InputRequired()])
    cube_capacity = IntegerField('Cube Capacity: ', [validators.InputRequired(), validators.NumberRange(min=1)]) 
    smart_token = StringField('Smart Token:')
    lic_bandwidth = IntegerField('Bandwidth Licence value (MB):', [validators.InputRequired()])
    dns = StringField('DNS Server(s):', [validators.InputRequired(), validators.IPAddress()])
    domain_name = StringField('Domain Name:', [validators.InputRequired()])
    interface = StringField('Router Interface:', [validators.InputRequired()])
    int_ip = StringField('Main Interface IP Address:', [validators.InputRequired()])
    int_subnet = StringField('Main Interface Subnet Mask:', [validators.InputRequired()])
    int_gateway = StringField('Default Route:', [validators.InputRequired()])
    username = StringField('Router Username:', [validators.InputRequired()])
    password = StringField('Router Password:', [validators.InputRequired()])
    ntp_server = StringField('NTP Server:', [validators.InputRequired()])
    password_encrypt = StringField('Config Key Password Encrypt:', [validators.InputRequired()])
    sip_networks = StringField('SIP Networks:', [validators.InputRequired()])
    webex_otg = StringField('Webex OTG:', [validators.InputRequired()])
    webex_domain = StringField('Webex Domain:', [validators.InputRequired()])
    webex_LGU = StringField('Webex LGU:', [validators.InputRequired()])
    webex_username = StringField('Webex Username:', [validators.InputRequired()])
    webex_password = StringField('Webex Password:', [validators.InputRequired()])  
    webex_proxy = StringField('Webex Proxy:', [validators.InputRequired()])
    sip_sbcip= StringField('PSTN SBC IP Address:', [validators.InputRequired()])