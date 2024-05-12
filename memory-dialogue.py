from openai import OpenAI


client = OpenAI()
# client = OpenAI(
#     api_key='替换为api key',
#     base_url='替换为反代地址'
#     )

MODEL = 'gpt-3.5-turbo'

def slow(msg):
    """一次性响应输出"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=msg
    )

    print(f"ChatGPT > {response.choices[0].message.content}")  # 打印全部响应内容

    if len(msg) < 21:  # 限制只记忆10轮对话
        msg.append({response.choices[0].message.content})  # 将响应内容追加进原始的message列表
    else:  # 删除第一轮对话
        del msg[1:3]

def stream(msg):
    """流式响应输出"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=msg,
        stream=True  # 开启流式输出
    )
    
    contents = ''  # 存储完整流式输出内容的变量
    print("AI > ", end='')

    for chunk in response:
        if chunk.choices[0].delta.content != None:  # 去除流式输出结束时的None内容(content=None)
            print(f"{chunk.choices[0].delta.content}", end='')  # 不换行打印流式输出内容
            contents += chunk.choices[0].delta.content  # 存储流式输出内容
        else:
            print()  # 打印结束后换行，以免"Me >"显示在流式输出内容后面

    if len(msg) < 21:  # 限制只记忆10轮对话
        msg.append({'role': 'assistant', 'content': contents})  # 将流式输出内容追加进原始的message列表
    else:  # 删除第一轮对话
        del msg[1:3]


if __name__ == '__main__':
    message = [{'role': 'system', 'content': "你是一个乐于助人的智能助手。"}]  # 系统角色提示语
    
    while True:
        choice = input("请选择你的对话方式(A. 一次性输出  B.流式输出): ")
        if choice.upper() == 'A':
            print("你选择了一次性输出。下面进入对话，按^+C退出")
            break
        elif choice.upper() == 'B':
            print("你选择了流式输出。下面进入对话，按^+C退出")
            break
        else:
            print("输入有误，请重新输入：")
    
    while True:
        content = input("Me > ")
        message.append({'role': 'user', 'content': content})  # 用户角色内容

        if choice == 'A':
            slow(message)  # 一次性响应函数
        else:
            stream(message)  # 流式响应函数
            