import gspread
from oauth2client.service_account import ServiceAccountCredentials 

path1 = "..."  # Paste the path to your project folder 

scope1 = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive'] 

creds1 = ServiceAccountCredentials.from_json_keyfile_name(path1 + "/NAME_OF_YOUR_JSON_FILE.json", scope1)  # Paste the name of your JSON file dowloaded when enabling Google Drive API 

client1 = gspread.authorize(creds1)

my_sheet = client1.open("NAME_OF_YOUR_SPREADSHEET").sheet1   # Paste the name of your Google Sheets spreadsheet 

data1 = my_sheet.get_all_records()

print(data1) 
