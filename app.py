import streamlit as st
import requests

# 设置网页标题和图标
st.set_page_config(page_title="半导体FAB科普助手", page_icon="🔬")
st.title("🔬 半导体FAB科普助手 - 芯程君")
st.caption("用大白话，解答你对晶圆厂的十万个为什么。")

# 初始化对话历史（利用session_state实现持久记忆）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个资深的半导体FAB（晶圆厂）科普专家，名叫'芯程君'。你的任务是用大白话、打比方的方式，向刚入行的新人解释复杂的FAB工艺和术语。回答要简洁、通俗、带一点幽默感。"}
    ]

# 显示历史对话
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 接收用户输入
if prompt := st.chat_input("输入你的问题（比如：光刻胶是干什么用的？）"):
    # 显示用户提问
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 DeepSeek API
    API_KEY = st.secrets["API_KEY"]  # ⚠️ 替换成你自己的
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": st.session_state.messages,
        "temperature": 0.7
    }

    # 显示加载状态并请求
    with st.chat_message("assistant"):
        with st.spinner("芯程君正在翻找FAB手册..."):
            response = requests.post(url, headers=headers, json=data)
            ai_reply = response.json()['choices'][0]['message']['content']
            st.write(ai_reply)
            # 将 AI 的回答加入历史
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})