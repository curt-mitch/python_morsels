import re

# def semantic_wrap(text):
#   return re.sub(r'([\?\.!])[ ]{1,}', r'\1\n', text)

SENTENCE_END_RE = re.compile(r'([.?!])[ ]+')

def semantic_wrap(text):
  return SENTENCE_END_RE.sub(r"\1\n", text)


