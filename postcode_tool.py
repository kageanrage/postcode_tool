import pyperclip

output = pyperclip.paste()
converted_to_csv = output.replace('\r', ',').replace('\n',"")[:-1]  # removes carriage returns, new lines, and the final comma
print(converted_to_csv)
pyperclip.copy(converted_to_csv)
