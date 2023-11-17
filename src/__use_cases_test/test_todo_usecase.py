from usecases import TodoUsecase

class TestTodoUsecase:
    
    @staticmethod
    def test_create_todo():
        todo1 = TodoUsecase.create_todo(title='x', description='x')
        todo2 = TodoUsecase.create_todo(title='x', description='x')
        
        # idは毎回ランダムに生成される
        assert todo1.id != todo2.id

        # 作成時間は作成のタイミングのタイムスタンプであり、毎回異なる
        assert todo1.created_at != todo2.created_at
