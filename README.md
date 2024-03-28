
A python program that performs sentiment analysis on a dataset of product reviews.
Start:
Phase 1: Data Preparation
    •	Importing modules
        •	Import NumPy
        •	Import pandas
        •	Import spacy
    •	Download the amazon dataset
    •	View and explore the first 5 rows of the dataset
    •	Explore the features and datatypes of the dataset
    •	Explore missing data of the 24 features in the dataset
    •	Narrow down feature extraction to the most relevant features for sentiment analysis
    •	Explore the dataset for missing data in the extracted features
    •	Clean the extracted features by dropping the entries with missing data
    •	Validate that the entries with missing data are dropped

Phase 2: Defining Functions and Preprocessing
    •	Define a function preprocess( ) to lemmatise, strip, remove words with less meaning and punctuations
    •	Create a new feature (processed_reviews), apply the function – preprocess( ), and assign it to processed_reviews
    •	View the cleaned and extracted dataset to have look at the new feature created with the processed strings or tokens
    •	Next, we download the spaCy language model, apply it to the preprocessed feature and tokenize in the following steps:
        •	 Download the spacy language model
        •	 Convert the processed reviews text into spaCy Doc objects and render to explore more
        •	Iterate over each Doc object and print token information using a for loop
            •	Render the processed docs with displacy
        •	Performing Named Entity Recognition
            •	Iterate over each Doc object and access named entities in further exploration
 Phase 3: Sentiment Analysis
    •	Word Cloud: Positive and Negative Sentiments
        •	Download and Install wordcloud
        •	Import wordcloud
        •	Import matplotlib
        •	Import defaultdict – default dictionary
        •	Declare two dictionary variables for positive and negative words
        •	Install spacytextblob model
        •	Install textblob.download_corpora and  TextBlob to use .sentiment and .polarity
        •	Create a graph image of positive and negative word clouds
    •	Define a function for Sentiment Analysis
        •	Import DOC from spacy.tokens
        •	Define a function to add custom extension attributes to each Doc
        •	Create a TextBlob object for the text of the document
        •	Set the polarity and sentiment attributes using the TextBlob object
        •	Return a doc
    •	Register the custom extension attribute
    •	Because the Extension 'blob' already exists on Doc. 
    •	To overwrite the existing extension, we set `force=True` on `Doc.set_extension
    •	Access the text data from the Pandas Series object and iterate over each text –  for loop
        •	Process the text and get the Doc object
        •	Process the text and get the Doc object using the spaCy model – nlp( )
        •	Calculate the sentiment polarity and subjectivity scores using TextBlob
        •	Print the polarity and subjectivity scores for each text
Phase 4: Similarity Score
    •	Finding Similarity between a pair of reviews using – small – medium – large spaCy models
        •	Load the respective spaCy model
        •	Select two reviews for comparison
        •	Process the text of each review
        •	Compute the similarity score between a pair of reviews
End
