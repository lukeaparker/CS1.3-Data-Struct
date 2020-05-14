import os

class Jumble:

    def __init__(self, first_word, second_word, third_word, fourth_word):
        self.dict = self._group()
        self.first_word = first_word
        self.second_word = second_word
        self.third_word = third_word
        self.fourth_word = fourth_word
        self.first_answer = self.generate_first_answer(first_word, second_word, third_word, fourth_word)

    def _generate_lookup(self):
        with open("/usr/share/dict/words") as f:
            lines = f.read().lower()
            word_list = lines.split('\n')
        lookup = []
        for word in word_list:
            word_id = self._generate_id(word)
            pair = (word_id, word)
            lookup.append(pair)
        return lookup
    
    def _validate_word(self, word, key_word):
        for char in word:
            if len(word) != len(key_word):
                return False
            elif char not in key_word:
                return False
        for char in key_word:
            if char not in word:
                return False
        return True
    
    def _generate_id(self, word):
        word_val = 0
        for char in word:
            char_val = ord(char)
            word_val += char_val
        return word_val        
    
    def _group(self):
        ano_dict = {}
        for key, word in self._generate_lookup():
            if key in ano_dict:
                ano_dict[key].append(word)
            else:
                ano_dict.setdefault(key, [word])
        return ano_dict
    
    def _find_ano(self, key_word):
        key = self._generate_id(key_word)
        possible_choices = self.dict.get(key)
        choice_list = []
        for word in possible_choices:
            if self._validate_word(word, key_word) == True:
                if word != key_word:
                    choice_list.append(word)
        return choice_list
    
    def generate_first_answer(self, first_word, second_word, third_word, fourth_word):
        first_word = self._find_ano(self.first_word[0])
        second_word = self._find_ano(self.second_word[0])
        third_word = self._find_ano(self.third_word[0])
        fourth_word = self._find_ano(self.second_word[0])
        print(first_word)
        print(second_word)
        print(third_word)
        print(fourth_word)
    
def run():
    first_word = ('laisa', [1, 2, 3])
    second_word = ('laurr', [0, 2])
    third_word = ('bureek', [0, 1])
    fourth_word = ('prouot', [2, 4, 5])
    jumble = Jumble(first_word, second_word, third_word, fourth_word)
    print(jumble.first_answer)
    
run()



        

