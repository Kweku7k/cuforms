from flask import Flask,redirect,url_for,render_template,request, flash, session, jsonify, json
from forms import *
# from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from send_mail import send_mail
# from flask_mail import Mail, Message
import urllib.request, urllib.parse
import urllib
from urllib.parse import urlencode
import requests
import webbrowser
import os
import http.client


app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628b21sb13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# mail= Mail(app)

# app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://isbiiqutsfeekn:c2058971f5bb424127a6b01d9ed3419b5599727a6f67d80136187b13465fe69a@ec2-34-200-94-86.compute-1.amazonaws.com:5432/d3ucdicb4224a8'


# api_v1_cors_config = {
#     "origins":["http://localhost:3000"],
#    " methods":['POST','OPTIONS']
#     "Access-Control-Allow-Origin":'localhost:3000'
# }

# cors = CORS(app, resources={
#     r"/addpost":api_v1_cors_config
# })
# app.config['CORS_HEADERS'] = 'Content-Type'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mr.adumatta@gmail.com'
app.config['MAIL_PASSWORD'] = 'Nimda@2021'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# mail= Mail(app)


#Functions
def skill(percentage):
    poor = range(0, 29) 
    fair = range(30, 59)
    acceptable = range(60, 75)
    good = range(76, 92)
    outstanding = range(93,97)
    exceptional = range(98,101)
    yourskill = "not set"
    for i in poor:
        if percentage == i:
            print(i)
            yourskill = "Poor"
    for i in fair:
        if percentage == i:
            print(i)
            yourskill = "Fair"
    for i in acceptable:
        if percentage == i:
            print(i)
            yourskill = "Acceptable"
    for i in good:
        if percentage == i:
            print(i)
            yourskill = "Good"
    for i in outstanding:
        if percentage == i:
            print(i)
            yourskill = "Outstanding"
    for i in exceptional:
        if exceptional == i:
            print(i)
            yourskill = "Exceptional"
    return yourskill

def findPercentage(score, total):
    try:
        percentage = str(round((score / total) * 100)) + "%"
    except ZeroDivisionError:
        percentage = 0
    return percentage

def sendmail(body):
    msg = Message('Results from TNP', sender = 'mr.adumatta@gmail.com', recipients = ['lecturesoft@gmail.com','nkba@live.com'])
    msg.body = body
    mail.send(msg)
    return 'Sent'

def sendtelegram(params):
    url = "https://api.telegram.org/bot1699472650:AAEso9qTbz1ODvKZMgRru5FhCEux_91bgK0/sendMessage?chat_id=-511058194&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

def findTotal(array):
    total = 0
    for i in range(len(array)):
        total = total + array[i]
        print("Function " + str(total))
    # percentage
    groupTotal = len(array) * 4
    print("GROUP TOTAL")
    print(groupTotal)
    print(len(array))
    print(total)
    percentage = findPercentage(total, groupTotal)

    return percentage

@app.route('/', methods=['GET','POST'])
def landing():
    return render_template('landingPage.html')

@app.route('/allSurveys')
def allSurveys():
    flash(f'Thanks for filling this bad bitch outtt!!', 'success')
    return render_template('allSurveys.html')

@app.route('/info', methods=['GET','POST'])
def home():
    session['qNumber'] = 1
    form = RegistrationForms()
    if form.validate_on_submit():
        residence = form.residence.data
        region = form.region.data
        gender = form.gender.data
        age = form.age.data
        nationality = form.nationality.data
        market = form.market.data
        recommendation = form.recommendation.data
        newRegistration = RegistrationForm( residence = residence, gender = gender, age = age, nationality = nationality, market = market, region = region, recommendation = recommendation)
        db.session.add(newRegistration)
        db.session.commit()
        return redirect(url_for('exitform'))
    return render_template('index.html', form=form)


@app.route('/adduser',methods=['POST'])
# @cross_origin() 
def adduser():
    newUser = User(firstname=request.json['firstname'], lastname=request.json['lastname'], phone=request.json['phone'], email=request.json['email'], answers="None")
    print('From react')
    print(newUser)
    return render_template('adminpage.html')




# @app.route("/ussd")
# def ussd():
#     conn = http.client.HTTPSConnection("{{USSDBaseURL}}{{endPoint}}")
#     payload = "{\n    \"USERID\": \"NALOTest\",\n    \"MSISDN\": \"233XXXXXXXXX\",\n    \"USERDATA\": \"3\",\n    \"MSGTYPE\": false,\n    \"NETWORK\": \"MTN\"\n}"
#     headers = {}
#     conn.request("POST", "/", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))
#     return 'done'


@app.route("/ussd", methods = ['GET','POST'])
def ussd():
  
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "")

#   session_id   = "sessionId"
#   serviceCode  = "serviceCode"
#   phone_number = "phoneNumber"
#   text         = "1"

  if text == '':
      print("text" + text)
      # This is the first request. Note how we start the response with CON
      response  = "CON Welcome to Shell, what would you like to do today \n"
      response += "1. Pay for fuel \n"
      response += "2. Join Loyalty Program"

  elif text    == '1':
      # Business logic for first level response
      print("text" + text)

      response  = "CON Please enter the attendants code \n"
    #   response += "1. Account number"

  elif text   == '2':
      print("text" + text)

      # This is a terminal request. Note how we start the response with END
      response = "END Your phone number is " + phone_number

  elif text          == '1*1':
      print("text" + text)

      # This is a second level response where the user selected 1 in the first instance
    #   accountNumber  = "ACC1001"
      # This is a terminal request. Note how we start the response with END
      response       = "Please enter the amount fuel you are buying? " 

  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response

# @app.route("/phone/<string:phonenumber>")
# def phone(phonenumber):
#     credentials = 'selasi@delaphonegh.com', '3AsX3Jz7u28NV6U'
#     session = requests.Session()
#     session.auth = credentials

#     os.system("zoiper")

#     params = {
#         'query': 'role:end-user phone:'+phonenumber,
#         'sort_by': 'created_at',
#         'sort_order': 'asc'
#     }

#     url = 'https://delaphonegh.zendesk.com/api/v2/search.json?' + urlencode(params)
#     response = session.get(url)
#     if response.status_code != 200:
#         print('Status:', response.status_code, 'Problem with the request. Exiting.')
#         exit()

#     # Print the subject of each ticket in the results
#     data = response.json()
#     for result in data['results']:
#         userId = result['id']
#         userName = result['name']
#         print(userId)
#         print(userName)
#         webbrowser.open("https://delaphonegh.zendesk.com/agent/users/"+str(userId))

#     return phonenumber

@app.route('/testPost/<string:number>', methods=['POST','GET'])
def testPost(number):
    print("gotten requestio")
    print(number)
    # point = int(request.data[ adj ])
    print(request.data)
    return "DONE"

@app.route('/users', methods=['POST','GET'])
def users():
    users = User.query.all()
    allusers = dict.fromkeys(users)
    # allusers = us /ers 
    # users = [{'id':1, 'name':'Kweku'},{'id':2, 'name':'Nana'}]
    print(type(users))
    print(type(allusers))
    print(allusers)
    # return json({'users':users})
    return str(users)

    # return json.dumps(
    #     {'users':users}
    # )
    # response = app.response_class(
    #     response=json.dumps(
    #         [
    #             {
    #         username:users.firstname,
    #         email:users.email,
    #        id:users.id
    #             }
    #         ]
    #     ),
    #     mimetype='application/json'
    # )
    # return response

@app.route('/signup', methods=['POST','GET'])
def signup():

    return "Signup"

@app.route('/forms')
def forms():
    questions = Question.query.order_by(Question.id.asc()).all()
    set1 = []
    set2 = []
    set3 = []
    for question in questions:
        if question.id <= 7:
            set1.append(question)
        if  8 <= question.id <= 14:
            set2.append(question)
        if  15 <= question.id <= 22:
            set3.append(question)
        print(set3)
        # while 7 < question.id < 14:
        
    learnerCentricity = set1
    # learnerCentricity = Question.query.filter_by(skillGroup = "Learner Centricity").all()
    teachingForRecall = set2
    # teachingForRecall = Question.query.filter_by(skillGroup = "Teaching for Recall").all()
    teachingForEngagement = set3
    # teachingForEngagement = Question.query.filter_by(skillGroup = "Teaching for Engagement").all()
    totalquestions = len(questions)
    return render_template('forms.html', questions = questions, totalquestions=totalquestions, learnerCentricity=learnerCentricity, teachingForRecall=teachingForRecall, teachingForEngagement=teachingForEngagement )

@app.route('/admin')
def admin():
    questions = Question.query.all()
    totalquestions = len(questions)
    return render_template('admin.html', questions = questions, totalquestions = totalquestions)

@app.route('/admin/questions')
def adminquestions():
    questions = Question.query.all()
    print(questions)
    return render_template('questions.html', questions = questions)

@app.route('/admin/addquestion', methods=['GET','POST'])
def addquestion():
    form = Questions()
    if form.validate_on_submit():
        new_question = Question(question=form.question.data, skillGroup = form.skillGroup.data, q_number=form.q_number.data, component =form.component.data )
        db.session.add(new_question)
        db.session.commit()
        print("It submits")
        return redirect (url_for('admin'))
    return render_template('addaquestion.html', form=form)

def send_sms(phone,message):
    params = {"key":'aniXLCfDJ2S0F1joBHuM0FcmH',"to":phone,"msg":message,"sender_id":'PrestoSL'}
    url = 'https://apps.mnotify.net/smsapi?'+ urllib.parse.urlencode(params)
    content = urllib.request.urlopen(url).read()
    print (content)
    print (url)

@app.route('/newreport', methods=['GET','POST'])
def newreport():
    code = "ajlsbdf312wiubc"
    message = 'Your clearance code is: ' + code
    # send_sms('0545977791', message) 
    return render_template('newreport.html')

# @app.route("/sendMail")
# def index():
#    print("Initiating sending mail")
#    msg = Message('Hello', sender = 'mr.adumatta@gmail.com', recipients = ['dev.lecturesoft@gmail.com'])
#    msg.body = "Hello Flask message sent from Flask-Mail"

#    print(msg)
#    mail.send(msg)
#    return "Sent"

@app.route('/forex')    
def forex():
    url = "https://api.apilayer.com/currency_data/convert?to=GBP&from=USD&amount=5"

    payload = {}
    headers= {
    "apikey": "KggjPZDWQHGB8eHxmWefEkeH1JiKUogx"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    print(result)
    return result

dict = {}

@app.route('/restartForm')
def restartForm():
    session['qNumber'] = 1
    dict = {}
    return redirect('exitform')

@app.route('/reverseForm')
def reverseForm():
    session['qNumber'] = int(session['qNumber']) - 1
    return redirect('exitform')

@app.route('/exitform', methods=['GET', 'POST'])
def exitform():
    if session['qNumber']:
        print("Found a session")
    else:
        session['qNumber'] = 1

    currentQuestion = session['qNumber']
    print(session['qNumber'])
    allQuestions = Question.query.all()
    rows = len(allQuestions)
    
    currentQuestionPercentage = currentQuestion/rows
    percentage = str(round(currentQuestionPercentage*100)) + '%' 
    print(percentage)

    if percentage == '100%':
        # session['qNumber'] = 1
        # sendSms to number
        # send_sms("0545977791", "Thank you for filling the Graduate Form. Your clearance code is PRXX2345923. Please use this to ensure you are cleared successfully.")
        print(dict)
        formattedDict = str(dict).replace("},", " } \n")
        sendtelegram(formattedDict)
        session['qNumber'] = 1
        # dict = {}
        return redirect('landing')

    question = Question.query.get_or_404(session['qNumber'])
    if request.method == 'POST':
        answer = request.form.get('answer')
        dict[question.id] = {
            "question":question.question,
            "answer":answer
        }
        print(dict)
        session['qNumber'] = currentQuestion + 1
        print(dict)
        formattedDict = str(dict).replace("},", " } \n")
        print(formattedDict)
    return render_template('designForm.html', question=question, currentQuestion=currentQuestion, allQuestions=allQuestions, percentage=percentage)

@app.route('/report', methods=['GET','POST'])
def report():
    # send_mail()
    forMail = []
    mailBody = ''
    questions = Question.query.all()
    totalquestions = len(questions)
    score = 0
    muchwork = []
    attention = []
    fair = []
    strengths = []
    teachingForRecall = []
    learnerCentricity = []
    teachingForEngagement = []

    for i in questions:
        # questionId is the question id
        questionId = str(i.id)
        # name is the point for each question
        point = int(request.form[ questionId ])
        # This picks the point you scored for each question and makes it an integer for a specific time
        score = score + point
        print(score)
        print("Component " + i.question)
        print(i.skillGroup + " - " + str(point))


        mailBody += str(i.id) + " - " + i.question + " - " + str(point) + "\n"
        # forMail.append(str(i.id) + " - " + i.question + "  " )
        if 3 <= point <= 4:
            print("Appending Strengths")
            if not i.component in strengths:
                print("Item is in array already.")
                strengths.append(i.component)
        if point == 1:
            print("Needs Much Work")
            if not i.component in muchwork:
                muchwork.append(i.component)    
        if point == 2:
            print("Appending Fair")
            if not i.component in fair:
                fair.append(i.component)
        if point == 0:
            print("Much attention Needed")
            if not i.component in attention:
                attention.append(i.component)

        # Fill the skillGroup for calculations
        if (i.skillGroup) == "Learner Centricity":
            learnerCentricity.append(point)
            print("This is a Learner Centricity Component with a total of ")
        if (i.skillGroup) == "Teaching for Recall":
            print("This is a Teaching for Recall Component")
            teachingForRecall.append(point)
        if (i.skillGroup) == "Teaching for Engagement":
            print("This is a Teaching for Engagement Component")
            teachingForEngagement.append(point)

    print("Score = " + str(score))
    total = totalquestions*4
    print("Total = " + str(total))
    percent = (score/total)
    print("Your percent" + str(percent))
    percentage = round(percent * 100)
    print(str(percentage) + "%")
    print("Your Skill was " + skill(12))
    skills = skill(percentage)
    print("Your Strengths = " + str(strengths))
    print("Attention needed = " + str(attention))
    print("Fair Skills = " + str(fair))
    print("++++++++++++++++++++++++")
    learnerCentricityTotal = findTotal(learnerCentricity)
    teachingForRecallTotal = findTotal(teachingForRecall)
    teachingForEngagementTotal = findTotal(teachingForEngagement)
    print(learnerCentricityTotal)
    print(teachingForRecallTotal)
    print(teachingForEngagementTotal)
    firstname = session['firstname']
    lastname = session['lastname']
    phone = session['phone']
    email = session['email']
    course = session['course']

    # params = "New Account Created for " + new_user.username

    print("This is sending to the mail " + str(forMail))
    msgbody = "You have recieved a new entry from " + firstname + " " + lastname + "\n" + " Email: " + email + "\n" + ". Phone: " + phone + "\n"  + ". Course: " + course  +"\n"+ str(mailBody)
    # sendmail(msgbody)
    sendtelegram(msgbody)
    cleanfair = str(fair)


    # send_sms('aniXLCfDJ2S0F1joBHuM0FcmH','0545977191',msgbody,'PrestoSL')
    return render_template('newreport.html', percentage = percentage, skills=skills, 
    strengths=(str(strengths).replace( '[' , '').replace( ']' , '').replace( "'" , '')), 
    attention=(str(attention).replace( '[' , '').replace( ']' , '').replace( "'" , '')), 
    muchwork=(str(muchwork).replace( '[' , '').replace( ']' , '').replace( "'" , '')), 
    fair=(str(fair).replace( '[' , '').replace( ']' , '').replace( "'" , '')), 
    learnerCentricityTotal=learnerCentricityTotal, teachingForRecallTotal=teachingForRecallTotal, teachingForEngagementTotal=teachingForEngagementTotal)

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000,debug=True)