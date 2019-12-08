import sys
import threading
import time

data = "My name is Michael Diente."

start_time = time.time()
shared_lock = threading.Lock()

class SentenceAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        global shared_lock
        shared_lock.acquire()

        sentences = data.replace("?", ".")
        sentences = sentences.replace("!", ".")

        count = sentences.count(".")
        print("Number of sentences: %i" % (count))

        shared_lock.release()

class WordAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
    
    def run(self):
        global shared_lock
        shared_lock.acquire()

        words = data.split()
        
        count = len(words)
        print("Number of words: %i" % (count))

        shared_lock.release()

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
        print("Reading text file: %s...\n" % (filePath))

        t1 = WordAnalyzer(data)
        t2 = SentenceAnalyzer(data)
        t3 = CharacterAnalyzer(data)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

        print("\nTime elapsed: %s second(s)" % (time.time() - start_time))
    else:
        print("Please provide text file path to analyze")