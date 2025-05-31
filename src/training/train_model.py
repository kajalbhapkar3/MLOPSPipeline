# # # import pandas as pd
# # # import joblib
# # # from sklearn.tree import DecisionTreeRegressor
# # # from sklearn.model_selection import train_test_split

# # # def train():
# # #     df = pd.read_csv('../data/processed/train.csv')

# # #     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
# # #     X = df[features]
# # #     y = df['msrp']

# # #     X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# # #     model = DecisionTreeRegressor(max_depth=5, random_state=42)
# # #     model.fit(X_train, y_train)

# # #     joblib.dump(model, '../../app/model.pkl')
# # #     print("✅ Model trained and saved.")

# # # if __name__ == '__main__':
# # #     train()
# # import os
# # import pandas as pd
# # import joblib
# # from sklearn.tree import DecisionTreeRegressor
# # from sklearn.model_selection import train_test_split

# # def train():
# #     base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# #     train_path = os.path.join(base_dir, 'data/processed/train.csv')
# #     model_path = os.path.join(base_dir, 'app/model.pkl')

# #     df = pd.read_csv(train_path)
# #     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
# #     X = df[features]
# #     y = df['msrp']

# #     X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# #     model = DecisionTreeRegressor(max_depth=5, random_state=42)
# #     model.fit(X_train, y_train)

# #     joblib.dump(model, model_path)
# #     print("✅ Model trained and saved.")

# # if __name__ == '__main__':
# #     train()

# ################################
# import os
# import pandas as pd
# import joblib
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.model_selection import train_test_split
# import subprocess

# def train():
#     script_dir = os.path.dirname(__file__)  # /src/training/
#     data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))  # /src/data/processed/train.csv
#     model_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'app', 'model.pkl'))  # adjust as needed

#     if not os.path.exists(data_path):
#         print("🔄 train.csv not found. Running preprocessing...")
#         result = subprocess.run(
#             ["python3", os.path.abspath(os.path.join(script_dir, '..', 'preprocessing', 'preprocess.py'))],
#             cwd=script_dir
#         )
#         if result.returncode != 0:
#             raise RuntimeError("Preprocessing failed")

#     df = pd.read_csv(data_path)

#     features = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
#     X = df[features]
#     y = df['msrp']

#     X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

#     model = DecisionTreeRegressor(max_depth=5, random_state=42)
#     model.fit(X_train, y_train)

#     joblib.dump(model, model_path)
#     print("✅ Model trained and saved.")

# if __name__ == '__main__':
#     train()
##############################
# src/training/train_model.py

import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import subprocess

def train():
    script_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))
    model_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'app', 'model.pkl'))

    if not os.path.exists(data_path):
        print("🔄 train.csv not found. Running preprocessing...")
        subprocess.run(["python3", os.path.abspath(os.path.join(script_dir, '..', 'preprocessing', 'preprocess.py'))])

    df = pd.read_csv(data_path)

    X = df[['engine_hp']]
    y = df['msrp']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)
    print(" Hi Simple Linear Regression model trained and saved.")

if __name__ == '__main__':
    train()
