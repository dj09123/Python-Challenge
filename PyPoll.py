#Create imports
import os
import csv



#create path to file that probably wont work
#need to ask for help on this
csvpath = os.path.join("Resources", "election_data_csv")


candidate = []


with open(poll_csv) as csvfile:
    csvreaser = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)

    for row in csvreader:
        candidate.append(row[2])



#Vote individuals and variables
diana_votes = 0
charles_votes = 0
raymon_votes = 0



for i in candidate:
    if i == "Diana Degette":
        diana_votes = diana_votes + 1
    if i == "Charles Casper Stockham":
        charles_votes = charles_votes + 1
    if i == "Raymon Anthony Doane":
        raymon_votes = raymon_votes + 1


#total number of candidates
total_candidates = len(total_candidates)
per_diana = 0
per_charles = 0
per_raymon = 0

#Candidate votes
candidate_votes = ( diana_votes,
                    charles_votes,
                    raymon_votes)


#total votes by candidate name
per_diana = round(100 * diana_votes / total ,2)
per_charles = round(100 * charles_votes / total ,2)
per_anthony = round(100 * anthony_votes / total ,2)



winner_index = candidate_votes.index(max)
winner_name = candidate_names[winner_index]



#createing text file
results = os.path.join("Analysis","PyPoll_Analysis.txt")



#closing
with open(results, "w") as textfile:
    textfile.write(analysis_out)