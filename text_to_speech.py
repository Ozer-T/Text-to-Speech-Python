import pyttsx3
import threading

#%%

class Speaking:
    """Speaking class is made for easy coding. Only one speaker can be created!"""  
    #This line can be acquired using .__doc__ for both instance and the class!
    # Speech eingine object is created
    speechEngine = pyttsx3.init()
    __instance_count = 0
    
    def __init__(self, rate = 150, gender = 'm'):
       
        
        if (Speaking.__instance_count == 1):
            raise ValueError('One instance of the class is already exists!')
            return None
        try:
            
            #Speech speed is given (Default = 200)
            self.speechEngine.setProperty("rate",rate)
            self.voices = self.speechEngine.getProperty('voices')
            
            if(gender == 'm'):
                self.speechEngine.setProperty('voice', self.voices[1].id)
            else:
                self.speechEngine.setProperty('voice', self.voices[0].id)
     
        except:
            print('An error occured during speak method!')
            pass
        Speaking.__instance_count += 1
        
    def speak(self,sentence_to_say = None, print2screen = True):
        
        try:
            
            if(print2screen):
                print('The text to vocalize => ' + str(sentence_to_say))
            self.speechEngine.say(sentence_to_say)
            self.speechEngine.runAndWait()
        except:
            print('An error occured while vocalizing!')


#%%

speaker=  Speaking()
speaker.speak('The test speech is completed.')





