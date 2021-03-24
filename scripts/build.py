from jinja2 import Template

def generate_config(router_name, cube_capacity, smart_token, lic_bandwidth, dns, domain_name, 
                    interface, int_ip, int_subnet, int_gateway,username, password,
                    ntp_server, password_encrypt, sip_networks, webex_otg, webex_domain, webex_LGU, webex_username,
                    webex_password, webex_proxy, sip_sbcip):
    variables = {'router_name':router_name,
                'cube_capacity':cube_capacity,
                'smart_token':smart_token,
                'lic_bandwidth':lic_bandwidth,
                'dns':dns,
                'domain_name':domain_name,
                'interface':interface,
                'int_ip':int_ip,
                'int_subnet':int_subnet,
                'int_gateway':int_gateway,
                'username':username,
                'password':password,
                'ntp_server':ntp_server,
                'password_encrypt':password_encrypt,
                'sip_networks':sip_networks,
                'webex_otg':webex_otg,
                'webex_domain':webex_domain,
                'webex_LGU':webex_LGU,
                'webex_username':webex_username,
                'webex_password':webex_password,
                'webex_proxy':webex_proxy,
                'sip_sbcip':sip_sbcip}

    with open('./scripts/base_config.j2') as file:
        jinja_template = Template(file.read())
        config = jinja_template.render(variables=variables)
        return config
