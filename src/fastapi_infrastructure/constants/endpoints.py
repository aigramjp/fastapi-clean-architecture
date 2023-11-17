

class Endpoints:
    class Todo:
      base = '/todo'
      get_todo = f'{base}/get-todo'
      update_todo = f'{base}/update-todo'
      delete_todo = f'{base}/delete-todo'
      create_todo = f'{base}/create-todo'
      get_todos = f'{base}/get-todos'
      