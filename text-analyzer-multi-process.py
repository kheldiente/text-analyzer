from multiprocessing import Process
import time
import sys

start_time = time.time()
threads = []

sentence_count = 0
word_count = 0
character_count = 0

class SentenceAnalyzer(Process):
    def __init__(self, data):
        Process.__init__(self)
        self.data = data

    def run(self):
        print("Counting sentences...")

        sentences = data.replace("?", ".").replace("!", ".")
        sentence_count = sentences.count(".")

        print("\nNumber of sentences: %i" % (sentence_count))

class WordAnalyzer(Process):
    def __init__(self, data):
        Process.__init__(self)
        self.data = data

    def run(self):
        print("Counting words...")

        global word_count
        words = data.split()
        word_count = len(words)

        print("Number of words: %i" % (word_count))

class CharacterAnalyzer(Process):
    def __init__(self, data):
        Process.__init__(self)
        self.data = data

    def run(self):
        print("Counting characters...")

        global character_count
        characters = data.replace(" ", "").replace("\n", "")
        character_count = len(characters)

        print("Number of characters (excluding spaces): %i" % (character_count))


if __name__  == "__main__":
    arguments = len(sys.argv) - 1
    if (arguments == 1):
        filePath = sys.argv[1]
        print("Reading text file: %s..." % (filePath))

        file = open(filePath)
        data = file.read()

        print("Running 3 processes...\n")
        t1 = SentenceAnalyzer(data)
        t2 = WordAnalyzer(data)
        t3 = CharacterAnalyzer(data)

        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        
        t1.start()
        t2.start()
        t3.start()

        # Wait for all process to finish
        for thread in threads:
            thread.join()

        print("\nTime elapsed: %s second(s)" % (time.time() - start_time))
    else:
        print("Please provide text file path to analyze. Run python text-analyzer-multiprocessing.py <.txt>")