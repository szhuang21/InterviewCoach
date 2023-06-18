from hume import HumeBatchClient
from hume.models.config import LanguageConfig

import json
import constants

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
# files = ["/Users/prachideo/Desktop/AI_Hackathon/InterviewCoach/backend/test_videos/talk_video.mov"]
files = ["/Users/kelsi/OneDrive/Pictures/Camera Roll/WIN_20230617_20_30_35_Pro.zip"]
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
positive_emotions = {}
negative_emotions = {}

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

            if emotion_name in constants.positive_emotions_language:
                positive_emotions[emotion_name] = positive_emotions.get(emotion_name, []) + [emotion_score]
            elif emotion_name in constants.negative_emotions_language:
                negative_emotions[emotion_name] = negative_emotions.get(emotion_name, []) + [emotion_score]


# Calculate the average scores for each emotion
average_positive_emotions = {}
for emotion, scores in positive_emotions.items():
    average_score = sum(scores) / len(scores)
    average_positive_emotions[emotion] = average_score

average_negative_emotions = {}
for emotion, scores in negative_emotions.items():
    average_score = sum(scores) / len(scores)
    average_negative_emotions[emotion] = average_score

sorted_positive_emotions = sorted(average_positive_emotions.items(), key=lambda x: x[1], reverse=True)
sorted_negative_emotions = sorted(average_negative_emotions.items(), key=lambda x: x[1], reverse=True)
top_positive_emotions = sorted_positive_emotions[:5]
top_negative_emotions = sorted_negative_emotions[:5]


print("Top 5 Positive Emotions:")
for emotion, score in top_positive_emotions:
    print(f"{emotion}: {score}")

print("\nTop 5 Negative Emotions:")
for emotion, score in top_negative_emotions:
    print(f"{emotion}: {score}")


print(transcript)