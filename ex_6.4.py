text = "X-DSPAM-Confidence: 0.8475"
spos=text.find(':')
 
 
value=text[spos+2:]
print(float(value))