while True:
    inp = input("\nEnter the text you want to flip backwards: ").lower()
    text = inp.split(" ")
    rev, cor = "", ""
    for sin in text:
        cor += sin + " "
        rev += sin[::-1] + " "
    print("\n" + cor + "\n" + rev)
    
    