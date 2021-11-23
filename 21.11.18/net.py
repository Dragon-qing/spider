import hashlib
import time

import requests



def login():
    m = hashlib.md5()
    str = "11100437"
    m.update(str.encode("utf-8"))
    str1 = m.hexdigest()
    password = "{MD5}"+str1
    cookie = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    params = {
        'action': 'login',
        'username': '1910300719 @ cmcc',
        'password': password,
        'ac_id': 1,
        'ip': '10.2.55.20',
        'n': 200,
        'type': 1,
        '_': int(time.time()),
        'os': 'Windows 95',
        'name': 'Windows',
        'double_stack': 0
    }
    url = "http://10.0.0.2/srun_portal_pc?ac_id=1&theme=pro"
    response = requests.get(url, headers=headers, params=params, cookies=cookie)
    print(response.text)


if __name__ == '__main__':
    login()