
class CountVectorizer: 
  """ Класс для преобразования текстовых данных """ 
  
  def __init___(self,feature_names_out): 
    self.feature_names_out  = feature_names_out
    

  def get_feature_names_out(self, corpus): 
    """ Токенизация текста,приведение слов к нижнему регистру """ 
    
    self.feature_names_out = []
    for line in corpus: 
      for word in line.split(): 
        word = word.lower()
        if word not in self.feature_names_out: 
          self.feature_names_out.append(word)
    return self.feature_names_out


  def fit_transform (self, text): 
    """ One-hot Enconding """

    words= defaultdict(int)
    
    for line in text: 
      for word in self.feature_names_out: 
          words[word] = 0
    
    bag_of_words = []

    for line in text:
      list_words = words.copy()    
      for word in line.split(): 
        word = word.lower()
        list_words[word] += 1
      bag_of_words.append(list(list_words.values()))

    return bag_of_words


if __name__ == "__main__":
  corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"]
  
  vectorizer = CountVectorizer()
  print(vectorizer.get_feature_names_out(corpus))
  print(vectorizer.fit_transform(corpus))
