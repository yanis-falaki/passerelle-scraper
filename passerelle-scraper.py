import os
import sqlite3
import requests

def Start():
  db_path = os.environ.get('DB_PATH')
  if db_path is None:
      raise ValueError("DB_PATH environment variable not set")
  
  conn = sqlite3.connect(db_path)
  cursor = conn.execute('SELECT mls_number, order_number, url FROM PHOTOS')

  for row in cursor:
    url = row[2]
    filename = f'{row[1]}.jpg'
    directory = f'./images/{row[0]}/'
    response = requests.get(url)

    if not os.path.exists(directory):
      os.makedirs(directory)

    if response.status_code == 200:
      with open(directory + filename, 'wb') as f:
        f.write(response.content)
        print('Image downloaded successfully')
    else:
      print('Failed to download image')
    


if __name__ == "__main__":
  Start()