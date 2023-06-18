from hume import HumeBatchClient
from hume.models.config import FaceConfig
import json
# import constants

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
files = ["backend/media/filler-words.mov"]
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


# import requests
# from hume import HumeBatchClient
# from hume.models.config import FaceConfig
# from hume.models.config import LanguageConfig
# from hume.models.config import BurstConfig
# import os

# # # Increase the timeout value to a higher value (e.g., 30 seconds)
# # timeout = 30

# # client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24", timeout=timeout)
# client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
# cwd = os.getcwd()
# #urls =
# # files = ["/Users/sophiazhuang/Desktop/InterviewCoach/InterviewCoach/backend/media/filler-words.mov"] #["https://hume-tutorials.s3.amazonaws.com/faces.zip"]
# files = ["https://hume-tutorials.s3.amazonaws.com/faces.zip"]
# config = LanguageConfig()
# job = client.submit_job(None, [config], files=files)

# print(job)
# print("Running...")

# details = job.await_complete()

# predictions = job.get_predictions()
# for result in predictions:
#     transcription = result["output"]["transcription"]
#     print("Transcription:", transcription)

# job.download_predictions("test_lang_predictions.json")
# print("Predictions downloaded to test_lang_predictions.json")
