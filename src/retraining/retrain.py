
# import os
# import pandas as pd
# import joblib
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# def retrain():
#     print("🔁 Starting model retraining...")

#     script_dir = os.path.dirname(__file__)
#     data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))
#     model_path = os.path.join(script_dir, '..', '..', 'app', 'model.pkl')

#     data = pd.read_csv(data_path)
#     y = data["msrp"]
#     X = data.drop("msrp", axis=1)
#     X = pd.get_dummies(X)

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     model = DecisionTreeRegressor(max_depth=5)
#     model.fit(X_train, y_train)

#     preds = model.predict(X_test)
#     mse = mean_squared_error(y_test, preds)
#     print(f"✅ Retrained model MSE: {mse}")

#     joblib.dump(model, model_path)
#     print("💾 Retrained model saved.")

# if __name__ == "__main__":
#     retrain()
#################################################
import os
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def retrain():
    print("🔁 Starting model retraining...")

    # Paths
    script_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'processed', 'train.csv'))
    model_path = os.path.join(script_dir, '..', '..', 'app', 'model.pkl')

    # Load data
    df = pd.read_csv(data_path)

    # Use only one feature: engine_hp
    df = df[['engine_hp', 'msrp']].dropna()

    X = df[['engine_hp']]
    y = df['msrp']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train simple regression model
    model = DecisionTreeRegressor(max_depth=5)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"✅ Retrained model MSE: {mse}")

    # Save model
    joblib.dump(model, model_path)
    print(f"💾 Simplified model saved to: {model_path}")

if __name__ == "__main__":
    retrain()
