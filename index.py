def divideNote(weeks,filename):
       import math 
       lines = [line.rstrip('\n') for line in open(f"C:/Users/angular_nija_avenger/Documents/notes/{filename}")]

       g = math.floor(len(lines)/weeks)
       temp = g

       x = True
       l = len(lines)
       counter = 1
       while x:
                 if g > l:
              	   break
                 lines.insert(g,f"<<<<<<<<<<<<<WEEK OF {counter}>>>>>>>>>>>>>>")
                 counter+=1
                 g+=temp
       ge = open(f"C:/Users/angular_nija_avenger/Documents/notes/split_weeks/{filename}","a")
       ge.write(f"<<<<<<<<<<<<<WEEK OF 0>>>>>>>>>>>>>> \n")
       for i in lines:
             ge.write(i+"\n")
       ge.close()



number_of_weeks = input("enter the number of weeks you want: ")
note_directory = input("noteName: ")

try:
     x = int(number_of_weeks) 
     divideNote(x,note_directory)

catch:
     print("invalid only numbers can be used")          