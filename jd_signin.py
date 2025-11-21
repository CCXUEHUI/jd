import os
import requests

def jd_request(function_id, cookie):
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
        "client": "android"
    }
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        return {"error": f"HTTP {resp.status_code}"}

def jd_signin(cookie):
    # 尝试多个签到接口
    for func in ["signBeanIndex", "taskBean", "beanTaskList"]:
        data = jd_request(func, cookie)
        print(f"接口 {func} 返回：{data}")
        # 简单判断是否签到成功
        if "data" in data and ("dailyAward" in data["data"] or "beanNum" in str(data)):
            print("✅ 签到成功，可能已获得京豆")
            return
    print("⚠️ 未能成功签到，请检查 Cookie 是否有效")

if __name__ == "__main__":
    pt_key = os.getenv("JD_PT_KEY")
    pt_pin = os.getenv("JD_PT_PIN")
    if not pt_key or not pt_pin:
        print("❌ 未检测到 JD_PT_KEY 或 JD_PT_PIN，请在 GitHub Secrets 中配置")
    else:
        cookie = f"pt_key={pt_key};pt_pin={pt_pin};"
        jd_signin(cookie)
