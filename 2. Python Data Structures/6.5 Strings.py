text = "X-DSPAM-Confidence:    0.8475";

#find where the number begins and ends
num_beg = text.find(':')
num_end = len(text)

#finds the number and turn it into float
number = text[num_beg+1:num_end]
floatnumber = float(number)

print(floatnumber)
