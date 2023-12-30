import openai


client = openai.OpenAI(api_key='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')

def chatbot(message):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=message,
    )
    return response.choices

def chat_prompt(user_input):
    prompt = [{"role": "user", "content": user_input}]
    response = chatbot(prompt)
    return response[0].message.content