import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


li = pd.DataFrame([[np.nan, 2, np.nan, 0],
                 [3, 4, np.nan, 1],
             [np.nan, np.nan, np.nan, 5],
               [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
li
def read_data(filepath, format):
  """
  Reads data from a file.

  Args:
    filepath: Path to the file.
    format: File format (CSV, Excel, JSON ,VAR).

  Returns:
    A DataFrame containing the data.
  """

  if format == "csv":
    return pd.read_csv(filepath)
  elif format == "excel":
    return pd.read_excel(filepath)
  elif format == "json":
    return pd.read_json(filepath)


  else:
    raise ValueError(f"Unsupported file format: {format}")
# date_set = read_data("../DateSet/csv/student-dataset.csv", "csv")
def data_summary(df):
  """
  Prints a statistical summary of the data.

  Args:
    df: A DataFrame containing the data.

  Returns:
    None.
  """

  print(df.describe())
  print("Most frequent values:")
  for col in df.columns:
    print(f"{col}: {df[col].mode()}")
    
data_summary(li)

def missing_values(df, strategy="mean"):
  """
  Handles missing values in a DataFrame.

  Args:
    df: A DataFrame containing the data.
    strategy: Handling strategy (mean, median, mode, remove).

  Returns:
    A DataFrame with missing values handled.
  """

  if strategy == "mean":
    return df.fillna(df.mean())
  elif strategy == "median":
    return df.fillna(df.median())
  elif strategy == "mode":
    return df.fillna(df.mode())
  elif strategy == "remove":
    return df.dropna()
  else:
    raise ValueError(f"Unsupported missing value handling strategy: {strategy}")
    

missing_v= missing_values(li,"mean")


def encode_categorical_data(df):
  """
  Encodes categorical data in a DataFrame.

  Args:
    df: A DataFrame containing the data.

  Returns:
    A DataFrame with encoded categorical data.
  """

  for col in df.columns:
    if df[col].dtype == "object":
      df[col] = pd.Categorical(df[col])
      df[col] = df[col].cat.codes
  return df
encode_categorical_data(missing_v)

from setuptools import setup, find_packages

setup(
    name='dataprepkit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
    ],
    author='Ahmed Eldesoky',
    author_email='ahmedeldesoky284@email.com',
    description='A package for data preparation tasks',
    url='https://github.com/ahmed-eldesoky284/dataprepkit',
   
)
