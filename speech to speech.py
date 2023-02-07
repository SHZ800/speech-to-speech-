import vosk 
import queue
import pyttsx3
import argparse
import soundfile as sf
import sounddevice as sd

engine = pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',100)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument ('-1','--list-devices',action='store_true',
     help='show list of audio devices and exit')
args,remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__
    formatter_class = argparse.RawDescriptionHelpFormatter,
    parents=[parser])

parser.add_argument(
    '-f','--filename',type=str,metavar='FILENAME',
    help='audio file to store recording to')

parser.add 



     


def speakword(text):
    engine.say(text)
    engine.runAndWait()


while(True):
      speakword("Hello,it's me, I've been wondering")