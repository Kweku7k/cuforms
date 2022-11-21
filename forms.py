from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegistrationForms(FlaskForm):
    residence = StringField('Residence', validators=[DataRequired()])
    region = StringField('Region of permanent residence', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    nationality = StringField('Nationality')
    market = SelectField('How did you hear about central university before coming here.', choices=[('Media/Newspaper', 'Media/Newspaper'),('Friend or Relative', 'Friend or Relative'),('The Internet', 'The Internet'),('Outreach Programme', 'Outreach Programme')])
    recommendation = BooleanField('Would you recommend Central University to a potential applicant')
    submit = SubmitField('Okay')

class Questions(FlaskForm):
    question = StringField('Phone', validators=[DataRequired()])
    q_number = StringField('Question Number')
    component= SelectField('Component', choices=[('--Component--', '--Component--'),('Prior Knowledge', 'Prior Knowledge'), ('Social Engagement', 'Social Engagement'), ('Relevance', 'Relevance'), ('Application', 'Application'),('Lecture Focus', 'Lecture Focus'),('Meaningful Application', 'Meaningful Application'),('Organisation', 'Organisation'),('Visualization', 'Visualization'),('Elaboration', 'Elaboration'),('Repetition', 'Repetition'),('Empowerment', 'Empowerment'),('Usefulness', 'Usefulness'),('Success', 'Success'),('Interest', 'Interest'),('Caring', 'Caring')])
    skillGroup = SelectField('Skill Group', choices=[('--Skill Group--', '--Skill Group--'),('Learner Centricity', 'Learner Centricity'),('Teaching for Recall', 'Teaching for Recall'),('Teaching for Engagement', 'Teaching for Engagement')])
    submit = SubmitField('Submit')

class NewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Name', validators=[DataRequired()])
    consumer = StringField('consumer')
    submit = SubmitField('Submit')

class NewQuestion(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    questionUpdate = StringField('QuestionUpdate')
    submit = SubmitField('Submit')






    