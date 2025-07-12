# String creation
text = "Hello, World!"

# Accessing characters
print("First character:", text[0])

# Slicing
print("First five characters:", text[:5])

# Concatenation
greeting = "Hello"
name = "Alice"
print("Concatenation:", greeting + " " + name)

# Repetition
print("Repetition:", greeting * 3)

# Length of string
print("Length:", len(text))

# Changing case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Replace substring
print("Replace:", text.replace("World", "Python"))

# Split string
words = text.split(", ")
print("Split:", words)

# Strip whitespace
whitespace_text = "   Hello   "
print("Stripped:", whitespace_text.strip())

# Find substring
print("Find 'World':", text.find("World"))

# String formatting
age = 25
print(f"{name} is {age} years old.")

# Check if string starts/ends with substring
print("Starts with 'Hello':", text.startswith("Hello"))
print("Ends with '!':", text.endswith("!"))