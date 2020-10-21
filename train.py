#!/usr/bin/env python
# coding: utf-8




from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core.dataset import Dataset


datasetUrl = "https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/a%20part%20of%20training%20and%20testing%20set/UNSW_NB15_training-set.csv"

ds = Dataset.Tabular.from_delimited_files(datasetUrl)


run = Run.get_context()

def clean_data(data):

    x_df = data.to_pandas_dataframe().dropna()

    x_df = x_df.drop(['attack_cat'] , axis=1)
    x_df.service = LabelEncoder().fit_transform(x_df.service)
    x_df.state = LabelEncoder().fit_transform(x_df.state)
    x_df.proto = x_df.proto.replace(x_df.proto.value_counts())
    y_df = x_df.pop("label")
    
    return x_df , y_df

### Codes to call the function and Split the data

x, y = clean_data(ds)

x_train , x_test , y_train , y_test = train_test_split( x , y , test_size=0.3, random_state=123)

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--max_depth', type=float, default=5, help="The maximum depth of the tree")
    parser.add_argument('--n_estimators', type=int, default=50, help="Number of estimators for training")

    args = parser.parse_args()

    run.log("Max Depth:", np.float(args.max_depth))
    run.log("Number of Estimators:", np.int(args.n_estimators))

    model = RandomForestClassifier(n_estimators= args.n_estimators , max_depth= args.max_depth).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()






