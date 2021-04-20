# twilio-chat-poc

Proof of concept chat application using the Twilio API.

Implementation is based on the following resources:
1. Building a Django Twilio Programmable Chat Application, Michael Jenkins: https://www.twilio.com/blog/2018/03/python-django-twilio-programmable-chat-application.html.

2. How to Build Chat into Django Applications with Twilio Programmable Chat, Kevin Ndung'u: https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html

3. Build a Video Chat Application with Python, JavaScript and Twilio Programmable Video, Miguel Grinberg: https://www.twilio.com/blog/build-video-chat-application-python-javascript-twilio-programmable-video

## Feature list and to-dos

What works:

1. Basic text chatting

2. Basic video chatting

To be done: 

1. Voice chat

2. Landing page for choosing chat type


## Setup

1. Clone the project

```
git clone https://github.com/rishmanisation/twilio-chat-poc
```

2. Check if you have virtualenv installed using the version command. If not, install it and then create a new virtual environment. Then, install the 
project dependencies inside the virtual environment.

```
virtualenv --version
python -m pip install virtualenv
virtualenv my_env
source ./my_env/bin/activate
python -m pip install -r requirements.txt
```

3. Sign up for a free developer account at http://www.twilio.com, follow the onboarding steps to create a project and then locate the following information:

    a. Account SID: This will be under project information section in the dashboard.

    b. Chat Service SID: Click the “Programmable Chat” button or browse to https://www.twilio.com/console/chat/dashboard. On the Programmable Chat Dashboard, click the red plus sign to create a new chat service.  Give your chat app service a name. Under the Base Configuration, find the “Chat Service SID”.

    c. Sync SID: Navigate to the "Sync Services" page and click on the default service. Use the SID as the Sync SID.

    d. API SID and API Secret: Navigate to the "API Keys" page and create a new key.

Create a file called .env in the home directory and add the collected information as follows:

```
TWILIO_ACCT_SID='<Account SID>'
TWILIO_CHAT_SID='<Chat Service SID>'
TWILIO_SYNC_SID='<Sync SID>'
TWILIO_API_SID='<API SID>'
TWILIO_API_SECRET='<API Secret>'
```

4. Run the migrations and then start the server. Open your browser and navigate to http://127.0.0.1:8080/chat.

```
python manage.py migrate OR honcho run ./manage.py migrate
python manage.py runserver OR honcho run ./manage.py runserver
```

### BELOW STEPS ARE FOR VIDEO CHAT ONLY

5. Video chat works only over HTTPS. Hence, we need to set up ngrok prior to running our code. Install ngrok from https://www.ngrok.io and unzip the file. Then, navigate to the directory you unzipped the file to and run

```
./ngrok http 8000
```

6. Copy the https FQDN and paste it into APPROVED_HOSTS in settings.py.

7. You can now start the server as described above. Once done, open the URL and navigate to https://\<ngrok FQDN>/video. Sign in using your name, then open the URL on another device and sign in again.

