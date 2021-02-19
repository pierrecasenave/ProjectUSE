import sys
import numpy as np
import pandas as pd
import tensorflow as tf 
import tensorflow_hub as hub

def main(user_input, org_file):
    embed = hub.load('https://tfhub.dev/google/universal-sentence-encoder/3')
    orgs_table = pd.read_csv('./' + org_file).dropna(subset=['short_description']).reset_index(drop=True)
    embeddings = embed(orgs_table.short_description)['outputs'].numpy()
    scores = np.dot(embeddings, embed([user_input])['outputs'].numpy()[0])
    orgs_table.insert(len(orgs_table.columns),'score',scores)
    orgs_table.sort_values('score', ascending=False)[:15].to_csv('top15.csv', index=False)
    return


if __name__ == "__main__":
    user_input = sys.argv[1]
    org_file = sys.argv[2]
    main(user_input, org_file)