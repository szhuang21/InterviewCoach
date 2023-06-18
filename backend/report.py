from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import LanguageConfig
from hume.models.config import BurstConfig
import os

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
cwd = os.getcwd()
#urls =
files = ["/Users/prachideo/Desktop/AI_Hackathon/InterviewCoach/backend/test_videos/vocal_vid.mov"] #["https://hume-tutorials.s3.amazonaws.com/faces.zip"]
config = LanguageConfig()
job = client.submit_job(None, [config], files=files)


print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("test_lang_predictions.json")
print("Predictions downloaded to test_lang_predictions.json")
