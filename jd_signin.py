import os
import requests

def jd_request(function_id, cookie, body="{}"):
    url = "https://api.m.jd.com/client.action"
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36"
    }
    params = {
        "functionId": function_id,
        "appid": "ld",
        "clientVersion": "9.2.0",
        "client": "android",
        "body": body
    }
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        return {"error": f"HTTP {resp.status_code}"}

def jd_signin(cookie):
    # 首页秒杀签到
    seckill_data = jd_request("seckillSign", cookie)
    print("首页秒杀签到返回：", seckill_data)

    # 幸运签到
    lucky_data = jd_request("signBeanAct", cookie,
                            body='{"fp":"-1","shshshfp":"-1","shshshfpa":"-1"}')
    print("幸运签到返回：", lucky_data)

if __name__ == "__main__":
    pt_key = os.getenv("JD_PT_KEY")
    pt_pin = os.getenv("JD_PT_PIN")
    if not pt_key or not pt_pin:
        print("❌ 未检测到 JD_PT_KEY 或 JD_PT_PIN，请在 GitHub Secrets 中配置")
    else:
        cookie = f"pt_key={pt_key};pt_pin={pt_pin};"
        jd_signin(cookie)
