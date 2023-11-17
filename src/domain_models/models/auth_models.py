from pydantic import BaseModel
from typing import Optional
from ..utils.regexs import EMAIL_REGEX
from ..enums.error_enum import ErrorEnum

class AuthEmailModel(BaseModel):
    email: Optional[str]

    def check_email_format(self) -> Optional[ErrorEnum]:
        if not self.email:
            return ErrorEnum.EMPTY_EMAIL
        elif not EMAIL_REGEX.search(self.email):
            return ErrorEnum.INVALID_EMAIL_FORMAT

class AuthPasswordModel(BaseModel):
    password: Optional[str]

    def check_password_format(self) -> Optional[ErrorEnum]:
        if not self.password:
            return ErrorEnum.EMPTY_PASSWORD
        elif len(self.password) < 8:
            return ErrorEnum.TOO_SHORT_PASSWORD_SIZE
        elif len(self.password) >= 24:
            return ErrorEnum.TOO_LONG_PASSWORD_SIZE
