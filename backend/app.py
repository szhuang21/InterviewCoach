from flask import Flask
# from report import generate_report
from report import generate_better_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

# @app.route('/getReport', methods=['POST'])
# def get_report():
#     video = request.files['video']
#     # Assuming generate_report function accepts a file path as a parameter
#     video.save('temp_video.mp4')  # Save the uploaded video as a temporary file
#     report = generate_report('temp_video.mp4')
#     # Process the report or return it as a response
#     return report

@app.route('/generateBetterResponse')
def get_better_response():
    response = generate_better_response("What is your biggest weakness?", "i am stupid", 20, "software engineer")
    return response


if __name__ == '__main__':
    app.run()
