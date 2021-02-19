import pandas as pd
import numpy as np

def main(input_data):
    import tensorflow as tf 
    import tensorflow_hub as hub
    import tensorflow_text
  
    embed = hub.load('https://tfhub.dev/google/universal-sentence-encoder/3')
    orgs_table = input_data['org_table'].dropna(subset=['short_description']).reset_index(drop=True)
    
    user_input = input_data['user_input'].sentence.tolist()
    embeddings = embed(user_input)['outputs'].numpy()
    scores = np.dot(embeddings, embed(user_input)['outputs'].numpy()[0])
    df_final = pd.Series(scores).to_frame(name='score')
    return df_final
