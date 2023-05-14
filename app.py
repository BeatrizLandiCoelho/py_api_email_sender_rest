from flask import Flask, request, jsonify, make_response
from sender import send_email

app = Flask(__name__)

#_______________________________________________________________________#

@app.route("/v1/sender", methods=["POST"])
def emailSender():

  to = request.json['to']
  subject = request.json['subject']
  emailBody = request.json['body']

  if(to == '' or subject == '' or emailBody == ''):
        return responseGenerator(400,"all parameters are mandatory")
  

  send_email(subject, emailBody, to)

  return responseGenerator(200,"Email send sucecifully",
                           "send to", to, 
                           "subject",subject,
                           "email body", emailBody)

#_______________________________________________________________________#

def responseGenerator(status, message, 
                      email_reciver = False, reciver = False,
                      email_subject = False , subject = False,
                      email_body = False, body = False):
    
    response ={}
    response["status"]= status
    response["message"] = message

    if(email_reciver and reciver 
        and email_subject and subject ):
        response[email_reciver] = reciver
        response[email_subject] = subject
        response[email_body] = body

    return jsonify(response) 
#_____________________________________________________________________________#
if(app):
    print("server read to go")

app.run(debug=True)