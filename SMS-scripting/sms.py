from twilio.rest import Client

account_sid = 'AC660aae0d8ca227d3dce65aa9f2f41a5d'
auth_token = 1 #auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15614751176',
  body='helloooooo',
  to='************'
)

print(message.sid)