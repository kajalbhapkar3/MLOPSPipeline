# # # # import pandas as pd
# # # # import joblib
# # # # from sklearn.metrics import mean_squared_error
# # # # from sklearn.model_selection import train_test_split

# # # # def evaluate():
# # # #     df = pd.read_csv('../data/processed/train.csv')
# # # #     model = joblib.load('../../app/model.pkl')

# # # #     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
# # # #     X = df[features]
# # # #     y = df['msrp']

# # # #     _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # # #     y_pred = model.predict(X_test)

# # # #     mse = mean_squared_error(y_test, y_pred)
# # # #     print(f"✅ Test MSE: {mse}")

# # # # if __name__ == '__main__':
# # # #     evaluate()
# # # import os
# # # import pandas as pd
# # # import joblib
# # # from sklearn.metrics import mean_squared_error
# # # from sklearn.model_selection import train_test_split

# # # def evaluate():
# # #     base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# # #     train_path = os.path.join(base_dir, 'data/processed/train.csv')
# # #     model_path = os.path.join(base_dir, 'app/model.pkl')

# # #     df = pd.read_csv(train_path)
# # #     model = joblib.load(model_path)

# # #     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
# # #     X = df[features]
# # #     y = df['msrp']

# # #     _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # #     y_pred = model.predict(X_test)

# # #     mse = mean_squared_error(y_test, y_pred)
# # #     print(f"✅ Test MSE: {mse}")

# # # if __name__ == '__main__':
# # #     evaluate()
# # ########################################################
# # import os
# # import pandas as pd
# # import joblib
# # from sklearn.metrics import mean_squared_error
# # from sklearn.model_selection import train_test_split

# # def evaluate():
# #     script_dir = os.path.dirname(__file__)
# #     data_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'train.csv')
# #     model_path = os.path.join(script_dir, '..', '..', 'app', 'model.pkl')

# #     df = pd.read_csv(data_path)
# #     model = joblib.load(model_path)

# #     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
# #     X = df[features]
# #     y = df['msrp']

# #     _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# #     y_pred = model.predict(X_test)

# #     mse = mean_squared_error(y_test, y_pred)
# #     print(f"✅ Test MSE: {mse}")

# # if __name__ == '__main__':
# #     evaluate()
# import os
# import pandas as pd
# import joblib
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import train_test_split

# def evaluate():
#     script_dir = os.path.dirname(__file__)
#     data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))
#     model_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'app', 'model.pkl'))

#     df = pd.read_csv(data_path)
#     model = joblib.load(model_path)

#     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
#     X = df[features]
#     y = df['msrp']

#     _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     y_pred = model.predict(X_test)

#     mse = mean_squared_error(y_test, y_pred)
#     print(f"✅ Test MSE: {mse}")

# if __name__ == '__main__':
#     evaluate()
##################################################
# src/testing/evaluate.py

import os
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

def evaluate():
    script_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))
    model_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'app', 'model.pkl'))

    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    X = df[['engine_hp']]
    y = df['msrp']

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"✅ Test MSE: {mse}")
    print(f"✅ Test RMSE: {rmse}")

if __name__ == '__main__':
    evaluate()
