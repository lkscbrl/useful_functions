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

def stemming(text, sufixes='ada|anca|ancia|cao|dao|enca|ez|eza|ismo|mento|sao|tude|ura|ario|aria|eiro|eira|ista|or|nte'):
  
  splits = re.findall(r'^{.*?}{' + sufixes + '}?$', text)
  stem = splits[0][0]
  
  return stem
