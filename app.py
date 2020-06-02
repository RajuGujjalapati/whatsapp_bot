#below code creates a folder name called 'myven'
#################python -m venv myvenv###########
#below code helps to activate
###############myvenv\Scripts\activate############
#create a python files by going into 'myven' folder
#######touch ap.py###-->if that file exists opens , if not create

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])#only accepts post requests 
def sms_reply():#call back url,send mesages using this url.sms is the root which takes messages and then sends sms.
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)
    # Create reply
    resp = MessagingResponse()
    if msg == 'Hi':
       resp.message("poora edava")
    else:
         resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
#we are created local host url , no one can see except me.
    #now we can deploy our project in aws, and other servers , so that when we
    #deploy main url in twilio website, it runs forever
    #for temperory purpose, iam using ngrok webiste(allows us to tunnel froma
    #public URL to our application running locally
#unzip the unrok file which we have downloaded and then goto that file(folder) in 'cmd'
    #ngrok.exe http port number(in this case 5000)
#after then we will get link and it runs on any system.
    
#and it have time session which is upto 7-8 hrs

#twilio direct link:https://www.twilio.com/console/sms/whatsapp/sandbox
#give the 'ngrok' link to twilio 'WHEN THE MESSAGE COMES IN'.and add 'https://6fbf6ffa.ngrok.io/sms'
   # after every succesful mesage see in cmd it shows status code.
    
