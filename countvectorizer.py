import collections 
from collections import defaultdict

class CountVectorizer: 
  """ Класс для преобразования текстовых данных """ 
  
  def __init___(self,feature_names_out,fit_transform): 
    self.feature_names_out  = feature_names_out
    self.fit_transform = fit_transform
  

  def get_feature_names_out(self, corpus): 
    """ Токенизация текста,приведение слов к нижнему регистру """ 
    
    self.feature_names_out = []
    for line in corpus: 
      for word in line.split(" "): 
        word = word.lower()
        if word not in self.feature_names_out: 
          self.feature_names_out.append(word)
    return self.feature_names_out


  def fit_transform (self, text): 
    """ One-hot кодирование для подсчета числа вхождений слова в строку """

    words= defaultdict(int)
    #всем словам из self.feature_names_out задаю значние 0 
    for word in self.feature_names_out: 
        words[word] = 0   
    
    #теперь считаю, сколько каждое слово входит в каждый текст 
    for line in text:     
      bag_of_words = [] 
      for word in line.split(" "): 
        word = word.lower()
        words[word] += 1
      bag_of_words.append(list(words.values()))

      return bag_of_words


if __name__ == "__main__":
  corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"]
  
  

vectorizer = CountVectorizer()
print(vectorizer.get_feature_names_out(corpus))
print(vectorizer.fit_transform(corpus))
