import os
import openai
openai.api_key = "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"

def generate_better_response(question, response, age, role):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Can you make this message sound more natural, clear, concise, and confident to pass an interivew: {response}."},
            {"role": "system", "content": f"You are a {age} year old answering the interview question: {question}"}
        ]
    )

    better_response = completion.choices[0].message.content
    print(better_response)
    return better_response

# generate_better_response("How do you think you are at skateboarding", "I think I am okay at skateboarding.", 18, "software engineering")
generate_better_response("What is your greatest weakness", "Unorganized", 18, "software engineering")