from var import REGISTERY

class ORTHOCORRECTOR(object):
    def __init__(self):
        self.words = []
        self.path_dic = "dic/liste_francais.txt"
        self.load_dic()
    def load_dic(self):
        try:
            file = open(self.path_dic, "r")
            file.close()
        except:
            print("Unable to load dictionnary ! Main path : " + str(self.path_dic))
        file = open(self.path_dic, "r")
        self.words = file.readlines()
        file.close()
        for i in range(0, len(self.words)):
            self.words[i] = self.words[i].replace("\n", "")
        self.words.append("\n")
    def correct(self, text):
        self.texte = text.split(" ")
        self.result = []
        for i in range(0, len(self.texte)):
            self.text = self.texte[i]
            self.filter()
            self.texte[i] = self.finish()
        return "".join(self.texte)
    def filter(self):
        self.mots = []
        for i in range(0, len(self.words)-1):
            if len(self.text) == len(self.words[i]): self.mots.append(self.words[i])
            else: pass
        self.words.clear()
        self.words = self.mots
        del self.mots
    def finish(self):
        self.max_delta = len(self.text)
        self.mot = ""
        self.indices = []
        for i in range(0, len(self.words)):
            self.indices.append(self.hamming_distance(self.text, self.words[i]))
        for i in range(0, len(self.indices)):
            if self.indices[i] <= self.max_delta:
                self.max_delta = self.indices[i]
                self.mot = self.words[i]
        return self.mot
    def hamming_distance(self, string1, string2): 
        if (len(string1) != len (string2)):
            return -1
        distance = 0
        L = len(string1)
        for i in range(L):
            if string1[i] != string2[i]:
                distance += 1
        return distance
    def sentence(self, sentence):
        self.basic_sentence = sentence
        l = sentence.split(" ")
        for i in range(0, len(l)):
            R = REGISTERY()
            for j in range(0, len(R.ponctuation)):
                l[i] = l[i].replace(R.ponctuation[j], "")
            l[i] = ORTHOCORRECTOR().correct(l[i])
        return " ".join(l)
    def detect_error_btw_sentences(self, sentence):
        n = self.sentence(sentence).lower().split(" ")
        for i in range(0, len(n)):
            R = REGISTERY()
            for j in range(0, len(R.ponctuation)):
                n[i] = n[i].replace(R.ponctuation[j], "")
        m = self.basic_sentence.lower().split(" ")
        print(m)
        print(n)
        for i in range(0, len(n)):
            try:
                if n[i] != m[i]:
                    return i
                else:
                    pass
            except:
                pass 
        return -1