from gtts import gTTS

def main():
  usrinput = input('\n\nWhat would you like to Text-To-Speech?\n\n> ')
  tts = gTTS(usrinput)
  tts.save('output.mp3')
  print('\n\nFinished!\n\n')


if __name__ == "__main__":
  main()