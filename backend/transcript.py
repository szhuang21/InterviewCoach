from hume import HumeBatchClient
from hume.models.config import LanguageConfig

import json

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
files = ["/Users/prachideo/Desktop/AI_Hackathon/InterviewCoach/backend/test_videos/talk_video.mov"]
urls = None
config = LanguageConfig()
job = client.submit_job(None, [config], files = files)

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("test_lang_predictions.json")
print("Predictions downloaded to test_lang_predictions.json")

with open('test_lang_predictions.json') as file:
    data = json.load(file)

transcript = []
emotions_all = {}

video = data[0]["results"]["predictions"]
# Iterate over each frame in the video data
for vid in video:
    predictions = vid['models']['language']['grouped_predictions'][0]['predictions']

    for prediction in predictions:
        transcript.append(prediction['text'])
        emotions = prediction['emotions']

        for emotion in emotions:

            emotion_name = emotion['name']
            emotion_score = emotion['score']

            emotions_all[emotion_name] = emotions_all.get(emotion_name, []) + [emotion_score]

# Calculate the average scores for each emotion
average_emotions = {}
for emotion, scores in emotions_all.items():
    average_score = sum(scores) / len(scores)
    average_emotions[emotion] = average_score

top_emotions = sorted(average_emotions.items(), key=lambda x: x[1], reverse=True)[:5]

for emotion, score in top_emotions:
    print(f"{emotion}: {score}")


print(transcript)