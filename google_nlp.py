
# From google api documentation
def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()
    # content = 'Your text to analyze, e.g. Hello, world!'
    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment


# snippet from pingshiuanchua
# analyzes sentimet of pitch emails
# needs error handling
    # theres an email in latin that broke it
        #pitches_with_results['body'].iloc[390]?

from tqdm import tqdm # This is an awesome package for tracking for loops
import pandas as pd

def sentiment_to_df(series):
    '''Analyze sentiment, get score and magnitude, '''
    gc_results = [sample_analyze_sentiment(str(row)) for row in tqdm(series, ncols = 100)]
    gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
    gc = list(zip(series, gc_score, gc_magnitude))
    columns = ['text', 'score', 'magnitude']
    pitches_with_results_df = pd.DataFrame(gc, columns = columns)
