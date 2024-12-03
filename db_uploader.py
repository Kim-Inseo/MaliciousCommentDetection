import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MaliciousCommentDetection.settings')
# Python 실행 시 환경 변수에 파일 경로 등록
django.setup() # Python 파일에서 Django 실행

from PredictApp.models import *

# CSV 파일 경로
CSV_PATH = './PredictApp/data/Dataset.csv'

# 데이터 삽입
def insert_data(path):
    text_data = pd.read_csv(path, sep='\t')
    text_data.dropna(inplace=True)
    text_data.reset_index(drop=True, inplace=True)
    text_data.rename(columns={'lable': 'label'}, inplace=True)
    text_data['label'] = text_data['label'].apply(int)

    for idx in range(len(text_data)):
        Text.objects.create(
            content = text_data.iloc[idx, 0],
            label = text_data.iloc[idx, 1],
        )

    print('Data Inserted Successfully')

insert_data(CSV_PATH)