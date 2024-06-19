from transformers import pipeline

# Creating the Sentiment Analysis Pipeline: This means that the pipeline will use a default model for sentiment analysis.
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

response = classifier("I'm sad that Bunny encountered a bug")

print(response)
