import firebase_admin
from firebase_admin import credentials, messaging

config = {
  "type": "service_account",
  "project_id": "fishtankapp-88d91",
  "private_key_id": "xxxxxxxxxxx",
  "private_key": "private key"
  "client_email": "firebase-adminsdk-rtm0h@fishtankapp-88d91.iam.gserviceaccount.com",
  "client_id": "100500891628555041108",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rtm0h%40fishtankapp-88d91.iam.gserviceaccount.com"
}
cred = credentials.Certificate(
    "/home/pi/Final Codes/firebase_cloud_msg/keys.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
