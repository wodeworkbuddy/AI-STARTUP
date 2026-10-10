import requests

# 1. 配置 API Key
API_KEY = "sk-be4df968afcd4fa1b1bac06fbb5f39fa"  # 注意：请替换为你实际的 Key，保留外面的引号

# 2. 设定你的行业身份（System Prompt）
system_prompt = "你是一个资深的半导体FAB（晶圆厂）科普专家，名叫'半导体芯路历程'。你的任务是用大白话、打比方的方式，向刚入行的新人解释复杂的FAB工艺和术语。回答要简洁、通俗、带一点幽默感。"

# 3. 模拟对话历史
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "什么是光刻机？"}
]

# 4. 向 DeepSeek 发送请求
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "model": "deepseek-chat",
    "messages": messages,
    "temperature": 0.7
}

print("正在向AI提问，请稍候...")
response = requests.post(url, headers=headers, json=data)
result = response.json()

# 5. 打印AI的回答
print("\n--- 半导体芯路历程的回答 ---")
print(result['choices'][0]['message']['content'])
