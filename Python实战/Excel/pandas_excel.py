import pandas  as pd

df = pd.read_excel('./res/学生明细表.xlsx', sheet_name=0)  # 这个会直接默认读取到这个Excel的第一个表单
data = df.all  # 默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data))  # 格式化输出
