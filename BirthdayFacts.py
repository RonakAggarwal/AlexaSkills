def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "factIntent":
        return birthday_facts(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! Namaste!"
    speechOutput =  "Hello , Welcome to birthday facts " \
                    "You can ask me a fact by saying Tell me some birthday facts"
    repromptText =  "You can ask me a fact by saying Tell me some birthday facts"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def birthday_facts(intent, session):
    import random
    index = random.randint(0,len(birthdayfacts)-1)
    cardTitle = "Hello"
    sessionAttributes = {}
    speechOutput = "" + birthdayfacts[index] 
    repromptText = "You can ask me a fact by saying Tell me some birthday facts"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using birthday facts Alexa Skills Kit. " \
                    "Have a great day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



birthdayfacts = [  "If we take account of all birthdays in a year all over the world, which month do you think will have the maximum number of birthday celebrations? Any guesses? Well, it is August!",
                "So, precisely what percentage of total birthdays are celebrated in August? 9% of all birthdays in the world in a given year!",
                "The other two months that follow August closely in terms of number of birthdays celebrated in a month are July and September.",
                "Birthday cards are extremely popular in US though. Why so? That’ because 58% of all cards that are purchased in US are actually birthday cards!",
                "Anne Frank’s diary – we have read of it or at least heard of it. It is world famous. Did you know it was actually her birthday present that she got on her 13th birthday?",
                "There is something known as Golden Birthday. Every single person has this birthday. Do you know which birthday is that? Well, it can never be greater than 31st birthday and it can never be smaller than 1st birthday. Can you guess now? Let us clarify. Golden Birthday is that birthday when a person’s date of birth and his or her age is exactly the same. This means that if a person’s date of birth is say 14th of a month and he or she turns 14, his or her 14th birthday will be the Golden Birthday.",
                "Since you last celebrated your birthday till the time you celebrate your next birthday, your nails will grow by nearly 4 centimeters and your hair will grow by nearly 12 centimeters.",
                "Since you last celebrated your birthday till the time you celebrate your next birthday, this entire world would have experienced at least 50,000 earthquakes.",
                "Again, during the same period, the whole world will have experienced a population growth of 76,570,430. Yes, that many new babies will be born!",
                "Did you know that garden snails have average speed of 0.03 miles an hour? So, if a snail were to keep moving non-stop since your last birthday celebration till your next birthday celebration, it would cover 263 miles. You can cover that distance with just 3 days of non-stop walking.",
                "How many times do you think will you breathe within the same time frame? That’s a whopping 10,512,000 breaths! Remember that on an average a person breaths only 20 times a minutes.",
                "We all get dreams. Some we remember, some we don’t. But in the time since your last birthday to the time you celebrate your next birthday, how many dreams will you get? Well, not many actually. It will be nearly 1,460 dreams."
                ]