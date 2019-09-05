from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

import pandas as pd


# engage = create_engine('redshift+psycopg2://finance_ro:qdgag#6Be_$128@alexa-bi-cluster-3.ceu7fvioeu30.us-east-1.redshift.amazonaws.com:8192/alexadb3')
csv = pd.read_csv('C:\\Users\\alexrand\\Documents\\Alexa_monthly_engagement_metrics_v3.csv')
print(csv.to_json('c:\\Users\\alexrand\\Documents\\engage.json'))
