from app import db

class User(db.Model):
    tablename = ['User']
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    answers = db.Column(db.String(), default="Error in retrieving the answers")
    def __repr__(self):
        return f"User('{self.lastname}', '{self.email}', '{self.phone}')"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    skillGroup = db.Column(db.String())
    q_number = db.Column(db.String())
    component = db.Column(db.String())

class RegistrationForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    residence = db.Column(db.String())
    region = db.Column(db.String())
    gender = db.Column(db.String())
    age = db.Column(db.String())
    market = db.Column(db.String())
    recommendation = db.Column(db.String())
    nationality = db.Column(db.String())
    answers = db.Column(db.String())
    def __repr__(self):
        return f"User('{self.lastname}', '{self.email}', '{self.phone}')"
