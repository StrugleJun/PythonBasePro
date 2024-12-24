from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
engine = create_engine(
    'postgresql+psycopg2://postgres:Psql666!!@122.51.206.240:5432/dvdrental',
    pool_size=10,  # 最大连接数
    max_overflow=20  # 超过最大连接数时的连接数
)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()
# result = session.execute(text('select * from actor')).fetchall()
# print(result)


result = session.execute(text('select * from address;'))
keys = result.keys()
actors = [dict(zip(keys, row)) for row in result.fetchall()]
for actor in actors:
    print(actor)
session.close()

# 把查询的结果写到excel文件中
