from hume import HumeBatchClient
from hume.models.config import FaceConfig

import json

import constants

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
files = ["Screenshot 2023-06-17 170731.png"]
urls = None
config = FaceConfig()
job = client.submit_job(None, [config], files = files)

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")


with open('predictions.json', 'r') as file:
    data = json.load(file)

# Get the predictions
predictions = data[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions']
emotions = predictions[0]['emotions']

# Sort the emotions based on their scores in descending order
sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)


# Get the top 5 positive emotions
top_5_positive_emotions = [emotion['name'] for emotion in sorted_emotions if emotion['name'] in constants.positive_emotions_other][:5]
top_5_positive_scores = [emotion['score'] for emotion in sorted_emotions if emotion['name'] in constants.positive_emotions_other][:5]


# Get the top 5 negative emotions
top_5_negative_emotions = [emotion['name'] for emotion in sorted_emotions if emotion['name'] in constants.negative_emotions_other][:5]
top_5_negative_scores = [emotion['score'] for emotion in sorted_emotions if emotion['name'] in constants.negative_emotions_other][:5]


# Print the top 5 positive emotions
print("Top 5 Positive Emotions:")
for i in range(5):
    print(top_5_positive_emotions[i], top_5_positive_scores[i])

print()
# Print the top 5 negative emotions
print("Top 5 Negative Emotions:")
for i in range(5):
    print(top_5_negative_emotions[i], top_5_negative_scores[i])