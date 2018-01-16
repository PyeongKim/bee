'''
Created on 2015. 11. 6.

@author: kimpyeongeun
'''


print('aaa')
def new_function(aaa):
    if aaa=='a':
        print('k')



def sim(word):
    length_matrix = len(word)**2
    go = len(word[0])
    for i in word:

        length = min(len(i),go)
        go = len(i)

    if len(word[0])>length:
        last = 0
    else:
        last = -1
    n = 0
    add =''
    while n<length:
        for t in range(length_matrix):
            add += word[t][n]
        n+=1
    add += word[last][n:]

    return add


class Alternade:
    def __init__(self,word):
        if isinstance(word,str):
            word = [word]
            self.word = word
        else:
            self.word = word
    def words(self):
        if isinstance(self.word,str):
            a = list(self.word)
            ad = ''
            for d in a:
                ad += d
            return [ad]
        else:
            ab = []
            for i in self.word:
                ab.append(i)
            return ab

    def __repr__(self):
        if len(self.word)!=1:

            return 'Alternade({})'.format(self.word)
        else:
            final = ''
            for alpha in self.word:
                final += alpha
            return 'Alternade({}{}{})'.format("'",final,"'")
    def __add__(self, other):
        return Alternade(self.word + other.word)
    def __str__(self):
        return sim(self.word)
    words = property(words)


word1 = Alternade('SHOE')
print(repr(word1))


words = ['COLD']

word2 = Alternade(words)
word1 = Alternade('SHOE')
word3 = word1 + word2
print(word3)
