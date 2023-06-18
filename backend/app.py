from flask import Flask, request, jsonify
# from report import generate_report
from chatgpt import generate_question
from report import generate_better_response
from report import videoToEmotions, getTranscript, generate_better_response, generate_graph
import json
from flask_cors import CORS
import flask

# Starts Flask connection
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'


# @app.route('/getInterviewQuestion', methods=['POST'])
# def get_interview_question():
#     print("line 20")
#     print("request: ", request)
#     if not request:
#         return 'no request found', 400
    
#     data = request.get_data()
#     response = flask.jsonify({'some': 'data'})
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response 
#     # age = data["age"]
#     # role = data["role"]
#     # question = generate_question(age, role)
#     # return {'response': '200',
#     #     'question': question
        
#     # }

@app.route('/getInterviewQuestion', methods=['POST'])
def get_interview_question():
    print("line 41")
    data = request.get_json()
    print("line 43")
    age = data.get('age')
    print("line 45")
    role = data.get('role')

    if not age or not role:
        return 'Invalid request body', 400

    question = generate_question(age, role)

    return question

# /getReport is a test endpoint
@app.route('/getReport', methods=['POST'])
def get_report():
    if not request:
        return 'no request found', 400
    
    data = request.get_data()
    zip_url = data.decode('utf-8')
    top_positive_emotions,  top_negative_emotions = videoToEmotions(zip_url)
    return {'response': '200',
        'top_positive_emotions': top_positive_emotions,
        'top_negative_emotions': top_negative_emotions,
    }

# /getReport is a test endpoint
@app.route('/getFullReport', methods=['POST'])
def get_full_report():
    print("line 33")
    if not request:
        return 'no request found', 400
    print("line 36")
    data = request.get_data()
    zip_url = data.decode('utf-8')
    print("line 38")
    top_visual_positive_emotions,  top_visual_negative_emotions = videoToEmotions("WIN_20230618_13_22_38_Pro.mp4")
    print("line 41")
    graph = generate_graph(zip_url)
    print("line 43")
    graph_json = json.loads(graph.to_json())
    print("line 43")
    return {'response': '200',
        'top_visual_positive_emotions': top_visual_positive_emotions,
        'top_visual_negative_emotions': top_visual_negative_emotions,
        'graph': graph_json, 
        
    }
    # top_verbal_positive_emotions,  top_verbal_negative_emotions = wordToEmotions(zip_url)
    # transcription = getTranscript(zip_url)
    # suggestions = generate_better_response(zip_url)

    # return {'response': '200',
    #     'top_visual_positive_emotions': top_visual_positive_emotions,
    #     'top_visual_negative_emotions': top_visual_negative_emotions,
    #     'top_verbal_positive_emotions': top_verbal_positive_emotions,
    #     'top_verbal_negative_emotions': top_verbal_negative_emotions,
    #     'transcription': transcription, 
    #     'suggestions': suggestions 
    # }

@app.route('/generateBetterResponse')
def get_better_response():
    response = generate_better_response("What is your biggest weakness?", "i am stupid", 20, "software engineer")
    return response


if __name__ == '__main__':
    app.run()
