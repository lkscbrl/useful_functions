import re

def text_split(text, sep=' '):
  
  return text.split(sep)
  
def text_join(text, sep=' '):
  
  return sep.join(text)

def remove_duplicates(text):

  return list(dict.fromkeys(text))

def text_lowercase(text):

  return str(text).lower() 

def remove_stopwords(text, stop_words):

  filtered_text = [word for word in text if word not in stop_words]

  return filtered_text

def remove_extra_whitespaces(text):

  return ' '.join(text.split())

def stemming(text):
  
  splits = re.findall(r'^{.*?}{}?$', text)
  stem = splits[0][0]
  
  return stem
