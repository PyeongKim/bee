'''
Created on 2016. 2. 15.

@author: kimpyeongeun
'''
class Organism:
    
    def __init__(self, in_immune):
        reader = open(in_immune, 'r')
        data = reader.readline()
        immune = set()
        while data:
            immune.add(int(data.rstrip()))
            data = reader.readline()
        
        self.innate_immune = immune
        self.ad_immune = {}
    
    def isResistant(self, virus):
        
        put = self.ad_immune.get(virus, 0)
       
        put += 1
        
        self.ad_immune[virus] = put
        
        if self.ad_immune[virus] >= 3:
            self.innate_immune.add(virus)
        
        return len(self.innate_immune.intersection({virus})) == 1
        
    def mutation(self, virus): 
        
        self.ad_immune[virus] = 0
        if len(self.innate_immune.intersection({virus})) == 1:
            self.innate_immune.remove(virus)
        else:
            pass

organism = Organism('immune_system.txt')
print(organism.isResistant(88))
print(organism.isResistant(88))
print(organism.isResistant(88))
organism.mutation(88)
print(organism.isResistant(88))
organism.mutation(42)