from flask import Flask, request, jsonify , Response
from twilio.twiml.voice_response import VoiceResponse   
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/voice', methods=['GET','POST'])
def voice():
    resp = VoiceResponse()
    resp.say("Hello, this is a customized message from Twilio!", voice='alice')
    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
