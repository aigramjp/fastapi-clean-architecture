from enum import Enum

class ErrorEnum(str, Enum):
    EMPTY_EMAIL = 'empty password'
    INVALID_EMAIL_FORMAT = 'invalid email format'

    EMPTY_PASSWORD = 'empty password'
    TOO_SHORT_PASSWORD_SIZE = 'too short password size'
    TOO_LONG_PASSWORD_SIZE = 'too long password size'

    TOO_LONG_TITLE = 'too long title'
    TOO_LONG_DESCRIPTION = 'too long description'

