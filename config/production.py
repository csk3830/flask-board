from config.default import *
from logging.config import dictConfig


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='H+!(y_o*Q;q]j4Pa8E3SVF0C4X+hH0M}',
    url='ls-6ad2a389ec91d534451478e6023113103a4b9246.cypmmlwk7zug.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'x0be\x92\x1ailU\x7f\x07_\xb5R\xaaD\xb4'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})