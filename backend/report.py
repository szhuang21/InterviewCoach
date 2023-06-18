# import speech_recognition as sr
# from os import path
# from pydub import AudioSegment

# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("transcript.mp3")
from hume import TranscriptionConfig
from hume import HumeBatchClient
from hume.models.config import ProsodyConfig
import json

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
files = ["media/compressed.mp4"]
urls = None
config = ProsodyConfig()
print(config)

job = client.submit_job(None, [config], files = files)

print(job)
print("Running...")

details = job.await_complete()

# Retrieve predictions from job
full_predictions = job.get_predictions()
print("full_predictions: ", full_predictions)
job.download_predictions("predictions.json")

# # Extract relevant predictions
# predictions = full_predictions[0]['results']['predictions'][0]['models']['prosody']['grouped_predictions'][0]['predictions'][0]
# print("predictions: ", predictions)


# transcription = predictions['text']
# print("transcription: ", transcription)

# job.download_predictions("predictions.json")
# # print("details: ", job.get_details())
# print("Predictions downloaded to predictions.json")

# with open('predictions.json', 'r') as file:
#     data = json.load(file)

