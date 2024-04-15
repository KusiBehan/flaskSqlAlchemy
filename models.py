from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    status = db.Column(db.Text)

    def __repr__(self):
        return f'{self.id} , {self.task} , {self.status} |'


