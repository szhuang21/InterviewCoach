from hume import HumeBatchClient
from hume.models.config import ProsodyConfig

import json

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
files = ["/Users/prachideo/Desktop/AI_Hackathon/InterviewCoach/backend/test_videos/talk_video.mov"]
urls = None
config = ProsodyConfig()
job = client.submit_job(None, [config], files = files)

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("test_prosody_predictions.json")
print("Predictions downloaded to test_prosody_predictions.json")