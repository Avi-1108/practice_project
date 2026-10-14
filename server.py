'''
Import the relevant libraries and functions 
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyzes the input text provided via request parameters for emotional content.

    Retrieves the string payload from the query parameter 'textToAnalyze',
    processes it through the emotion detector library, and formats a human-readable 
    summary of the emotional breakdown alongside the identified dominant emotion.

    Returns:
        str: A formatted sentence detailing all emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        print("Invalid text! Please try again!.")

    else:
        print(
            f"For the given statement, the system response is 'anger': {anger_score},"
            f" 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy':"
            f" {joy_score} and 'sadness': {sadness_score}. The dominant emotion is"
            f' {dominant_emotion}.'
        )

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application interface.

    This function triggers on the root web path URL ('/') and serving the 
    front-end interface 'index.html' template to the user's browser.

    Returns:
        str: The rendered HTML content of the application index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
