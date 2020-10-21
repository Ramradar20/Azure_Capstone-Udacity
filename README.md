
# Azure – Capstone – Deploy the Best Model 

As part of this project, Model Experiments are performed using both HyperDrive and AutoML to identify the best Performing model and Deploy it.

- The Deployed Model End Point is consumed using POST call with data instance in JSON format. The display of score based on the data will signifies the successful deployment of the model for consumption. 

# Project Set Up and Installation

### HyperDrive Setup:

HyperDrive is used to tune the model and parameters we have identified , as part of the HyperDrive run , Parameters are selected for tuning. In this experiments , Random forest Model is selected and parameters such as n_estimators , max_depth are utilized. 
are identified. Initial dataset codes are provided as part of train.py script. And this script is embedded with Estimator and used for HyperDrive Experiments.
If the datascource and pre-processing steps need to be changed , train.py script need to be updated

### AutoMl Setup:
AS part of autoMl setup , autoMl config is updated with the task type , training data and other relevant parameters for experiments.  Experiment run will trigger experimentation with various models and best model will be recommended by autoML , which can be registered and deployed 

### Deployment Procedure 

As part of the deployment , the best model from AutoMl is identified and deployed. For Deployment set of steps need to be followed
-	Save and Register the best model
-	Configure the Score.py file which consist of init and run for initializing the registered model and running it as part of consumption
-	Environment details
-	Inference config , where we need to provide entry script and environment
-	Micro service setup
-	Model deployment 

![](images/automl_inf_config.png)

### Status will be provided based on deployment of the model , we can also check that in the Azure Ml Studio to check the deployment 

![](images/deployed_model_healthy.png)

**In this Screen shot , we can observe that the best model is deployed successfully and the deployment status is “Healthy”**


# Dataset

## Overview

The raw network packets of the UNSW-NB 15 data set is created by the IXIA PerfectStorm tool in the Cyber Range Lab of the Australian Centre for Cyber Security (ACCS) for generating a hybrid of real modern normal activities and synthetic contemporary attack behaviours.

Tcpdump tool is utilised to capture 100 GB of the raw traffic (e.g., Pcap files).

Source of Dataset – [UNSW-NB 15 data set]( https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/a%20part%20of%20training%20and%20testing%20set/UNSW_NB15_training-set.csv)

In this dataset , we can find various online transaction signatures. These features can be used to identify whether a transaction is a fraudulent transaction or Normal Transaction 

## Task

We will be using machine learning models to classify whether a transaction is a Normal Transaction or Fraudulent transactions

**Task**- Classification problem as we are classifying based on features into Normal or Fraudulent Transaction 

There are more than 45 features as part of the dataset, which has wide range of information of network transformation and attack classifications. 

Feature Descriptions are provided in the link below,


https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/NUSW-NB15_features.csv

Target – “label” with values as 1 – for Fraudulent Transaction and 0 – for Normal Transaction is used as Target

## Access 

The data is access using the following URL
https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/a%20part%20of%20training%20and%20testing%20set/UNSW_NB15_training-set.csv

### TabularDatasetFactory Azure API is used to fetch the data directly from the URL and stored it in Azure environment
Screenshot below
![](images/dataset.PNG)

