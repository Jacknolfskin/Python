import io
import re

"""
统计文本中单词，并按出现频率排名
"""
class Count:
    def __init__(self, path):
        self.mapping = dict();
        with io.open(path, encoding='utf-8') as f:
            data = f.read()
            words = [s.lower() for s in re.findall('\w+', data)]
            for word in words:
                self.mapping[word] = self.mapping.get(word, 0) + 1

    def common(self):
        return sorted(self.mapping.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    test = Count('word.txt').common()
    for i in test:
        print(i)
