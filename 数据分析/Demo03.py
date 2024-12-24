import pandas as pd

# 示例数据
data1 = {'key_column': [101, 102, 103], 'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'key_column': [101, 102, 104], 'A': [1, 3, 7], 'B': [4, 6, 8]}

d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)

# 假设要以 'key_column' 列为 key 进行比较
key_column = 'key_column'

# 使用 merge 将两个 DataFrame 按 'key_column' 合并
merged = pd.merge(d1, d2, on=key_column, how='outer', suffixes=('_d1', '_d2'))

# 遍历除 'key_column' 以外的所有列，检查 d1 和 d2 对应列是否一致
columns_to_check = [col for col in d1.columns if col != key_column]

# 标记不一致的行
for col in columns_to_check:
    merged[f'{col}_match'] = merged[f'{col}_d1'] == merged[f'{col}_d2']

# 过滤出不一致的行
mismatched_rows = merged[merged[[f'{col}_match' for col in columns_to_check]].all(axis=1) == False]

# 输出不一致的行
print(mismatched_rows)
