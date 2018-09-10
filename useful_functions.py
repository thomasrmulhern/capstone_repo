# USEFUL FUNTIONS FOR WORKING WITH THE DATA

def get_tone(pid):
    '''get the tone of a result from the id of a pitch'''

    if type(pid) is not type(True):
        print('None')
        return None
    else:
        return results[results['pitch_id'] == pid]['tone']

# e.g. get_tone('011dc369-540d-4de2-a60e-412de16feb0f')

def get_body(pitch_id):
    '''get the body of a pitch email from the pitch id of a result'''

    if type(pitch_id) is type(None):
        return None
    else:
        return list(pitches[pitches['id'] == pitch_id]['body'])

#e.g. get_body('c335e34f-d9b2-4eca-8b98-a17d89f228bf')


def writep(filename_as_string, file):
    '''rewrite pitches.pickle'''
    import pickle
    pitches_out = open("/Users/thomasmulhern/new_desk/post/learning/galvanize/capstone/pickles/{0}.pickle".format(filename_as_string),"wb")
    pickle.dump(file, pitches_out)
    pitches_out.close()

# e.g. writep(pitches_with_results)

def openp(filename_as_string):
    '''open pitches_with_results.pickle'''
    import pickle
    pitches_with_results_f = open('/Users/thomasmulhern/new_desk/post/learning/galvanize/capstone/pickles/{0}.pickle'.format(filename_as_string), 'rb')
    file =  pickle.load(pitches_with_results_f)
    pitches_with_results_f.close()
    return file

#e.g. openp(pitches_with_results)


#def non_null_pitches(text):
#    for idx, pitch in enumerate(text):
#        if (type(text) is type(None)) or (len(str(text)) < 30):
#            pass
#        else:
#            pitches_with_body.append(pitches.iloc[idx])
#non_null_pitches(pitches['body'])   

     
#pitches_with_body = pd.DataFrame(columns=pitches.columns)
#pitches_with_body = pitches
#
#
#for idx, pitch in enumerate(pitches_with_body['body']):
#    if (type(pitch) is type(None)):
#        pitches_with_body.drop(idx, inplace=True)
#    elif (len(str(pitch)) < 100):
#        pitches_with_body.drop(idx, inplace=True)
#    else:
#        pass
#len(pitches_with_body)
#        
#        
#        
#from sklearn.feature_extraction.text import TfidfVectorizer   
#        
#        
#vectorizer = TfidfVectorizer("english")
#pitches['vectorized'] = pitches['punct_free_body'].apply(lambda x: vectorizer.fit_transform([x]))
