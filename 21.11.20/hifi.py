import requests
def check():
    # url = "https://www.hifini.com/"
    temp = "bbs_sid=d21b8eiir84gpbcc3372qg1cdt; bbs_token=BjkmzJiJgjhfrJWuMGWEhzeOO_2FX3lVJSJlgNLXSJJhhYEUu2ycvMDQ3fJ2pV05xmV9jdaaQ2GGvUXDoMVBgNhnRuW_2BvX3Iau; cookie_test=cpsCss_2BN3rO5S6aaNCiN_2Fjdg_2BILJ8sHX5H3N0wAczoIYavxa; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1637217664,1637370450; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1637370450"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {cookie.split("=")[0]:cookie.split("=")[-1] for cookie in temp.split("; ")}
    # response = requests.get(url, headers=headers, cookies=cookies)
    # print(cookies)
    # with open("hifi.html","wb") as f:
    #     f.write(response.content)
    url2 = "https://www.hifini.com/sg_sign.htm"
    response = requests.post(url2, headers=headers, cookies=cookies)
    print(response.json()["message"])


if __name__ == '__main__':
    check()
