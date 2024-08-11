from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.json
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)
    
    # Format the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )
    
    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
curl -X POST http://localhost:5000/emotionDetector -H "Content-Type: application/json" -d '{"text": "I think I am having fun"}'
