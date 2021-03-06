# Python-Google-Sheets-API
How to access Google Sheets API (with Python): a quick, simple & free alternative to a database for small projects / MVPs.<br>

<h2>Steps</h2>
<li>Create a new spreadsheet via <a href="https://www.google.com/sheets/about/">Google Sheets</a> (a Google account is necessary). Fill in some data in the cells.</li>
<li>Open <a href="http://console.cloud.google.com/">Google Cloud Console</a> and create a new project.</li>
<li>Enable <a href="https://console.cloud.google.com/apis/library/drive.googleapis.com">Google Drive API</a>.  Set ‘web server access’, to read ‘application data’. Download your credentials (keep safe!) in JSON format to your project folder.</li>
<li>Enable <a href="http://console.cloud.google.com/apis/library/sheets.googleapis.com">Google Sheets API</a>.</li> 
<li>Install libraries:</li>
<code>pip3 install gspread</code><br>
<code>pip3 install gspread-dataframe</code><br>
<code>pip3 install oauth2client</code><br>
<li>Open your JSON file, copy “client_email” email address from it.</li>
<li>In your Google Sheets spreadsheet press “Share" (big green button in the right top) & paste that email address to add it as “editor”.</li>
<li>Run your program (the data from the spreadsheet will be printed in your Terminal):</li>
<code>python3 gsheetsapi.py</code><br>
