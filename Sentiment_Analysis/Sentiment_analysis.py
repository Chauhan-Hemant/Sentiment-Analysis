import tkinter as tk
from tkinter import *
from textblob import TextBlob


def get_sentiment(text):
    """
    Function to get sentiment analysis
    """
    blob = TextBlob(str(text))
    polarity = blob.polarity
    if polarity == 0:
        sentiment = 'Neutral'
    elif polarity > 0:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
    return sentiment


def print_sentiments(df):
    """
    Function to print sentiment
    """
    sentiments = []
    for i in df:
        sentiment = get_sentiment(i)

        sentiments.append({
            'text': i,
            'sentiment': sentiment
        })

    neutral, positive, negative = 0, 0, 0
    for info in sentiments:
        if info['sentiment'] == 'Neutral':
            neutral += 1
        elif info['sentiment'] == 'Positive':
            positive += 1
        elif info['sentiment'] == 'Negative':
            negative += 1

    count = neutral + positive + negative
    neutral = (neutral / count) * 100
    positive = (positive / count) * 100
    negative = (negative / count) * 100

    sentiment_result = Label(result_frame,
                             text=str(f"Positive : {positive} %\nNeutral  : {neutral} %\nNegative : {negative} %"))
    sentiment_result.pack()


def getTextInput():
    """
    Function to take the input from the textbox
    """
    result = [text.get('1.0', 'end')]
    result_label = Label(result_frame, text=str("Sentiments of the Above entered text : "))
    result_label.pack()
    print_sentiments(result)


def clearText():
    """
    Function to clear the textbox and output section
    """
    text.delete('1.0', 'end')
    for widget in result_frame.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Sentiment Analysis")

Label(root, text="Enter Text for Sentiment Analysis", padx=25, pady=10, font=("", 15), fg='green').pack()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root)
text.pack()

text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

submit_btn = Button(root, text='Get Sentiment', fg='green', command=getTextInput)
submit_btn.pack(padx=25, pady=10)

reset_button = Button(root, text="Clear", fg='red', command=clearText)
reset_button.pack(padx=25, pady=10)

result_frame = Frame(root, bg='white')
result_frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.7)

root.minsize(800, 800)
root.mainloop()
