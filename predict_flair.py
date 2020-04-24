from utilities import get_submission_data
from utilities import get_processed_data
from utilities import get_model_prediction
def get_prediction(url):
    data = get_submission_data(url)
    processed_data = get_processed_data(data)
    predicted_flair = get_model_prediction(processed_data)
    return predicted_flair
