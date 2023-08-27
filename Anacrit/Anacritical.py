import os
import time
import datetime

#functions

#adding to statistics
def add_to_stats(adding): 
    adding=adding+1
    return adding

#displaying score
def badminton_scoring(player_score,opp_score):
    print(str(player_score)+" - "+str(opp_score))
   
#displaying realtime stats 
def current_stats(total_points,total_unforced,total_forced,total_induced,total_unforced_opp):
    print(f"Total points played: "+str(total_points))
    print(f"Total forced errors: "+str(total_forced))
    print(f"Total unforced errors: "+str(total_unforced))
    print(f"Total induced errors: " +str(total_induced))
    print(f"Total unforced errors by opponent: " +str(total_unforced_opp))
    
#intro
print("Welcome to Anacritical!")

#declaring variables for keeping track of stats
total_points =0
total_won=0 #total points won by player
total_lost=0 #total points lost
player_score = 0 #player's score
opp_score = 0 #opponent's score

total_forced = 0 #total forced errors 
total_unforced = 0 #total unforced
total_induced=0 #total induced errors (forced error by opponent)
total_unforced_opp=0 #total

#specifications of win forced points
drop_points = 0
smash_points = 0
moving_points = 0

#specifications of unforced errors
lost_net = 0
lost_out = 0
lost_serve = 0

#variables to check which stat 
win_or_lost = 'n' #placeholder
un_forced = 'n'#placeholder
error = 'n' #...placeholder
error_how = 'n' #PLACE HOLD HER >_<

#START - first, choosing sport
print("Enter what sport you are recording.\nAnacritical Sports: Basketball, Tennis, Badminton, Football, Volleyball.") 
sport = input() #for demo - its just badminton as an option LUL

mode = input("Choose a mode.\nTournament Mode - best of 3 sets up to 25, win by 2 until 29-29 (t)\nFreeplay Mode - no points cap (f)\n")
while mode != 'f' and mode != 't':
    mode=input("Please enter either 't' for Tournament Mode or 'f' for Freeplay Mode.\n") #if input is not recognized

print("Freeplay Mode Selected.") # demo version :v

#collecting date
collect = datetime.datetime.now()
date = collect.strftime("%d-%m-%Y")

#starting up stopwatch
start = input(f"Ready!\nPress 'enter' to confirm Badminton Freeplay Recording Session:")
start_time=int(time.time())

print("Recording and Stopwatch starts now.") #COLLECTING STARTS NOW
while True:
    #printing current stats
    badminton_scoring(player_score,opp_score)
    current_stats(total_points,total_unforced,total_forced,total_induced,total_unforced_opp)
    
    #getting input for next point
    win_lost = input("Won (w) or Lost (l)? Enter (f) to finish.\n")
    while win_lost!='w' and win_lost!= 'l' and win_lost!='f':
        win_lost = input("Please enter 'w' for won point, 'l' for lost point or 'f' to end session.\n") #if input not recognized
        
    if win_lost == "w": #***********WON the point:
        un_forced=input("Opponent made Forced(f) or Unforced Error(u)?\n") #what did opponent do?
        if un_forced == "f":
            total_induced=add_to_stats(total_induced)
            error = input("Error forced by Dropshot (d), Smash (s) or Moving Opponent Around (m)?\n") #how was error induced in opponent by player?
            while error != 'd' and error !='s' and error !='m': 
                error = input("Please enter 'd' for dropshot, 's' for smash or moving opponent around 'm'.\n") #loop if input is not recognized
                
            #considering input for forced error!!
            if error == 'd':
                drop_points=add_to_stats(drop_points) #won by drop shot
            elif error == 's':
                smash_points =add_to_stats(smash_points) #won by smash
            elif error == 'm':
                moving_points =add_to_stats(moving_points) #won by moving opponent around
                
        elif un_forced =="u": #opponent performed unforced error
            total_unforced_opp=add_to_stats(total_unforced_opp) #adding to unforced error stat lmao
            
        player_score = add_to_stats(player_score) #add to player score
        total_points=add_to_stats(total_points) #add total points
            
    elif win_lost == "l": #************lost the point
        
        un_forced=input("Player made Forced (f) or Unforced error (u)?\n") #forced or unforced?
        while un_forced!= 'f' and un_forced!='u':
            un_forced=input("Please enter 'f' for Forced Error or 'u' for Unforced Error.\n") #input not recognized
        
        #considering input for forced error!!!
        if un_forced=='f':
            total_forced=add_to_stats(total_forced) #add to forced errors
            
        #consideirng input even further if player commits unforced error
        elif un_forced=='u':
            total_unforced=add_to_stats(total_unforced) #add to total unforced errors
            
            error_how = input("Out (o), in the net(n) or missed serve?(ms)\n") #what type of unforced error?
            while error_how!='o' and error_how!='n' and error_how!='ms': 
                error_how =input("Please enter 'o' for out, 'n' for in the net or 'ms' for missed serve.\n")#input not recognized
                
            #considering input!!! - adding to type of unforced error
            if error_how=='o':
                lost_out=add_to_stats(lost_out)
            elif error_how=='n':
                lost_net=add_to_stats(lost_net)
            elif error_how=='ms':
                lost_serve=add_to_stats(lost_serve)
                
        #at the end: add to this
        opp_score=add_to_stats(opp_score) #add to opponents score
        total_points=add_to_stats(total_points) #add total points
    
    elif win_lost == "f":
        print("Recording finished.")
        break 

#getting end time
end_time = time.time()
#elapsed time calculating
seconds_lapsed = int(end_time - start_time)

#putting into hours minute seconds format
mins = seconds_lapsed // 60
seconds_lapsed = seconds_lapsed % 60
hours = mins // 60
mins = mins % 60
lapse = (str(hours)+":"+str(mins)+":"+str(seconds_lapsed))

#percentages variables to write into text file -
try:
    unforced_percent = int(total_unforced/opp_score*100)
    unforced_percent=str(unforced_percent)
except Exception as e:
    unforced_percent = 0
    
try:
    forced_percent = int(total_forced/opp_score*100)
    forced_percent=str(forced_percent)
except Exception as e:
    forced_percent = 0

try:
    drop_percent =int(drop_points/total_induced*100)
    drop_percent =str(drop_percent)
except Exception as e:
    drop_percent=0
    
try:
    smash_percent= int(smash_points/total_induced*100)
    smash_percent=str(smash_percent)
except Exception as e:
    smash_percent = 0

try:
    moving_percent =int(moving_points/total_induced*100)
    moving_percent=str(moving_percent)
except Exception as e:
    moving_percent = 0  

#turning variables into string for printing to text file
total_points =str(total_points)
total_won=str(total_won)
total_lost=str(total_lost)
player_score = str(player_score)
opp_score = str(opp_score)

total_forced = str(total_forced)
total_unforced = str(total_unforced)
total_induced=str(total_induced)
total_unforced_opp=str(total_unforced_opp)

drop_points = str(drop_points)
smash_points = str(smash_points)
moving_points = str(moving_points)

lost_net = str(lost_net)
lost_out = str(lost_out)
lost_serve = str(lost_serve)

date = str(date)

#content
file_content = f"""Badminton FreePlay
Date: {date} 
Time elapsed: {lapse}
Final score: {player_score+" - "+opp_score}

Total number of unforced errors: {total_unforced}
Percentage of lost points that were unforced errors: {unforced_percent}%
Unforced errors in net: {lost_net}
Unforced errors out: {lost_out}
Serve errors: {lost_serve}

Total number of forced errors: {total_forced}
Percentage of lost points that were forced errors: {forced_percent}%

Total number of induced errors: {total_induced}
Total number of drop shot points: {drop_points}
Percent of induced errors that were drop shots: {drop_percent}%
Total number of smash points: {smash_points}
Percent of induced errors that were smash points: {smash_percent}%
Total number of moving points: {moving_points}
Percent of induced errors that were moving points: {moving_percent}%

Total number of unforced errors from opponent: {total_unforced_opp}
"""

#making badminton folder in Anacritical folder if it doesn't exist
folder_name = "Badminton"
current_directory = os.getcwd() # Get the current working directory
folder_path = os.path.join(current_directory, folder_name) #path to folder

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    
#naming session 
file_name=input("Name this Session. Entering a name will produce a text file with the title, found in the 'Badminton' folder.\n")
while not file_name.isalnum():
    file_name=input("Please only use alphanumerical characters to name your file.\n") #check if name is alphanumeric
    
#file path crafting
file_path = os.path.join(folder_path, file_name)

#checking if path to possibly same-named file exists
while os.path.exists(file_path):
    file_name=input("That file name already exists. Please choose a different name.\n")
    file_path = os.path.join(folder_path, file_name)
    
with open(file_path, 'w') as file:
    file.write(file_content)

print("Write successful. You can find your text file of data in the 'Badminton' folder.\n Thank you for using Anacritical!\nElevate your Game, One Stat at a Time...")
time.sleep(5)