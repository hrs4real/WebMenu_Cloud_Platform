#!/usr/bin/python3
import cgi
import json
import openai
import time
# Set the appropriate headers for a CGI script
print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")

print()

# Get the user's message from the request
form = cgi.FieldStorage()
user_message = form.getvalue('message')
openai.api_key = 'YOUR_OPENAI_API_KEY'
# Generate response using OpenAI GPT-3
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=user_message,
    max_tokens=50,
    temperature=1.2,
    n=1,
    stop=None
)
print("<pre><h3>")
print(response["choices"][0]["text"])
print("<h3></pre>")