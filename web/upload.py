from urllib.request import urlretrieve
import os


def download(url, savepath='./'):
    """
    download file from internet
    :param url: path to download from
    :param savepath: path to save files
    :return: None
    """

    def reporthook(a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")

    filename = os.path.basename(url)
    # 判断文件是否存在，如果不存在则下载
    if not os.path.isfile(os.path.join(savepath, filename)):
        print('Downloading data from %s' % url)
        urlretrieve(url, os.path.join(savepath, filename), reporthook=reporthook)
        print('\nDownload finished!')
    else:
        print('File already exsits!')
    # 获取文件大小
    filesize = os.path.getsize(os.path.join(savepath, filename))
    # 文件大小默认以Bytes计， 转换为Mb
    print('File size = %.2f Mb' % (filesize / 1024 / 1024))


if __name__ == '__main__':
    # 以下载cifar-10数据集为例
    url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    download(url, savepath='./')
