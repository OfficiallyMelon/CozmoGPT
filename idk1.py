while True:
    from pyChatGPT import ChatGPT
    import speech_recognition as sr
    import cozmo
    import time
    import random
    
   
    # replace with chatgpt secret key. You will get this in insepct-->applications-->cockies
    session_token = ''
    api = ChatGPT(session_token, conversation_id='e12185d9-7e59-48a8-9c0d-bbba3c210297')
    
    
    def chat():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print("You said: " + query)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        print("query: ", query)
    
        response = api.send_message(str(query))
        message1 = response["message"]
        print(response["message"])
        return message1
    
    returned_message = chat()

       
    def cozmo_program(robot: cozmo.robot.Robot):
        robot.say_text(returned_message).wait_for_completed()
       
        if "Happy'" in returned_message:
            print("ran")
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()
    
        if "Dance'" in returned_message:
            print("ran")
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDancingMambo).wait_for_completed()
    
        if "Sad'" in returned_message:
            print("ran")
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabLose).wait_for_completed()
            

    
    cozmo.run_program(cozmo_program)