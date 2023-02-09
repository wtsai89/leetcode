s = ""
s = input("Greeting: ").strip()
if len(s) >= 5 and s[0:5].lower() == "hello":
    print("$0")
elif s[0].lower() == "h":
    print("$20")
else:
    print("$100")