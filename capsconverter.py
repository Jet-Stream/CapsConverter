#Tiny program that converts user input's string to all caps, all lowercase, or title case
while True:
    text = input('Enter a sentence, or type Stop:')
    if text == 'Stop':
        break
    change = input('Do you want the sentence to be all Uppercase, all Lowercase, or Title Case?')
    change2 = change.upper()
    acceptedinputs1 = ['UPPER','UPPERCASE','UPPER CASE']
    acceptedinputs2 = ['LOWER', 'LOWERCASE', 'LOWER CASE']
    acceptedinputs3 = ['TITLE', 'TITLECASE', 'TITLE CASE']
    if change2 in acceptedinputs1:
        upperchange = text.upper()
        print (upperchange)
    elif change2 in acceptedinputs2:
        lowerchange =  text.lower()
        print (lowerchange)
    elif change2 in acceptedinputs3:
        titlechange = text.title()
        print(titlechange)
    else:
        print('Sorry, not sure what you mean by that')
    
    
       


        
        
