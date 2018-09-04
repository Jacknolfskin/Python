"""
成绩筛选
"""

score = float(input('请输入成绩:'))
if score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'E'
print('对应的等级为:', grade)
