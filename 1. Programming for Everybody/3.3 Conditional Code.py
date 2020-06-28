score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error, please enter a numerical number.")
    quit()

if score < 0.0:
    print("Error, please enter a score between 0 and 1")
    quit()
elif score > 1.0:
    print ("Error, please enter a score between 0 and 1")
    quit()

if score >= 0.9:
    print ("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")
