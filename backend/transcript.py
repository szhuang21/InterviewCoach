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

video = data[0]["results"]["predictions"]
# Iterate over each frame in the video data
for vid in video:
    predictions = vid['models']['language']['grouped_predictions'][0]['predictions']

    for prediction in predictions:
        transcript.append(prediction['text'])

print(transcript)