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
    print(f"ChatGPT > {response.choices[0].message.content}")

def stream(msg):
    """流式响应输出"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=msg,
        stream=True
    )
    print("AI > ", end='')
    for chunk in response:
        if chunk.choices[0].delta.content != None:
            print(f"{chunk.choices[0].delta.content}", end='')
    else:
        print()


if __name__ == '__main__':
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
        message = [{'role': 'user', 'content': content}]
        if choice == 'A':
            slow(message)
        else:
            stream(message)
