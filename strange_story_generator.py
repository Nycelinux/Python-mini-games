def strange_story_generator():
    print("\n Lets create a story! Fill in the blanks!")  
    noun= input("Noun:")
    verb= input("Verb:")
    adjective= input("Adjective:")  
    place= input("place:")  
    action= input("Action:")   
    action2= input("Second action:")
    story= f""" *** THE STRANGE ADVENTURE ***

It was a beautiful day when suddenly a very {adjective} {noun} appeared in the middle of {place}. 
Nobody knew why, but it started to {verb} furiously! 

Before anyone could react, it decided to {action}. 
The crowd gasped in shock. But the real chaos started when it chose to {action2} as well!

And that, kids, is how {place} was changed forever. """

    print("\n Here is your story: \n") 
    print(story)

if __name__ == "__main__": 
    strange_story_generator()    