from flask import Flask, request, jsonify, make_response
from sender import send_email

app = Flask(__name__)

@app.route("/v1/sender", methods=["POST"])
def olaMundo():

  to = request.json['to']
  subject = request.json['subject']
  emailBody = request.json['body']

  email =  send_email(subject, emailBody, to)

  return responseGenerator(200,"Email send sucecifully","send to", to, "subject",subject,"email body", emailBody)


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
    
if(app):
    print("server read to go")

app.run(debug=True)