text = "X-DSPAM-Confidence:    0.8475";

cpos = text.find(':')
numtext = len(text)
num = text[cpos+1 : numtext]
numfinal = num.strip()
finalfloat = float(numfinal)
print(numfinal)
