from flask import Flask, render_template, request
import pinecone
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from tqdm.auto import tqdm
import re

df = pd.read_csv("covid19_tweets_new.csv")

# Initialize Pinecone
pinecone.init(api_key="<YOUR-API-KEY>", environment="<YOUR-API-ENVIRONMENT>")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModel.from_pretrained("gpt2")

# A function to encode text into vector
def encode_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    if len(inputs) > 512:
        inputs = inputs[:512]
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

index_pine = pinecone.Index("semantic-search")

# Function for semantic search
def search(query):
    query_vector = encode_text(query)
    query_vector = query_vector.astype('float64')
    query_vector = query_vector.tolist()

    results = index_pine.query(vector=query_vector, top_k=10)
    return results


app = Flask(__name__)

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def search_res():
    if request.method == 'POST':
        query = request.form['query']
        res = search(query)
        resss = []
        for j in res['matches']:
            # print(df.iloc[int(j['id'])]['title'], "\n")
            resss.append({'text': df.iloc[int(j['id'])]['text'], 'score': j['score']})
        return render_template('index.html', query=query, result=resss)

if __name__ == '__main__':
    app.run(debug=True)