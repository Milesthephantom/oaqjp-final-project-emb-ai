import requests

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
        return response.json().get('text', 'No text in response')
    else:
        return f"Error: {response.status_code}, {response.text}"
      from emotion_detection import emotion_detector
result = emotion_detector("I love this new technology.")
print(result)

