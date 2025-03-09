import re
text = "Hello, world!"
pattern = r"^Hello"
if re.match(pattern, text):
    print("字符串以'Hello'开头")
else:
    print("字符串不以'Hello'开头")