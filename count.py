fruit = "banana"
print(fruit.count("a"))

6.5
str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(":")
num = float(str[start+1:])
print(num)

# another alternative
str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(":")
target =str[start+1:]
num = float(target)
print(num)
