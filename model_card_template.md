# Model Card
Barbara Brooks created this model.

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

For the classification tasks, RandomForest Classifier from sklearn was sued with the default parameters.

## Intended Use

The model can be utilized to predict if an individual earns more than 50k based on data from the US Census Bureau.

## Training Data

The Census dataset was obtained as a csv file from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income).  the orginal dataset had 15 columns and 32,561 rows, containing the target label of "salary," with 6 numerical and 8 categorical features.  The "salary" target label has two classes (less than or equal to 50k & greater than 50k), the class imbalance ratio is 75%/25%.  A basic cleaning of the original dataset was performed to remove whitespaces - leading and trailing.  

An 80-20 split was utilixed for the training and testing of this dataset.  Stratification on the target label was applied.

## Evaluation Data

Precision, recall and fbeta metricvs are used to evaluate the classification performance.

## Metrics

Precision: 0.7460
Recall: 0.6302
Fbeta: 0.6832

## Ethical Considerations

Since the model was trained using 1994 census data, it isn't biased towards any particular group.

## Caveats and Recommendations

The extraction was obtained from the 1994 census data.  Since the dataset is outdated, it cannot be seen as statistically representative of the current population.   It is recommended that the 1994 data should be used for training purposes on ML classification and related issues. 
