from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit(1)
if sys.argv[1] != "-f":
    print("Invalid usage")
    sys.exit(1)
if sys.argv[2] not in figlet.getFonts():
    print("Invalid usage")
    sys.exit(1)

figlet.setFont(font=sys.argv[2])
text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
