import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ================= PATH =================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ================= LOAD DATA =================
def load_data():
    return pd.read_csv(os.path.join(BASE_DIR, 'data', 'laptop_data.csv'))

# ================= PREPROCESS =================
def preprocess(df):

    df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')

    # ---------- Basic Cleaning ----------
    df['Ram'] = df['Ram'].str.replace('GB','').astype(int)
    df['Weight'] = df['Weight'].str.replace('kg','').astype(float)

    # ---------- Screen Features ----------
    df['Touchscreen'] = df['ScreenResolution'].apply(lambda x: 1 if 'Touchscreen' in x else 0)
    df['Ips'] = df['ScreenResolution'].apply(lambda x: 1 if 'IPS' in x else 0)

    df['X_res'] = df['ScreenResolution'].str.extract(r'(\d+)x').astype(int)
    df['Y_res'] = df['ScreenResolution'].str.extract(r'x(\d+)').astype(int)

    df['ppi'] = ((df['X_res']**2 + df['Y_res']**2)**0.5) / df['Inches']

    df.drop(columns=['ScreenResolution','Inches','X_res','Y_res'], inplace=True)

    # ---------- CPU ----------
    def cpu_brand(x):
        if "i7" in x:
            return "Intel Core i7"
        elif "i5" in x:
            return "Intel Core i5"
        elif "i3" in x:
            return "Intel Core i3"
        elif "Intel" in x:
            return "Other Intel"
        else:
            return "AMD Processor"

    df['Cpu brand'] = df['Cpu'].apply(cpu_brand)
    df.drop(columns=['Cpu'], inplace=True)

    # ---------- GPU ----------
    df['Gpu brand'] = df['Gpu'].apply(lambda x: x.split()[0])
    df.drop(columns=['Gpu'], inplace=True)

    # ---------- MEMORY (FULL FIX 🔥) ----------
    def extract_storage(x):
        hdd = 0
        ssd = 0

        parts = x.split('+')

        for part in parts:
            part = part.strip()

            size_str = part.split()[0]

            # Convert TB → GB
            if 'TB' in size_str:
                size = float(size_str.replace('TB','')) * 1024
            else:
                size = float(size_str.replace('GB',''))

            # Assign storage
            if 'HDD' in part:
                hdd += int(size)
            elif 'SSD' in part:
                ssd += int(size)
            elif 'Flash Storage' in part:
                ssd += int(size)
            elif 'Hybrid' in part:
                hdd += int(size)

        return pd.Series([hdd, ssd])

    df[['HDD','SSD']] = df['Memory'].apply(extract_storage)
    df.drop(columns=['Memory'], inplace=True)

    # ---------- OS ----------
    df['os'] = df['OpSys']
    df.drop(columns=['OpSys'], inplace=True)

    return df

# ================= TRAIN =================
def train():

    df = load_data()
    df = preprocess(df)

    X = df.drop(columns=['Price'])
    y = np.log(df['Price'])

    # Save column order
    pickle.dump(X.columns, open(os.path.join(BASE_DIR,'model','columns.pkl'),'wb'))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------- Pipeline ----------
    step1 = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'),
         ['Company','TypeName','Cpu brand','Gpu brand','os'])
    ], remainder='passthrough')

    step2 = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        max_depth=20,
        n_jobs=-1
    )

    pipe = Pipeline([
        ('step1', step1),
        ('model', step2)
    ])

    # ---------- Training ----------
    pipe.fit(X_train, y_train)

    # ---------- Evaluation ----------
    y_pred = pipe.predict(X_test)

    print("📊 Model Performance:")
    print("R2 Score:", round(r2_score(y_test, y_pred), 3))
    print("MAE:", round(mean_absolute_error(y_test, y_pred), 3))

    # ---------- Save ----------
    pickle.dump(pipe, open(os.path.join(BASE_DIR,'model','pipe.pkl'),'wb'))

    print("✅ Model trained and saved successfully!")

# ================= MAIN =================
if __name__ == "__main__":
    train()