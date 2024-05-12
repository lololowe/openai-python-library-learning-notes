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
        {"role": "user", "content": "你最擅长什么?"},
    ],
)

print(response)
