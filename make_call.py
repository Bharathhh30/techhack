import os
from twilio.rest import Client
from pyngrok import ngrok

# Load ngrok configuration from file
ngrok.set_auth_token("2iXWagsnReYrk3koiGdh5L4ccPC_3a1QdhdzMBEvSGH8aQvD1")  # Replace with your ngrok authentication token

# Start ngrok with the named tunnel configuration
ngrok_tunnel = ngrok.connect("my_tunnel")  # Assuming ngrok.yml is in the default location

print(f"Public URL: {ngrok_tunnel.public_url}")

# Your Twilio credentials
account_sid = "ACd5ada1cf185906febfefb5952b0b6c6d"
auth_token = "1ea13df02355b249025f183ad4ecabdd"
client = Client(account_sid, auth_token)

# Create Twilio call
call = client.calls.create(
    from_="+15188752962",
    to="+918919162757",
    url=f"{ngrok_tunnel.public_url}/voice",
)

print(call.sid)
