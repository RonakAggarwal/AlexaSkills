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
        return business_fact(intent, session)
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
    speechOutput =  "Hello , Welcome to business facts " \
                    "You can ask me a business fact by saying Tell me a business fact"
    repromptText =  "You can ask me a business fact by saying Tell me a business fact"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def business_fact(intent, session):
    import random
    index = random.randint(0,len(businessfact)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "business fact is that " + businessfact[index] 
    repromptText = "You can ask me a business fact by saying Tell me a business fact"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using business fact Alexa Skills Kit. " \
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



businessfact = [ "If you were to wash one load of laundry every day for a whole 52 years, you would clean the same amount as the launderette staff at Disney World wash in ONE single day." ,
                "The first item on the McDonalds menu was a hotdog." ,
                "1 out of 10 people in Europe are conceived via an Ikea bed." ,
                "The inventor of Vaseline- Robert Chesebrough used to eat a spoonful of the magical stuff every day." ,
                "Jeff Bezos’ (the founder of Amazon) farther was a circus performer." ,
                "Domino’s was founded by two brothers- James and Tom Monaghan." ,
                "Until 1996 Marvel owned the rights to the word “Zombie”." ,
                "The average mobile user checks their mobile phone 150 times a day!",
                "The creator and designer of the famous Nike swoosh tick was paid $35." ,
                "Walmart (ASDA is a subsidiary of the retailer) averages $1.8 million of profit EVERY HOUR." ,
                "73% of people wouldn’t care if the brands they religiously used disappeared from their life." ,
                "American National Standards Institute (ANSI), has created an international standard for C++." ,
                "Starbucks is named after a character in Moby Dick by Herman Melville.",
                "The brand Coca-Cola makes that many different products that if you decided to drink a different one every day it would take you a whole 9 years to try all of them! " ,
                "Facebook’s main colour is blue as Mark Zuckerberg suffers from red-green colour blindness." ,
                "Nike is the most followed clothing brand on Instagram.",
                "Minimum requirement for a C++ program to run is a function." ,
                "Google was originally called BackRub" ,
                "In 2015, Apple became the first ever $700 billion company."
                ]