# # import pandas as pd
# # import joblib

# # def load_model(model_path="../../app/model.pkl"):
# #     model = joblib.load(model_path)
# #     return model

# # def make_prediction(model, input_data):
# #     """
# #     Takes a model and input dictionary,
# #     Returns a prediction.
# #     """
# #     df = pd.DataFrame([input_data])
# #     prediction = model.predict(df)
# #     return int(prediction[0])
# import os
# import pandas as pd
# import joblib

# def load_model():
#     base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
#     model_path = os.path.join(base_dir, 'app/model.pkl')
#     model = joblib.load(model_path)
#     return model

# def make_prediction(model, input_data):
#     df = pd.DataFrame([input_data])
#     prediction = model.predict(df)
#     return int(prediction[0])
#############################################################
import os
import pandas as pd
import joblib

def load_model():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    model_path = os.path.join(base_dir, 'app/model.pkl')
    model = joblib.load(model_path)
    return model

def make_prediction(model, input_data):
    """
    input_data: dict with key 'engine_hp', e.g., {"engine_hp": 300}
    """
    df = pd.DataFrame([input_data])
    prediction = model.predict(df[['engine_hp']])  # Use only the relevant feature
    return float(prediction[0])
