from entities import UserModel, ErrorEnum
from datetime import datetime

class TestUserModel:
    
    @staticmethod
    def test_check_email_format():
        user = UserModel(id='xxx', created_at=datetime.now())

        # メールフォーマットが正しい
        user.email = 'ban@aigram.jp'
        assert user.check_email_format() is None

        # メールアドレスが設定されていない
        user.email = None
        assert user.check_email_format() == ErrorEnum.EMPTY_EMAIL

        # メールアドレスのフォーマットが正しくない
        user.email = 'ban@aigram'
        assert user.check_email_format() == ErrorEnum.INVALID_EMAIL_FORMAT

        # メールアドレスに「.」を設定している -> ok
        user.email = 'ban.@aigram.jp'
        assert user.check_email_format() is None

        # メールアドレスに「_」を設定している -> ok
        user.email = 'ban_naohiko@aigram.jp'
        assert user.check_email_format() is None

    @staticmethod
    def test_check_password_format():
        user = UserModel(id='xxx', created_at=datetime.now())

        # パスワードが正しい（下限）
        user.password = '12345678'
        assert user.check_password_format() is None

        # パスワードが正しい（上限）
        user.password = '12345678901234567890123'
        assert user.check_password_format() is None

        # パスワードが設定されていない
        user.password = None
        assert user.check_password_format() is ErrorEnum.EMPTY_PASSWORD

        # パスワードの文字数が少ない
        user.password = '1234567'
        assert user.check_password_format() is ErrorEnum.TOO_SHORT_PASSWORD_SIZE

        # パスワードの文字数が多い
        user.password = '123456789012345678901234'
        assert user.check_password_format() is ErrorEnum.TOO_LONG_PASSWORD_SIZE
