from entities import TodoModel, ErrorEnum
from datetime import datetime

class TestTodoModel:
    
    @staticmethod
    def test_title_format():
        todo = TodoModel(id='xxx', created_at=datetime.now())

        # 空文字をすることができる
        todo.title = ''
        assert todo.check_title_format() is None

        # 1文字でも良い
        todo.title = 'x'
        assert todo.check_title_format() is None

        # 文字を設定しなくても良い
        todo.title = None
        assert todo.check_title_format() is None

        # 文字数の上限
        todo.title = '1234567890123456789012345678901234567890'
        assert todo.check_title_format() is None

        # 文字数の上限をオーバー
        todo.title = '12345678901234567890123456789012345678901'
        assert todo.check_title_format() is ErrorEnum.TOO_LONG_TITLE

    @staticmethod
    def test_description_format():
        todo = TodoModel(id='xxx', created_at=datetime.now())

        # 空文字をすることができる
        todo.description = ''
        assert todo.check_description_format() is None

        # 1文字でも良い
        todo.description = 'x'
        assert todo.check_description_format() is None

        # 文字を設定しなくても良い
        todo.description = None
        assert todo.check_description_format() is None

        # 文字数の上限
        todo.description = 'x' * 200
        assert todo.check_description_format() is None

        # 文字数の上限をオーバー
        todo.description = 'x' * 201
        assert todo.check_description_format() is ErrorEnum.TOO_LONG_DESCRIPTION
