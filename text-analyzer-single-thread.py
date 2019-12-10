import sys
import threading
import time

start_time =  time.time()
shared_lock = threading.Lock()
sentence_count = 0
word_count = 0
character_count = 0

class TextAnalyzer(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)

    def run(self):
        global sentence_count
        global word_count
        global character_count

        print("Counting sentences...")
        sentences = data.replace("?", ".").replace("!", ".")
        sentence_count = sentences.count(".")

        print("Counting words...")
        words = data.split()
        word_count = len(words)

        print("Counting characters...")
        characters = data.replace(" ", "").replace("\n", "")
        character_count = len(characters)

if __name__  == "__main__":
    arguments = len(sys.argv) - 1
    if (arguments == 1):
        filePath = sys.argv[1]
        print("Reading text file: %s..." % (filePath))

        file = open(filePath)
        data = file.read()

        print("Running single thread...\n")
        t1 = TextAnalyzer(data)
       
        t1.start()
        t1.join()

        print("\nNumber of sentences: %i" % (sentence_count))
        print("Number of words: %i" % (word_count))
        print("Number of characters (excluding spaces): %i" % (character_count))
        print("\nTime elapsed: %s second(s)" % (time.time() - start_time))
    else:
        print("Please provide text file path to analyze. Run python text-analyzer-single-thread.py <.txt>")