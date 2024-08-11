import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if the response is successful
    if response.status_code == 200:
        response_dict = response.json()  # Convert response text to dictionary
        
        # Extract scores for the required emotions
        emotions = {
            'anger': response_dict.get('anger', 0),
            'disgust': response_dict.get('disgust', 0),
            'fear': response_dict.get('fear', 0),
            'joy': response_dict.get('joy', 0),
            'sadness': response_dict.get('sadness', 0)
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Return the desired output format
        return {
            **emotions,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'error': f"Error: {response.status_code}, {response.text}"
        }
import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL and headers for the request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define the payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Handle the status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert response to dictionary
    response_data = response.json()

    # Extract emotions and determine dominant emotion
    anger = response_data.get('anger', 0)
    disgust = response_data.get('disgust', 0)
    fear = response_data.get('fear', 0)
    joy = response_data.get('joy', 0)
    sadness = response_data.get('sadness', 0)
    dominant_emotion = response_data.get('dominant_emotion', '')

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
