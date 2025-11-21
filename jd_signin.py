import os
import requests

def jd_signin(cookie):
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36"
    }

    url = "https://api.m.jd.com/client.action"
    params = {
        "functionId": "signBeanIndex",   # 签到领京豆接口
        "appid": "ld",
        "clientVersion": "9.2.0",
        "client": "android"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "dailyAward" in data["data"]:
            award = data["data"]["dailyAward"]
            print(f"✅ 签到成功，获得京豆：{award.get('beanAward', 0)}")
        else:
            print("⚠️ 签到结果：", data)
    else:
        print("❌ 请求失败，状态码：", response.status_code)


if __name__ == "__main__":
    pt_key = os.getenv("JD_PT_KEY")
    pt_pin = os.getenv("JD_PT_PIN")

    if not pt_key or not pt_pin:
        print("❌ 未检测到 JD_PT_KEY 或 JD_PT_PIN，请在 GitHub Secrets 中配置")
    else:
        cookie = f"pt_key={pt_key};pt_pin={pt_pin};"
        jd_signin(cookie)
