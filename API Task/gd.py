from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from progress_bar import my_progress_bar


# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# If modifying these scopes, delete the file token.pickle.


class GDApi():
    SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive']
    def __init__(self):
        creds = None
        # # The file token.pickle stores the user's access and refresh tokens, and is
        # # created automatically when the authorization flow completes for the first
        # # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # В credentials должно лежать то, что отдает гугл при создании приложения
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', GDApi.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)


    def create_folder(self, path):
        '''Создает папку с таким путем'''
        file_metadata = {
            'name': path,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.service.files().create(body=file_metadata,
                                            fields='id').execute()
        return file.get('id')

    def upload_file(self, path_to_file, upload_name, folder_id):
        '''загружает файл path_to_file в папку с id folder_id под именем upload_name'''
        file_metadata = {'name': upload_name,
                         'parents': [folder_id]}
        media = MediaFileUpload(path_to_file, mimetype='image/jpeg')
        file = self.service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

    def upload_dir(self, path, file_names):
        '''Загружает все файлы из file_names, лежащих в path на path'''
        print("Uploading Dir")
        dir_id = self.create_folder(path)
        for file in my_progress_bar(file_names):
            self.upload_file(path + "/" + file, file, dir_id)


def main():
    gd = GDApi()
    
    # dir_id = gd.create_folder("test_folder")
    # gd.upload_file("photo.jpg", "photo.jpg", dir_id)


if __name__ == '__main__':
    main()