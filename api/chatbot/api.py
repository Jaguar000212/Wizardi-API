import openai


class openAIChatbot:
    def __init__(self, api_key) -> None:
        self.client = openai.OpenAI(api_key=api_key)

    def chatbot(self, message):
        response = self.client.chat.completions.create(
          model="gpt-3.5-turbo-1106",
          messages=message,
        )
        return response.choices

    def chat_prompt(self, user_input):
        prompt = [{"role": "user", "content": user_input}]
        response = self.chatbot(prompt)
        return response[0].message.content