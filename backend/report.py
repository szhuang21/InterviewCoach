from hume import HumeBatchClient
from hume.models.config import FaceConfig

import json

import constants


def videoToEmotions(video):
    client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
    files = [video]
    config = FaceConfig()
    job = client.submit_job(None, [config], files = files)

    print(job)
    print("Running...")

    details = job.await_complete()
    job.download_predictions("predictions.json")
    print("Predictions downloaded to predictions.json")



    with open('predictions.json') as file:
        data = json.load(file)

    # Initialize dictionaries to store positive and negative emotions
    positive_emotions = {}
    negative_emotions = {}

    video = data[0]["results"]["predictions"]
    # Iterate over each frame in the video data
    for vid in video:
        predictions = vid['models']['face']['grouped_predictions'][0]['predictions']
        
        # Iterate over each prediction in the frame
        for prediction in predictions:
            emotions = prediction['emotions']

            
            # Iterate over each emotion in the prediction
            for emotion in emotions:
                emotion_name = emotion['name']
                emotion_score = emotion['score']
                
                # Check if the emotion is positive or negative
                if emotion_name in constants.positive_emotions_other:
                    positive_emotions[emotion_name] = positive_emotions.get(emotion_name, []) + [emotion_score]
                elif emotion_name in constants.negative_emotions_other:
                    negative_emotions[emotion_name] = negative_emotions.get(emotion_name, []) + [emotion_score]


    # Calculate the average scores for each positive emotion
    average_positive_emotions = {}
    for emotion, scores in positive_emotions.items():
        average_score = sum(scores) / len(scores)
        average_positive_emotions[emotion] = average_score


    # Calculate the average scores for each negative emotion
    average_negative_emotions = {}
    for emotion, scores in negative_emotions.items():
        average_score = sum(scores) / len(scores)
        average_negative_emotions[emotion] = average_score

    # Sort the average positive emotions by score (descending order)
    sorted_positive_emotions = sorted(average_positive_emotions.items(), key=lambda x: x[1], reverse=True)

    # Sort the average negative emotions by score (descending order)
    sorted_negative_emotions = sorted(average_negative_emotions.items(), key=lambda x: x[1], reverse=True)

    # Get the top 5 positive emotions
    top_positive_emotions = sorted_positive_emotions[:5]

    # Get the top 5 negative emotions
    top_negative_emotions = sorted_negative_emotions[:5]

    return top_positive_emotions, top_negative_emotions

    # print("Top 5 Positive Emotions:")
    # for emotion, score in top_positive_emotions:
    #     print(f"{emotion}: {score}")

    # print("\nTop 5 Negative Emotions:")
    # for emotion, score in top_negative_emotions:
    #     print(f"{emotion}: {score}")
