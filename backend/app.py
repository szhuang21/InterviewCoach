from flask import Flask, request
# from report import generate_report
from report import generate_better_response
from report import videoToEmotions, getTranscript, generate_better_response, generate_graph
import json
from flask_cors import CORS

# Starts Flask connection
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

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
