under_development_message = "This feature is coming!"

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return '''`Welcome to WhoseAround! I am the WhoseAroundBot. For now, you can communicate with me through commands.

Here are some available commands:
- !help: shows this menu
- !whosearound: shows a list of who is around for games, what they are interested in playing, and at what time
- !iwantotoplay <some game> <what time in HH:MM (optional)>: adds a game to the Game Options List
- !addinterest <some game> <what time in HH:MM (optional)>: show your interest in something in the Game Options List
- !about: about this bot`
'''
    
    if p_message == '!whosearound':
        return under_development_message
    
    if p_message == '!iwantotoplay':
        return under_development_message
    
    if p_message == '!addinterest':
        return under_development_message
    
    if p_message == '!about':
        return '''This bot is being written by Nick Barrett (https://github.com/NickBarrettHFX)
        '''