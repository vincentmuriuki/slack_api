# this sets up an ongoing webhook that will alert our python application via an HTTP POST request.
# we need to receive one or more POST requests
# we'll need a simple web server that can handle an inbount POST request from  from the Slack webhook
import os

from flask import Flask, request, Response


app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = requst.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200



@app.route('/', methods=['GET'])
def test():
    return Response('It works!')



if __name__ == '__main__':
    app.run(debug=True)


# 1. import Flask
# 2. Instantiate a new Flask application context
# 3. Pull in the SLACK_WEBHOOK_SECRET environment variable, which we get in just a moment from the Slack console
# 4. Establish a route that can receive an HTTP POST request from Slack that printsbthe output to the command line as long as the webhook secret key sent to us matches one from our environment variable
# 5. create another route for testing purposes thet responds to a GET request
# 6. set our Flask app to run when we run the script with Python
