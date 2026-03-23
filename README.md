**README File**

**Date:** `2026-03-23`

**Introduction:**
This code defines a Discord bot that integrates with the Ollama API to provide various functionalities such as
answering user questions, summarizing recent messages, clearing messages, fetching news, and providing LinkedIn profile information.
The bot uses the discord.py library to interact with the Discord API and the ollama library to communicate with the Ollama API. 
The bot responds to specific commands issued by users in a Discord server, allowing them to interact with the chatbot and access information in a conversational manner.

**Commands:**

- /hello: Greets the bot.
- /ask <question>: Allows users to ask a question to the chatbot, which responds with a concise and accurate answer.
- /summarize: Summarizes the last 10 messages in the channel.
- /clear [amount]: Clears a specified number of messages from the channel (default is 5).
- /helpme: Displays a help message with available commands.
- /ping: Checks if the bot is responsive.
- /news: Fetches the latest news headlines and provides brief summaries for each headline.
- /linkedInfo <linkedin_url>: Fetches information about a LinkedIn profile and provides a summary of the person's professional background, skills, and recent activity.

**Technologies Used:**

* Python: The programming language used to develop the bot.
* discord.py: A Python library for interacting with the Discord API.
* ollama: A Python library for communicating with the Ollama API.
* dotenv: A Python library for loading environment variables from a .env file.

**How to Use:**
1. Set up a Discord bot and obtain the bot token.
2. Create a .env file and add your bot token as BOT_TOKEN=your_token_here.
3. Run the bot using python app.py.

**Features:**
- The bot responds to user commands in a Discord server.
- It uses the Ollama API to generate responses to user questions and summarize messages.
- It can clear messages from the channel and provide help information about available commands.
- It can fetch the latest news and provide summaries, as well as fetch information about LinkedIn profiles. 