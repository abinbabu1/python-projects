'''
To Do List using REST API

There are two endpoints
'/todos'
'/todos/<integer>'

We can get all to do tasks by sending a get request to '/todos'
We can add, update, get and delete a task with the endpoint '/todos/<integer>'
'''

#Imports
from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

#Initialising Flask app and API
app = Flask(__name__)
api = Api(app)

#Setting up the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Creating model for tasks
class TaskModel(db.Model):
	__tablename__ = 'tasks'

	_id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(100), unique=True)
	summary = db.Column(db.String(200))

# db.create_all()

#Using RequestParser to format the arguments that are passed in to create a new task
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help='Task is required', required=True)
task_post_args.add_argument("summary", type=str, help='Summary is required', required=True)

#Using RequestParser to format the arguments that are passed in to update a task
task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task", type=str)
task_put_args.add_argument("summary", type=str)

#Using fields to format data retrieved from the SQLite database
#The three fields are id, task and summary
resource_fields = {
	'_id': fields.Integer,
	'task': fields.String,
	'summary': fields.String
}

class Index(Resource):
	def get(self):
		return "message": "Go to /todos to see all todo items"

#Class to create, get, delete and update tasks
#@marshal_with decorater is used with the resource_fields dictionary
#to format the data retrieved from the database into serialisable data 
class ToDo(Resource):

	#GET a task
	@marshal_with(resource_fields)
	def get(self, todo_id):
		'''
		Check whether a task with the given task ID exists in the Database.
		If it exists, return details of the task.
		Else, return 404 error
		'''
		task = TaskModel.query.filter_by(_id=todo_id).first()
		if task:
			return task, 200
		else:
			abort(404, message="Task ID not found!")

	#Create a new task
	@marshal_with(resource_fields)
	def post(self, todo_id):
		'''
		Parse the arguments passed in with the POST request.
		Check whether a task with the given task ID already exists in the Database.
		If yes, abort with error code 409.
		Then check if a task with the given task name already exists in the Database.
		Task names are set as unique.
		If such a task name already exists, abort.
		Else, create a new Model object and add the task to the Database
		'''
		args = task_post_args.parse_args()

		task = TaskModel.query.filter_by(_id=todo_id).first()
		if task:
			abort(409, message="Task ID already exists!")
		
		task_two = TaskModel.query.filter_by(task=args['task']).first()
		if task_two:
			abort(409, message="Task name already exists!")

		new_task = TaskModel(_id=todo_id, task=args['task'], summary=args['summary'])
		db.session.add(new_task)
		db.session.commit()

		return new_task, 201

	#Update a task
	@marshal_with(resource_fields)
	def put(self, todo_id):

		'''
		Parse the arguments passed in with the PUT request
		Check if a task with the given task ID exists in the Database
		If not, cannot update, so abort.
		If such a task exists, check the arguments passed.
		If it has task and summary, update it accordingly
		'''
		args = task_put_args.parse_args()

		new_task = TaskModel.query.filter_by(_id=todo_id).first()
		if not new_task:
			abort(409, message="Task ID doesn't exist!")

		task_two = TaskModel.query.filter_by(task=args['task']).first()
		if task_two:
			abort(409, message="Task name already exists!")
			
		if args['task']:
			new_task.task = args['task']
		if args['summary']:
			new_task.summary = args['summary']

		# db.session.add(new_task)
		db.session.commit()
		return new_task, 201

	#Delete a task
	def delete(self, todo_id):
		'''
		Check if a task with the given task ID exists in the Database
		If not, abort
		If such a task exists, delete that task from the database 
		'''
		task = TaskModel.query.filter_by(_id=todo_id).first()
		if not task:
			abort(409, message="Task ID doesn't exist!")

		db.session.delete(task)
		db.session.commit()
		return {"message": f"Task {todo_id} deleted!"}

#Class to view all tasks
class ToDoList(Resource):
	@marshal_with(resource_fields)
	def get(self):
		todos = TaskModel.query.all()
		return todos, 200

#Adding the endpoints
api.add_resource(Index, '/')
api.add_resource(ToDoList, '/todos')
api.add_resource(ToDo, '/todo/<int:todo_id>')

if __name__=='__main__':
	app.run()