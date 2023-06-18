from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import LanguageConfig

import json
import constants

import os
import openai

def videoToEmotions(video):
    client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
    files = [video]
    config = FaceConfig()
    job = client.submit_job(None, [config], files = files)

    # print(job)
    # print("Running...")

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



def wordsToEmotion(video):
    client = HumeBatchClient("HYNdEFrlFnYpEUJAcUfaKYf8Or8qMyIo3IFzuAQBlcFGiE24")
    # files = ["/Users/prachideo/Desktop/AI_Hackathon/InterviewCoach/backend/test_videos/talk_video.mov"]
    files = [video]
    config = LanguageConfig()
    job = client.submit_job(None, [config], files = files)

    # print(job)
    # print("Running...")

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

    return transcript, top_positive_emotions, top_negative_emotions


    # print("Top 5 Positive Emotions:")
    # for emotion, score in top_positive_emotions:
    #     print(f"{emotion}: {score}")

    # print("\nTop 5 Negative Emotions:")
    # for emotion, score in top_negative_emotions:
    #     print(f"{emotion}: {score}")


    # print(transcript)

def generate_better_response(question, response, age, role):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Can you make this message sound more natural and human-like (speak like you would to an interviewer, not too many big words), clear, concise, and confident to pass an interivew: {response}."},
            {"role": "system", "content": f"You are a {age} year old interviewing for a position in {role} answering the interview question: {question}"}
        ]
    )

    better_response = completion.choices[0].message.content
    print(better_response)
    return better_response