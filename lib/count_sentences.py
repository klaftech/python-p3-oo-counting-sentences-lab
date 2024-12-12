#!/usr/bin/env python3

import re
class MyString:
  def __init__(self,value=''):
    self._value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if isinstance(value,str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return True if self.value.endswith(".") else False
  
  def is_question(self):
    return True if self.value.endswith("?") else False

  def is_exclamation(self):
    return True if self.value.endswith("!") else False
  
  def count_sentences(self):
    sentences = re.split(r'(?<=[.?!])\s+', self.value)
    if sentences == ['']:
      return 0
    else:
      return len(sentences)

string = MyString()
#string.value = "This is a string! It has three sentences. Right?"
string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(string.count_sentences())

string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())

string.value = ""
print(string.count_sentences())
# => 3