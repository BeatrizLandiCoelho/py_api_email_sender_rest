from flask import Flask, request, jsonify, make_response
from sender import send_email

app = Flask(__name__)

@app.route("/v1/sender", methods=["POST"])
def olaMundo():

    
  to = request.json['to']
  subject = request.json['subject']
  emailBody = request.json['body']

  email =  send_email(subject, emailBody, to)

  return {"Email sent successfully.":"a"}



if(app):
    print("server read to go")

app.run(debug=True)