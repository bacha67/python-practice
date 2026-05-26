print("'It's already 2025'")
print('"It\'s already 2025"')
print('''It's already 2025''')
print("""It's already 2025""")
#Multiline Strings You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(len(a)) #use the len() function to get the length of a string
#Looping Through a String

x ="banana"
for i in x:
    print(i)
print(len(x))

txt ="the best thing inlife is free"
print("free" in txt) #use the in keyword to check if a certain phrase or character is present in a string
print("expensive" not in txt) #use the not in keyword to check if a certain phrase or character is NOT present in a string