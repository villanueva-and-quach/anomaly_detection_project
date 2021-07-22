
import pandas as pd
import numpy as np
import os
import seaborn as sns

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler




def prepare (df):
    #add names to the new cohorts
    df.name[df.cohort_id == 165] = df.name[df.cohort_id == 165].fillna('cohort165')
    df.name[df.cohort_id == 166] = df.name[df.cohort_id == 166].fillna('cohort166')
    # fill nulls with zero
    df[['start_date', 'end_date', 'program_id']]=df[['start_date', 'end_date', 'program_id']].fillna(0)
    #change dates to date type
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df.date = pd.to_datetime(df.date)
    #set index
    df= df.set_index(df.date, drop = True)
    #dop columns
    df =df.drop(columns=['date'])
    #remove observation that have nulls in endpoint
    df = df[df['endpoint'].notna()]
    #remove only '/'
    df = df[df.endpoint != '/']
    #remove everything that have  'toc', 'search', 'jpeg' 'svg'
    df = df[df.endpoint.str.contains('toc|search|jpg|jpeg|svg') == False]
    return df