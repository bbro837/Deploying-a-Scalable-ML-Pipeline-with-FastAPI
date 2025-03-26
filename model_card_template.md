# Model Card

Barbara Brooks created the model. 

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

 For the classification tasks, RandomForestClassifier from sklear was use with the default parameters.

## Intended Use

The model can be utilized to predict if an individual earns more than 50k based on data from the US Census Bureau.

## Training Data

The Census dataset was obtain as a csv file from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income).   The orginal dataset had 15 columns and 32,561
rows, containing the target label of "salary", with 6 numerical and 8 categorical features.  The "salarly" target label has two classes (less than or equal to 50k & greater than 50k), the class imbalance ration is 75%/25%.  A basic cleaning of the original dataset was performed to remove whitespaces -leading & trailing.  (Ref data_cleaning.ipynb file for data exploration and cleanings steps.) 

An 80-20 split was utilized for the training and testing of this dataset.  Stratification on target label of salary was applied.  

## Evaluation Data

Precision, recall and fbeta metrics are used to evaluate the classification performance. 

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The follwing scores were obtained from the test set:

Precision: 0.7460
Recall: 0.6302
Fbeta: 0.6832

## Ethical Considerations

Since the model was trained on the census data, it isn't biased towards and particular group of people. 


## Caveats and Recommendations

The extraction was done from the 1994 census data.  Since the dataset is outdated, thus can't be seen as a statisticval representation of the current population.   It is recommended that this database be used for training purpose on ML classification or related issues. 