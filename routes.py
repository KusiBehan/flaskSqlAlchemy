from flask import render_template, request

from models import Task


def register_routes(app, db):
    @app.route('/', methods=['GET'])
    def index():
        tasks = Task.query.all()
        return str(tasks)

    @app.route('/task', methods=['POST'])
    def create_task():
        task = request.form.get('task')
        status = request.form.get('status')

        task = Task(task=task, status=status)
        db.session.add(task)
        db.session.commit()

        return str(task)
