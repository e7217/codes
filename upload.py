import pandas as pd
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO

host = ''
db = ''


engine = create_engine('mysql+pymysql://root:root@{}/{}'.format(host, db), echo = False)
buffer = BytesIO()
im = Image.open('./cat01.jpg') # name of file
im.show()

im.save(buffer, format='jpeg')
img_str = base64.b64encode(buffer.getvalue())
print(img_str)

img_df = pd.DataFrame({'image_data' : [img_str]})
img_df.to_sql('images', con = engine, if_exists = 'append', index = False)
