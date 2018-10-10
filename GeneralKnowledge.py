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
        return general_knowledge(intent, session)
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
    speechOutput =  "Hello , Welcome to general knowledge " \
                    "You can ask me a GK by saying general knowledge"
    repromptText =  "You can ask me a GK by saying general knowledge"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def general_knowledge(intent, session):
    import random
    index = random.randint(0,len(generalknowledge)-1)
    cardTitle = "Hello"
    sessionAttributes = {}
    speechOutput = "general knowledge is that " + generalknowledge[index] 
    repromptText = "You can ask me a GK by saying general knowledge"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "You can ask me a GK by saying general knowledge" \
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



generalknowledge = [ "No piece of normal-size paper can be folded in half more than 7 times."
                "Blueberry juice boosts memory",
                "When cats are happy or pleased, they squeeze their eyes shut",
                "The elephant is the only animal with 4 knees",
                "Every human spent about half an hour as a single cell",
                "Each year, about 500,000 detectable earthquakes occur in the world. About 100,000 of those can be felt and about 100 of them cause damage.",
                "The tongue is the only body muscle that is attached from one end only.",
                "We, as humans, forget 90% of our dreams",
                "During thinking, we use on about 35% of our brains",
                "The percentage of people dreaming in black and white started decreasing after the spread of color TV",
                "Approximately two-thirds of people tip their head to the right when they kiss",
                "Just days before the World Cup of 1966 in England, the trophy was stolen and then later retrieved by a dog",
                "Some Chinese believe that swinging the arms cures headaches",
                "Coffee drinkers have more sex than non-coffee drinkers.  They also enjoy it more.",
                "The city of Portland in Oregon was named after a coin toss in 1844.  Heads for Portland and tails for Boston.",
                "A queen bee lays 1500 eggs a day.",
                "No president of the United States was an only child for his parents",
                "Laughter is a proven way to lose weight"
                ]
