from sqlalchemy import create_engine
from sqlalchemy import  text
import streamlit as st

def test():
    # 创建数据库连接
    # 格式：mysql+pymysql://用户名:密码@主机名:端口/数据库名
    engine = create_engine('mysql+pymysql://cmdi0501:laRfPDhspuMViGc5@mysql.sqlpub.com:3306/cmdi0501')
    
    # 一个简单的 SQL 查询
    sql_query = text("SELECT * FROM travel_bills")
    # sql_query = text("SHOW TABLES")
    
    # 使用引擎的连接执行查询
    with engine.connect() as connection:
        result = connection.execute(sql_query)
    
    # 遍历结果
    rows=[]
    for row in result:
        rows.append(row)
    a=str(rows)
    
    return a

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天记录
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message(message["role"], avatar='💣'):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar='🤖'):
            st.markdown(message["content"])

# 用于用户输入

if prompt := st.chat_input('我们来聊一点迎检相关的事儿吧'):
    with st.chat_message('user', avatar='💣'):
        st.markdown(prompt)

    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.spinner("迎检问答助手正在飞快加载中..."):
        response = test()
        with st.chat_message('assistant', avatar='🤖'):
            st.markdown(response)
        st.session_state.messages.append({'role': 'assistant', 'content': response})

