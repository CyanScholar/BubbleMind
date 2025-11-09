import requests

group_id = "xxxxxxxxxx"
api_key = "xxxxxxxxxxxxxxx"
url = f"https://api.minimax.chat/v1/text/chatcompletion_v2?GroupId={group_id}"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def chat(messages: list, temperature: float = 0.1, max_tokens: int = 256) -> str:
    """
    MiniMax API 接入函数
    
    Args:
        messages: 对话消息列表
        temperature: 温度参数
        max_tokens: 最大token数
        
    Returns:
        AI回复内容
    """
    payload = {
        "model": "minimax-text-01",
        "messages": messages,
        "stream": False,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.95
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        return response_data["reply"]
    else:
        raise Exception(f"MiniMax API 请求失败: {response.status_code}, {response.text}")
