import pandas as pd
import csv
import pickle
import numpy as np
from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec

## Import lists

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("pickled_names"):
    f.extend(filenames)
    break

# clean .txt
ethnicities = []
for each in f:
    ethnicities.append(each.partition('.')[0])

eth_dict = {}

for ethnicity in ethnicities:
    with open('pickled_names/'+ethnicity+'.pkl', 'rb') as filename:
        names = pickle.load(filename)
    eth_dict[ethnicity] = names

## make a super list of names and true ethnicities

super_list_names = []
super_list_ethnicities = []

for ethnicity in ethnicities:
    name_list = eth_dict[ethnicity][0]
    eth_list = []
    for name in name_list:
        eth_list.append(ethnicity)
    super_list_names = super_list_names + name_list
    super_list_ethnicities = super_list_ethnicities + eth_list
    
df = pd.DataFrame(
            {'Name': super_list_names,
             'True Ethnicity': super_list_ethnicities
            })

## Split into Training and Test
msk = np.random.rand(len(df)) < 0.3
train_df = df[msk]
test_df = df[~msk]

print len(test_df), len(train_df)

## Package DF into token
train_tokens = []
for ethnicity in ethnicities:
    new_tokens = (list(train_df[train_df['True Ethnicity'] == ethnicity]['Name']), ethnicity)
    train_tokens.append(new_tokens)

## Train Classifier (beware, this takes time)

classifier = mxec(train_tokens)
classifier.train()

# tests
print classifier.classify('alexander')
print classifier.classify('robert')
print classifier.classify('li')
print classifier.classify('sajkfldsafh')

## Predict!!!!

test_names = list(test_df['Name'])
test_eth = list(test_df['True Ethnicity'])

test_preds = []

for name in test_names:
    pred = classifier.classify(name)
    test_preds.append(pred)

df_preds = pd.DataFrame({
    'Name': test_names,
    'True Ethnicity': test_eth,
    'Prediction': test_preds
})

# Add True if you got it right
df_preds['Accuracy'] = (df_preds['Prediction']==df_preds['True Ethnicity'])

## Tool to Calculate TPR

def calcAccuracy(df):
    length = len(df)
    length_true = len(df[df['Accuracy']==True])
    return float(length_true)/float(length)

accuracies = []
ethnicity_list = []

# ethnic accuracies
for ethnicity in ethnicities:
    accuracy = calcAccuracy(df_preds[df_preds['True Ethnicity']==ethnicity])
    accuracies.append(accuracy)
    ethnicity_list.append(ethnicity)

# Aggregate accuracy
accuracies.append(calcAccuracy(df_preds))
ethnicity_list.append('OVERALL')

# put into df
df_acc = pd.DataFrame({
    'ethnicity': ethnicity_list,
    'True Positive Rate': accuracies
})

df_acc.set_index('ethnicity', inplace=True)

df_acc.to_csv('results/accuracies.csv')
df_preds.to_csv('results/predictions.csv')

