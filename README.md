# Wizardi-API

An API backend for [Wizardi](https://github.com/Jaguar000212/Wizardi), the multi-utility Discord bot. Wizardi-API powers Wizardi’s features and integrations, providing endpoints and services to enhance your Discord experience.

The API is under active development. Expect new features, improvements, and bug fixes as the project evolves.

---

## ⚒️ Requirements

- `flask` to create the web server and handle requests
- `requests` to handle requests from external sources
- `json` to manage JSON outputs
- `openai` to create an AI chatbot
- `animec` for anime database

---

## 💻 Installation

Clone the repository and install the dependencies as per your tech stack. For example, if using Node.js:

```bash
# Clone the repository
git clone https://github.com/Jaguar000212/Wizardi-API.git

# Change the directory
cd Wizardi-API

# Install dependencies
pip install -r requirements.txt

# Start the API server
python app.py
```

---

## 📚 Endpoints

Below are the available API endpoints in **Wizardi-API**. All endpoints are subject to change as the project evolves.

| Endpoint              | Description                        |
|-----------------------|------------------------------------|
| `/chat_get`           | Get a chat response from Wizardi using AI powered by OpenAI  |
| `/superhero`          | Generate or fetch a superhero profile. |
| `/element`            | Get information about a chemical element. |
| `/pickup`             | Get a random pickup line.          |
| `/meme`               | Fetch a random meme.               |
| `/joke`               | Fetch a random joke.               |
| `/fact`               | Get a random fun fact.             |
| `/lulcat`             | Generate a "lulcat" style message. |
| `/weather`            | Fetch weather information for a location. |
| `/quote`              | Get a random inspirational quote.  |
| `/shower_thoughts`    | Fetch a random shower thought.     |
| `/anime`              | Get information about an anime.    |
| `/anime_character`    | Get details about an anime character. |
| `/anime_news`         | Fetch the latest anime news.       |
| `/anime_waifu`        | Get a random anime waifu.          |

- **Example Usage:**
  ```http
  GET /meme
  ```

- **Response:**
  ```json
  {
   "title": "intellectual conversation",
   "author": "AdHour1983",
   "link": "https://redd.it/1kri4z8",
   "subreddit": "memes",
   "content": {
    "image": "https://i.redd.it/6gilsy6mj02f1.png",
    "imageHigh": "https://preview.redd.it/6gilsy6mj02f1.png?width=960&crop=smart&auto=webp&s=c3d46012d334a710a398fe12d50a2e286c89bfe1"
   },
   "misc": {
    "upvotes": 14,
    "nsfw": false,
    "spoiler": false
   }
  }
  ```

---

## 🟢 What more?

- New endpoints and features are planned.
- Bug fixes and optimizations are ongoing.
- Documentation will be expanded as the API grows.

**Contributions are welcome!**  
If you have suggestions or want to help, feel free to open an issue or a pull request.

> Currently, the development has been halted; contributions are welcome.

---

⭐ From [Jaguar000212](https://www.github.com/Jaguar000212)
