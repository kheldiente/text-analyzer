import sys
import threading
import time

data = "My name is Michael Diente"

start_time = time.time()
shared_lock = threading.Lock()

class CharacterAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        global shared_lock
        shared_lock.acquire()
        
        characters = data.replace(" ", "")
        characters = characters.replace("\n", "")

        count = len(characters)
        print("Number of characters (excluding spaces) %i" % (count))

        shared_lock.release()


if __name__  == "__main__":
    arguments = len(sys.argv) - 1
    if (arguments == 1):
        filePath = sys.argv[1]
        print("Reading text file: %s..." % (filePath))

        txt_analyzer = CharacterAnalyzer(data)
        txt_analyzer.start()

        txt_analyzer.join()
    else:
        print("Please provide text file path to analyze")