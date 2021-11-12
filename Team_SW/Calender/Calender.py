# -*- coding: utf-8 -*-
from google_auth_oauthlib.flow import InstalledAppFlow #�� ������ ���� ���̺귯��
from google.auth.transport.requests import Request
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
import pickle
import os.path


#----------------------------------------------- ����� ����------------------------------------------------------------

#Ŭ���̾�Ʈ ID Json ���ϸ�
creds_filename = 'client.json'
#���� ����
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None


#token.pickle�� ������ ���� ������ �����ϰ� ��ū�� refresh�Ѵ� 
#���� token.pickle�� ������ ���� flow�� �Ϸ��ϸ� �ڵ������� ���������
if os.path.exists('token.pickle'):
    with open('token.pickle','rb') as token:
        creds = pickle.load(token)

#token.pickle�� �������� �ʰų� Ÿ������ ������ ������ �α����ϰ� �Ѵ�
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token: #creds�� ���������� ����� ���¸�
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES) 
        creds = flow.run_local_server(port=0)
        with open('token.pickle','wb') as token:
            pickle.dump(creds,token)


#----------------------------------------------- ���� ���------------------------------------------------------------
import datetime

today = datetime.date.today().isoformat() #���� ��¥ ȣ��
time_min = today + 'T00:00:00+09:00'#UTC+9
time_max = today + 'T23:59:59+09:00'
service = build('calendar', 'v3', credentials=creds) #Api�� ���� ���� ��ü ����
print('Show today s schedule.')
events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=time_min,timeMax=time_max,maxResults=10,orderBy='startTime').execute()

events = events_result.get('items')
print(events[0])



