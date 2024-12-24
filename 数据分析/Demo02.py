import pandas as pd

# 示例数据
data1 = {'key_column': [101, 102, 103], 'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'key_column': [101, 102, 104], 'A': [1, 3, 7], 'B': [4, 6, 8]}

d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)

# 假设要以 'key_column' 列为 key 进行比较
key_column = 'key_column'

# 遍历 d1 的每一行，并查找在 d2 中是否有匹配的行
for _, row_d1 in d1.iterrows():
    # 提取 d1 当前行的 key_column 值
    key_value = row_d1[key_column]

    # 在 d2 中查找匹配的行
    matching_rows_d2 = d2[d2[key_column] == key_value]

    # 如果 d2 中有匹配的行
    if not matching_rows_d2.empty:
        # 对每个匹配的行，检查它是否与 d1 当前行完全一致
        for _, row_d2 in matching_rows_d2.iterrows():
            if not row_d1.equals(row_d2):  # 如果两行不一致
                print("d1 行：")
                print(row_d1)
                print("d2 行：")
                print(row_d2)
                print("-" * 50)
