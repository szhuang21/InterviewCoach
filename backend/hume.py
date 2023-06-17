from hume import HumeBatchClient
from hume.models.config import FaceConfig

client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
urls = ["https://hume-tutorials.s3.amazonaws.com/faces.zip"]
config = FaceConfig()
job = client.submit_job(urls, [config])

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")