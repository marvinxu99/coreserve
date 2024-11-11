from urllib.parse import urlparse   # For safer URL validation

url = '''https://id.gov.bc.ca/login/oidc/authorize/?scope=openid+profile+email&state=uWu92kk1KVOK-vhIhqrUYYTrL8q53KoK_Q3omuoWJ_g.6DIVPIu9eCY.XQUDrAfLQ7SknsIjcOEYmw&response_type=code&client_id=urn.ca.bc.gov.health.healthgateway.prod&redirect_uri=https%3A%2F%2Floginproxy.gov.bc.ca%2Fauth%2Frealms%2Fhealth-gateway-gold%2Fbroker%2Fbcsc%2Fendpoint&prompt=login&nonce=roODpR5Mj-fEdaW1lUbPYA
'''
parsed_url = urlparse(url)

print(parsed_url.scheme) # Output: https 
print(parsed_url.netloc) # Output: www.example.com 
print(parsed_url.path) # Output: /path/to/page 
print(parsed_url.query) # Output: query=example 
print(parsed_url.fragment)