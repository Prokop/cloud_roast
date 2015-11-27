import gspread
import json

from oauth2client.client import SignedJwtAssertionCredentials
from datetime import datetime

TITLES = ['classname', 'name', 'result', 'comments']

if __name__ == '__main__':
    json_key = json.load(open('google-93c7321c2bec.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                                json_key['private_key'],
                                                scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_key('1G23uWU3EkfFVg5GMOie1B7zi6ip2rwfF3QdW0bk2uE0')
    today = datetime.today()

    worksheet = sheet.add_worksheet(title=today.strftime('%B, %d - %H:%M'),
                                    rows=1, cols=1)
    worksheet.insert_row(TITLES, 1)

    with open('test_results') as f:
        for idx, line in enumerate(f.readlines()):
            if line.startswith('='):
                break
            row = line.split()
            if row:
                row = row[1], row[0], row[-1]
                worksheet.insert_row(row, idx+2)
