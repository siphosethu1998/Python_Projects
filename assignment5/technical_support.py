# Tech Support
# Stephan Jamieson
# 5/1/2015
responses={
    'bluetooth':'Have you tried mouthwash?',
    'windows':'Ah, I think I see your problem. What version?',
    'apple':'You do mean the computer kind?',
    'blue':'Ah, the blue screen of death. And then what happened?',
    'spam':'You should see if your mail client can filter messages.',
    'connection':'Contact Telkom.',
    'crashed':'Are the drivers up to date?',
    'hacked':'You should consider installing anti-virus software.'}


def default_response():
    return 'Curious, tell me more.'
    
def get_response(words):
    for word in words:
        if word in responses:
            return responses[word]
    return default_response()
    

def print_welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')


def get_input():
    query = input().lower().split(' ')
    return query

def main():
    print_welcome()
    query = get_input()
    while query!=['quit']:
        response=get_response(query)
        print(response)
        query=get_input()
        
main()
