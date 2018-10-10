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
        return car_guide(intent, session)
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
    speechOutput =  "Hello , Welcome to car guide " \
                    "You can ask me a guide by saying Tell me a car guidance"
    repromptText =  "You can ask me a guide by saying Tell me a car guidance"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def car_guide(intent, session):
    import random
    index = random.randint(0,len(carguide)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "guidance is that " + carguide[index] 
    repromptText = "You can ask me a guide by saying Tell me a car guidance"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using car guide Alexa Skills Kit. " \
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



carguide =[ "The world’s first speeding ticket was issued in 1902" ,
                    "1 in 4 cars on the UK’s road were made in China" ,
                    "A modern Formula 1 car can drive upside down in a tunnel at 120mph" ,
                "60 million cars are produced every year" ,
                "1 billion cars are currently in use around the world" ,
                "The average British driver will spend around 99 days of their life stuck in traffic" ,
                "A detailed explanation requires more math, but as a rule you should keep your models as simple as possible." ,
                "It would take less than a month to get to the moon by car",
                "The average car contains over 30,000 unique parts" ,
                "75% of all cars produced by Rolls Royce are still on the road" ,
                "Volkswagen owns twelve well-known car brands from 7 European countries" ,
                "The first ever car accident occurred in 1891" ,
                "The largest speeding fine ever produced was €1,000,000",  
                "The world record for removing and replacing a car engine is 42 seconds " ,
                "The odds of dying in a car accident are around 1 in 5,000"
                ]