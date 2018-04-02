from smb.SMBConnection import SMBConnection
import configparser

config = configparser.RawConfigParser()
config.read(r'../local.properties')

USERNAME = config.get('ServerSection', 'server.username')
PASSWORD = config.get('ServerSection', 'server.password')
LOCAL_NETBIOS_NAME = "photoframe"
REMOTE_NETBIOS_NAME = config.get('ServerSection', 'server.net.bios.name')
IP_ADDRESS = config.get('ServerSection', 'server.ip.address')
SHARE_NAME = config.get('ServerSection', 'server.shared.name')


conn = SMBConnection(USERNAME, PASSWORD, LOCAL_NETBIOS_NAME, REMOTE_NETBIOS_NAME)
print(conn.connect(IP_ADDRESS))

#results = conn.listPath(SHARE_NAME, '/optionally/some/subfolder')
results = conn.listPath(SHARE_NAME, '/')

for x in results:
    print(x.filename)
