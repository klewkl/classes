from math import log


class CountVectorizer:

    """
    Класс для преобразования текстовых данных - токенизация тестового корпуса, 
    приведение слов к нижнему регистру
    """

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
        self.bag_of_words = bag_of_words

      return bag_of_words

class TfIdfTransformer:

    """
    TF, IDF, TF-IDF матрицы
    """

  def tf_func(self, matrix):
    tf_matrix = []
    for i in self.bag_of_words:
      n = sum(i)
      words_tf= []
      for num in i:
        words_tf.append(round(num/n, 3))
        tf_matrix.append(words_tf)
        self.tf_matrix = tf_matrix

    return tf_matrix

  def idf_func(self, matrix): 
    num_docs = len(self.bag_of_words)
    idf_matrix = []
    for i in range(len(self.bag_of_words[0])):
      num_of_docs = 0
      for j in range(len(self.bag_of_words)):
        num_of_inputs = self.bag_of_words[j][i]
        if num_of_inputs > 0:
          num_of_docs += 1
          idf_matrix.append(round((log((num_docs + 1) / (num_of_docs + 1)) + 1), 3))
        self.idf_matrix = idf_matrix
    return idf_matrix

  def tf_idf(self, matrix): 
    tf = self.tf_func(matrix)
    idf = self.idf_func(matrix)
    result_matrix = []
    for snt in tf:
      for elem in snt: 
        for num in idf: 
          result_matrix.append(elem * num)
    
    return result_matrix


class TfIdfVectorizer(CountVectorizer):

    def __init__(self):
        self.transformer = TfIdfTransformer()

    def fit_transform(self, text):
        count_matrix = super().fit_transform(text)
        return self.transformer.fit_transform(count_matrix)


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]



# vectorizer = CountVectorizer()
# count_matrix = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_name())
# print(count_matrix)
#
#
# trans = TfIdfTransformer()
# print(trans.term_frequency(count_matrix))
# print(trans.idf_transform(count_matrix))
# print(trans.fit_transform(count_matrix))

# vector = TfIdfVectorizer()
# print(vector.fit_transform(corpus))
# print(vector.get_feature_name())
