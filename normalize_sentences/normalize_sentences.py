"""
When I write text in a fixed-width font (code, markdown, etc.), I use two
spaces after sentences. This can lead to inconsistencies when I copy text from
elsewhere or I collaborate on a project with someone who isn't a 2-spacer.

So this week I'd like you to write a function, normalize_sentences, which
accepts a string of text and makes sure there are two spaces between the
sentences.

Your function should work like this:

>>> normalize_sentences("I am. I was. I will be.")
'I am.  I was.  I will be.'
>>> normalize_sentences("Hello? Yes, this is dog!")
'Hello?  Yes, this is dog!'

Your function should treat ., ?, and ! as sentence-ending characters.
"""
def normalize_sentences(sentences):
  return sentences.replace(". ", ".  ").replace("? ", "?  ").replace("! ", "!  ")
