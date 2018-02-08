from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
print(APP_ID)
print(API_KEY)
print(SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})

# 从URL获取文件识别
client.asr('', 'pcm', 16000, {
    'url': 'http://121.40.195.233/res/16k_test.pcm',
    'callback': 'http://xxx.com/receive',
})