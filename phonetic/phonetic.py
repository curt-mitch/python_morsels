import sys

nato_dict = {
  'a': 'Alfa',
  'b': 'Bravo',
  'c': 'Charlie',
  'd': 'Delta',
  'e': 'Echo',
  'f': 'Foxtrot',
  'g': 'Golf',
  'h': 'Hotel',
  'i': 'India',
  'j': 'Juliett',
  'k': 'Kilo',
  'l': 'Lima',
  'm': 'Mike',
  'n': 'November',
  'o': 'Oscar',
  'p': 'Papa',
  'q': 'Quebec',
  'r': 'Romeo',
  's': 'Sierra',
  't': 'Tango',
  'u': 'Uniform',
  'v': 'Victor',
  'w': 'Whiskey',
  'x': 'Xray',
  'y': 'Yankee',
  'z': 'Zulu'
}

def phonetic():
  words = ''
  if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
      words += (sys.argv[i] + ' ')
  else:
    words = input('Text to spell out: ')
  for letter in words.strip():
    if letter.lower() in nato_dict:
      print(nato_dict[letter.lower()])
    elif letter == ' ':
      print('')

phonetic()
