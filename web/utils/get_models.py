from openai import OpenAI
from json import load

def get_model_lists(): 
    model_list = load(open('llm_list.json','r'))
    return model_list

def chat_response(message, model_config):
    client = OpenAI(
        api_key = model_config['api_key'],
        base_url = model_config['base_url']
    )
    completion = client.chat.completions.create(
    model = model_config['model'],
    messages = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
        {"role": "user", "content": message}
    ],
    temperature = 0.3,
    stream = True
    )
    return completion
