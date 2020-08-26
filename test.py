import configparser as parser

config = parser.RawConfigParser()
config.read('./settings.ini')

print(config.get('secrets', 'SECRET_KEY'))

#print(config['secrets']['SECRET_KEY'])
