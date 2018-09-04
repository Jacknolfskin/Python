import requests
import random
from threading import Thread
import datetime
import time
"""

接口压测

"""
url = "http://***/openapi/***/submit"

# 批次
# 总数=total_run_num * per_sec_count
total_run_num = 5
# 每秒多少
per_sec_count = 2000

last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
              '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
              '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
              '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
              '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
              '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
              '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']


def first_name_gbk():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    name = bytes.fromhex(val).decode('gb2312')
    return name


def first_name_unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def get_first_name(size):
    name = ""
    for x in range(size):
        try:
            name = name + first_name_gbk()
        except:
            name = name + first_name_unicode()
    return name


def send_request(name, step):
    payload = "{\"ph\":{\"ph1\": \"" + name + "\",\"ph2\": " + str(step) + "}}"
    headers = {
        'Content-Type': "application/json",
        'appId': "",
        'token': "",
        'ts': "",
        'Cache-Control': "no-cache",
        'Postman-Token': "6a26ff90-44e1-4c6e-8e2d-df4f3c59d2ca"
    }

    response = requests.request(
        "POST", url, data=payload.encode('utf-8'), headers=headers)
    return response.text


def main():
    name = random.choice(last_names) + get_first_name(random.choice([2, 3, 4]))
    step = random.randint(1, 3000)
    # print("姓名：{}，步数：{}".format(name, step))
    # print(first_name_gbk())
    text = send_request(name, step)
    # print(text)


def total_request():
    for x in range(total_run_num):
        ts = [Thread(target=main, args=()) for i in range(per_sec_count)]
        [t.start() for t in ts]
        [t.join() for t in ts]
        time.sleep(1)


if __name__ == '__main__':
    old_time = datetime.datetime.now()
    total_request()
    new_time = datetime.datetime.now()
    print("finish，共耗时：", (new_time - old_time).seconds, "秒")
