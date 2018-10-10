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
        return machine_learning(intent, session)
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
    speechOutput =  "Hello , Welcome to machine learning facts " \
                    "You can ask me a fact by saying Tell me machine learning fact"
    repromptText =  "You can ask me a fact by saying Tell me machine learning fact"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def machine_learning(intent, session):
    import random
    index = random.randint(0,len(machinelearning)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "machine learning fact is that " + machinelearning[index] 
    repromptText = "You can ask me a fact by saying Tell me machine learning fact"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using machine learning facts Alexa Skills Kit. " \
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



machinelearning =[ "Machine learning means learning from data" ,
                    "There are an incredible number of problems that you can solve by providing the right training data to the right learning algorithms." ,
                    "Machine learning is about data and algorithms, but mostly data." ,
                "You can have machine learning without sophisticated algorithms, but not without good data." ,
                "Unless you have a lot of data, you should stick to simple models" ,
                "Machine learning trains a model from patterns in your data, exploring a space of possible models defined by parametersselfselfselfselfselfselfselfself." ,
                "A detailed explanation requires more math, but as a rule you should keep your models as simple as possible." ,
                "Machine learning can only be as good as the data you use to train it.",
                "For supervised machine learning tasks like classification, you’ll need a robust collection of correctly labeled, richly featured training dataself." ,
                "Machine learning only works if your training data is representative." ,
                "Most of the hard work for machine learning is data transformation." ,
                "Deep learning is a revolutionary advance, but it isn’t a magic bullet." ,
                "Machine learning systems are highly vulnerable to operator error.",  
                "Machine learning can inadvertently create a self-fulfilling prophecy. " ,
                "AI is not going to become self-aware, rise up, and destroy humanity."
                ]