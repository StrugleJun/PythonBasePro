from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    'postgresql+psycopg2://postgres:Psql666!!@122.51.206.240:5432/dvdrental',
    pool_size=10,  # 最大连接数
    max_overflow=20  # 超过最大连接数时的连接数
)

# 设置显示最大行数和列数
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', None)  # 自动调整宽度
pd.set_option('display.max_colwidth', None)  # 显示完整的列宽

df = pd.read_sql("select * from address", con=engine)

# 设置某一列的值 左对齐还是右对齐 postal_code
# df['postal_code'].apply(lambda x: str(x))
df['postal_code'] = df['postal_code'].astype(str).str.ljust(20,' ')
print(df)
