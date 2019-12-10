import sys
import threading
import time

start_time = time.time()
shared_lock = threading.Lock()
threads = []

sentence_count = 0
word_count = 0
character_count = 0

class SentenceAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        global sentence_count
        global shared_lock
        shared_lock.acquire()

        print("Running sentence analyzer...")
        sentences = data.replace("?", ".").replace("!", ".")
        sentence_count = sentences.count(".")

        print("Releasing sentence analyzer...")
        shared_lock.release()

class WordAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        global word_count
        global shared_lock
        shared_lock.acquire()

        print("Running word analyzer...")
        words = data.split()
        word_count = len(words)

        print("Releasing word analyzer...")
        shared_lock.release()

class CharacterAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        global character_count
        global shared_lock
        shared_lock.acquire()
        
        print("Running character analyzer...")
        characters = data.replace(" ", "").replace("\n", "")
        character_count = len(characters)

        print("Releasing character analyzer...")
        shared_lock.release()


if __name__  == "__main__":
    arguments = len(sys.argv) - 1
    if (arguments == 1):
        filePath = sys.argv[1]
        print("Reading text file: %s..." % (filePath))

        file = open(filePath)
        data = file.read()

        print("Running 3 threads...\n")
        t1 = SentenceAnalyzer(data)
        t2 = WordAnalyzer(data)
        t3 = CharacterAnalyzer(data)

        t1.start()
        t2.start()
        t3.start()

        threads.append(t1)
        threads.append(t2)
        threads.append(t3)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        print("\nNumber of sentences: %i" % (sentence_count))
        print("Number of words: %i" % (word_count))
        print("Number of characters (excluding spaces): %i" % (character_count))
        print("\nTime elapsed: %s second(s)" % (time.time() - start_time))
    else:
        print("Please provide text file path to analyze. Run python text-analyzer-multi-threading.py <.txt>")