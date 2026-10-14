'''
Import the relevant libraries and functions 
'''

from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# pylint: disable=missing-function-docstring
def my_undocumented_function():
    pass

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)
    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        print("Invalid input! Try again.")
    else:
        # Return a formatted string with the sentiment label and score
        print(f"The given text identified as {label.split('_')[1]} with a score of {score}")


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
