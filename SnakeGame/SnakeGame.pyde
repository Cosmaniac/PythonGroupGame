class Timer:
    def __init__(self, tempTotalTime):
        self.totalTime = tempTotalTime
    
    def Start():
        savedTime = millis()
        
    def finish():
        passedTime = millis() - savedTime
        if(passedTime > totalTime):
            return true
        else:
            return false
        
    