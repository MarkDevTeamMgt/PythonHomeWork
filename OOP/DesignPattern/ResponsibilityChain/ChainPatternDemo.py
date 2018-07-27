



class AbstractLogger:
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, level):
        self.level = level

    def setNextLogger(self, nextLogger):
        self.nextLogger = nextLogger

    def logMessage(self,level, message):
        if self.level <= level:
            self.write(message)

        if self.nextLogger is not None:
            self.nextLogger.logMessage(self.level, message)


    def write(self,message):
        pass


class ConsoleLogger(AbstractLogger):

    def __init__(self, level):
        self.level = level

    def write(self, message):
        print "standard console::Logger" + message


class FileLogger(AbstractLogger):

    def __init__(self, level):
        self.level = level

    def write(self, message):
        print "file::Logger" + message


class ErrorLogger(AbstractLogger):

    def __init__(self, level):
        self.level = level

    def write(self, message):
        print "Error::Logger" + message


class ChainPatternDemo:

    @staticmethod
    def getChainOfLoggers():

        errorlogger = ErrorLogger(AbstractLogger.ERROR)
        fileLogger = FileLogger(AbstractLogger.DEBUG)
        consoleLogger = ConsoleLogger(AbstractLogger.INFO)


        errorlogger.setNextLogger(fileLogger)
        fileLogger.setNextLogger(consoleLogger)
        consoleLogger.setNextLogger(None)

        return  errorlogger


if __name__ == '__main__':
    loggerChain = ChainPatternDemo.getChainOfLoggers()

    loggerChain.logMessage(AbstractLogger.INFO,'this is an information')
    loggerChain.logMessage(AbstractLogger.DEBUG, 'this is a debug')
    loggerChain.logMessage(AbstractLogger.ERROR, 'this is an error')





