'''
The ConstantsEnvLocal file is a file similar to this but if you import it at the beginning,
the constants are the same and the content is placed in quotes, for example API_KEY='your_bot_token'
'''
import ConstantsEnvLocal as keys

BOT_NAME = keys.BOT_NAME
API_KEY = keys.API_KEY
ENV = keys.ENV  # This can be 'dev' or 'prod'
STORE_API_URL = keys.STORE_API_URL
