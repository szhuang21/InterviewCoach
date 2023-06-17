import os
import openai
openai.api_key = "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"
# openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)