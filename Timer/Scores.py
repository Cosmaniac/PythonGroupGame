
class Timer:
    def __init__(self, tempTotalTime):
        self.totalTime = tempTotalTime
    
    def Start(self):
        savedTime = int(minute())
        
    def finish(self):
        passedTime = int(minute()) - int(savedTime)
        if(passedTime > totalTime):
            return true
        else:
            return false
        
    