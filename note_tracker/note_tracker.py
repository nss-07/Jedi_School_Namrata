from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

'''class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')'''


TODOS = {
    'user1': {
        'todo1': {'task': 'task_desc'},
        'todo2': {'task': 'task_desc'}
    },
    'user2': {
        'todo1': {'task': 'task_desc'},
        'todo2': {'task': 'task_desc'}
    }
}


def validate_user_id(user_id):
    if user_id not in TODOS:
        abort(404, message="User {} doesn't exist".format(user_id))


def validate_todo_id(user_id, todo_id):
    if todo_id not in TODOS[user_id]:
        abort(404, message="Todo {} doesn't exist for user {}".format(todo_id, user_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, user_id, todo_id):
        validate_todo_id(user_id, todo_id)
        return TODOS[user_id][todo_id]

    def delete(self, user_id, todo_id):
        validate_todo_id(user_id, todo_id)
        del TODOS[user_id][todo_id]
        return '', 204

    def put(self, user_id, todo_id):
        validate_todo_id(user_id, todo_id)
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[user_id][todo_id] = task
        return task, 201


class UserTodos(Resource):
    def get(self, user_id):
        validate_user_id(user_id)
        return TODOS[user_id]

    def delete(self, user_id):
        validate_user_id(user_id)
        del TODOS[user_id]
        return '', 204

    # def put(self, user_id):
    #     pass

    def post(self, user_id):    # is this put or post??
        validate_user_id(user_id)
        args = parser.parse_args()
        todo_id = int(max(TODOS[user_id].keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[user_id][todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        user_id = int(max(TODOS.keys()).lstrip('user')) + 1
        user_id = 'user%i' % user_id
        TODOS[user_id] = {}
        todo_id = 'todo1'
        TODOS[user_id][todo_id] = {'task': args['task']}
        return TODOS[user_id], 201


# API Resource Routing
api.add_resource(TodoList, '/todos')
api.add_resource(UserTodos, '/todos/<user_id>')
api.add_resource(Todo, '/todos/<user_id>/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
