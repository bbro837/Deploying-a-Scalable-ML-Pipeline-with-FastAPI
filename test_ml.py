import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model
from ml.model import compute_model_metrics
from ml.model import inference

def test_one():
    """
    Test the train_model function to ensure it returns a trained RandomForestClassifier.
    """
    # Sample data
    X_train = [[1, 2], [3, 4], [5, 6]]
    y_train = [0, 1, 0]

    # Train the model
    model = train_model(X_train, y_train)

    # Assertions
    assert isinstance(model, RandomForestClassifier)
    assert model.n_classes_ == 2


def test_two():
    """
    Test the compute_model_metrics function to ensure it calculates precision, recall, and F1 correctly.
    """
    # Sample data
    y = [1, 0, 1, 1, 0]
    preds = [1, 0, 1, 0, 0]

    # Compute metrics
    precision, recall, fbeta = compute_model_metrics(y, preds)

    # Assertions
    assert round(precision, 2) == 1.0  # Precision should be 1.0
    assert round(recall, 2) == 0.67  # Recall should be approximately 0.67
    assert round(fbeta, 2) == 0.8  # F1 score should be approximately 0.8


def test_three():
    """
    Test the inference function to ensure it returns correct predictions.
    """
    # Sample data
    X_test = [[1, 2], [3, 4], [5, 6]]
    y_test = [0, 1, 0]

    # Train a sample model
    model = train_model(X_test, y_test)

    # Run inference
    preds = inference(model, X_test)

    # Assertions
    assert len(preds) == len(X_test)  # Ensure predictions match input size
    assert all(pred in [0, 1] for pred in preds)  # Ensure predictions are valid classes
