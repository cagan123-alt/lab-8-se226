from abc import ABC, abstractmethod
from collections import defaultdict


# Question 1
class AbstractClass(ABC):
    address = None
    
    def __init__(self, address):
        self.address = address
    
    @abstractmethod
    def calculateFreqs(self):
        pass


# Question 2,3,4
class ListCount(AbstractClass):
    def calculateFreqs(self):
        freqs = defaultdict(int)
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        freqs[char] += 1
        
        result = []
        for char, count in freqs.items():
            result.extend([char, count])
        
        print (result)

class DictCount(AbstractClass):
    def calculateFreqs(self):
        freqs = {}
        with open(self.address, 'r') as file:
            data = file.read()
            for char in data:
                if char.isalpha():
                    char = char.lower()
                    freqs[char] = freqs.get(char, 0) + 1
        print(freqs)


# Question 5
listCount = ListCount('weirdWords.txt')
listCount.calculateFreqs()
dictCount = DictCount('weirdWords.txt')
dictCount.calculateFreqs()