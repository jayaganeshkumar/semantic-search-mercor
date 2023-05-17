Sure, here is the updated README.md file:


# Semantic Search with Flask

This repository contains a simple web application that performs semantic search on a corpus of text documents. The application is built using Flask, Pinecone, Pandas, Transformers, and tqdm.

## Setup

To install the required dependencies, run the following command in your terminal:

```
pip install -r requirements.txt
```

## Creating an Account and API Key in Pinecone

1. Go to the [Pinecone website](https://pinecone.io/) and create an account.
2. Once you have created an account, you will be able to generate an API key.
3. Copy your API key and save it in a safe place.

## Running the Indexing Notebook

1. Open the `main1.ipynb` notebook in a Jupyter notebook.
2. In the notebook, replace the value of the `YOUR-API-KEY` variable with your Pinecone API key and `YOUR-ENVIRONMENT` with the environment of your index in Pinecone.
3. Run all of the cells in the notebook.

This will create an index in Pinecone and store the vectors of the documents in the corpus.

## Running the Application

1. In your terminal, navigate to the directory where you have cloned this repository.
2. Run the following command to start the application:

```
python main.py
```

The application will be running on port 5000. You can access it by visiting `http://localhost:5000` in your web browser.

## Features

The application has the following features:

* Can be used to search for documents of any type
* Can be used to search for documents that contain specific keywords or phrases
* Can be used to search for documents that are similar to a given document

Thank you