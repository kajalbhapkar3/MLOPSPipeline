# # import pandas as pd

# # def preprocess():
# #     df = pd.read_csv('../../data/processed/raw_data.csv')

# #     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# #     df = df.dropna(subset=['MSRP'])
# #     num_cols = df.select_dtypes(include='number').columns
# #     df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# #     df.to_csv('../../data/processed/train.csv', index=False)
# #     print("✅ Preprocessing completed.")

# # if __name__ == '__main__':
# #     preprocess()
# import os
# import pandas as pd

# def preprocess():
#     base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))  # This points to /src/
#     file_path = os.path.join(base_dir, 'data/processed/clean_raw.csv')
#     output_path = os.path.join(base_dir, 'data/processed/train.csv')

#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"🚫 File not found: {file_path}")

#     df = pd.read_csv(file_path)

#     # Your preprocessing steps here
#     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
#     df = df.dropna(subset=['msrp'])
#     num_cols = df.select_dtypes(include='number').columns
#     df[num_cols] = df[num_cols].fillna(df[num_cols].median())

#     df.to_csv(output_path, index=False)
#     print(f"✅ Preprocessing completed. Saved to: {output_path}")

# if __name__ == '__main__':
#     preprocess()

# src/preprocessing/preprocess.py
##########################################################################
import os
import pandas as pd

def preprocess():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    input_path = os.path.join(base_dir, 'data/processed/clean_raw.csv')
    output_path = os.path.join(base_dir, 'data/processed/train.csv')

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"🚫 File not found: {input_path}")

    df = pd.read_csv(input_path)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    # Drop rows with missing target or feature
    df = df.dropna(subset=['msrp', 'engine_hp'])

    # Fill other numeric columns just in case
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Keep only necessary columns
    df = df[['engine_hp', 'msrp']]

    df.to_csv(output_path, index=False)
    print(f"✅ Preprocessing completed. Saved to: {output_path}")

if __name__ == '__main__':
    preprocess()
