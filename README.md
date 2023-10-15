# ChatInputTwitchBot
Twitch bot that allows chat inputs to control a local virtual controller

IDE setup: 
https://code.visualstudio.com/docs/python/python-tutorial

TwitchIO quickstart:
https://twitchio.dev/en/stable/quickstart.html

vgamepad github:
https://github.com/yannbouteiller/vgamepad

twitch documentation on Client credentials grant flow:
https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#client-credentials-grant-flow

TODO:
- Rework Queue input handling to take in a list of commands to set controller state
- Implement Bucket input handling
- Move command selection type to virtual controller class from bot
- Test commands to configure bot
- Ensure configuration commands require elevated privileges
