import firebase_admin
from firebase_admin import credentials, messaging

config = {
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email" : "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
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
