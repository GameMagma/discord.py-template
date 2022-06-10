# Discord.py Bot Template
My template for a Discord bot made with the discord.py library.

## Required Packages (Base Program):
- discord.py
- python-dotenv

## Environment Variables Setup:
Create a file called ".env" - do not give it a name, just the file extension ".env". If you're using GitHub or public
source control, MAKE SURE TO EXCLUDE/IGNORE THIS FILE. Otherwise, your bot's token can be stolen and used.

In the file, follow this format:`VAR_NAME= var` Make sure you do not put a space before the equals sign (only before),
and put each token on a new line (no other whitespace, no comma at the end of the previous line). The two tokens needed
are the bot's app id and the bot's token. The program has been written to check for the token names "APP_ID" and "TOKEN",
but this can be changed in main.py if needed. Your bot's token and APP_ID can be found at https://discord.com/developers/applications

## IDE and Operating System
This was written in PyCharm on Windows 10 with Python 3.10, but as the project files and packages are not included, as
long as you just copy the python files and put them in the same project together, it'll probably work with any IDE and/or
and operating system.

## Docs And Stuff
The discord.py docs can be found at https://discordpy.readthedocs.io/ and the API reference 
(most of what you're probably looking for) can be found at https://discordpy.readthedocs.io/en/stable/api.html

When in doubt, look it up.