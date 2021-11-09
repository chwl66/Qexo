"""
在这里部署配置你的数据库信息
configuration your MongoDB database here
"""

CONFIGS = {
    'DOMAINS': ['.vercel.app', '127.0.0.1'],   # allow hosts
    'MONGODB_HOST': 'mongodb+srv://xxx.xxx.mongodb.net',  # your MongoDB host
    'MONGODB_PORT': 27017,  # default is '27017'
    'MONGODB_USER': 'user',  # your MongoDB username
    'MONGODB_DB': 'user',  # your MongoDB database name
    'MONGODB_PASS': 'password',  # your MongoDB password
}