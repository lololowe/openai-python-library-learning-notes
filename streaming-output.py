from openai import OpenAI


client = OpenAI()
# client = OpenAI(
#     api_key='替换为api key',
#     base_url='替换为反代地址'
#     )

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "你是个乐于助人的助手。"},
        {"role": "user", "content": "你好，请问你是?"},
        {"role": "assistant", "content": "你好! 我是一个专门设计来帮助你解答问题和提供信息的在线助手。有什么我可以帮助你的吗?"},
        {"role": "user", "content": "写一篇800字的作文，主题自拟。"},
    ],
    stream=True  # 开启流式响应
)

for chunk in response:  # 循环处理输出
    if chunk.choices[0].delta.content != None:  # 去除流式输出结束时的None内容(content=None)
        print(chunk.choices[0].delta.content, end='')  # 不换行打印流式输出内容
    else:
        print()  # 打印结束后换行，以免"Me >"显示在流式输出内容后面
        