#!/usr/bin/env python
# STUDENT READINESS PROJECT

__author__ = "Cassandra Pray"
__credits__ = ["Cassandra Pray", "Applied Research Lab"]
__email__ = "rfmx@iup.edu"


import csv
import ResultsTexts
import os
import errno
from tkinter import *
from tkinter.filedialog import askopenfilename




#-----------------------------------------------------------------------
#        FUNCTION FOR PRINTING INFO TO CONSOLE (USE AS CHECK)
#-----------------------------------------------------------------------

def printInfo(case):
    print("Banner ID:", BannerIDs[case])
    print("Name:", FullNames[case])
    print("Academic Habits Rank:", Scores[case][0])
    print("Persistence and Grit Rank:", Scores[case][1])
    print("Academic Confidence Rank:", Scores[case][2])
    print("Interpersonal Maturity Rank:", Scores[case][3])
    print("Confidence with Social Interaction Rank:", Scores[case][4])


#-----------------------------------------------------------------------
#        FUNCTION TO GENERATE RESULT LETTER
#-----------------------------------------------------------------------

# Note: a new folder called 'results' will be created within
#       the current working directory. Each student's result
#       letter will be created in this folder.


def getResults(case):
    ahRank  = Scores[case][0]
    pgRank  = Scores[case][1]
    acRank  = Scores[case][2]
    imRank  = Scores[case][3]
    csiRank = Scores[case][4]

    name = str(LastNames[case]+FirstNames[case])

    thepath = "Results/"

    filename = thepath+name


    cd = os.getcwd()
    fd = os.path.join(cd, r'Results')
    if not os.path.exists(fd):
        os.makedirs(fd)
        


    #-----------------------------------------------------------------------
    #        OPEN FILE TO WRITE TO: SPECIFIC TO STUDENT
    #-----------------------------------------------------------------------


    with open(filename, "w+") as f:

        f.write(FirstNames[case]+"," + "\n")
        f.write(" \n")
        f.write(ResultsTexts.AcademicHabits.get(ahRank)+ "\n")
        f.write(" \n")
        f.write(ResultsTexts.PersistenceGrit.get(pgRank)+ "\n")
        f.write(" \n")
        f.write(ResultsTexts.AcademicConfidence.get(acRank)+ "\n")
        f.write(" \n")
        f.write(ResultsTexts.InterpersonalMaturity.get(imRank)+ "\n")
        f.write(" \n")
        f.write(ResultsTexts.ComfortWithSocialInteraction.get(csiRank)+ "\n")
        f.write(" \n")
        f.write(ResultsTexts.FinalWord)

    f.close()





#-----------------------------------------------------------------------
#        MAKE THE USER INTERFACE
#-----------------------------------------------------------------------

def clickedBtn():
    fn = filedialog.askopenfilename() 
    print(fn)
    window.destroy()
    messagebox.showinfo('Processing', 'Info Processing')

    if fn.lower().endswith('.csv'):

        with open(fn) as csvfile:
            next(csvfile)
            readCSV = csv.reader(csvfile, delimiter = ',')

            BannerIDs = []
            FirstNames = []
            LastNames = []
            FullNames = []
            Scores = []

            for row in readCSV:
                bannerID = row[0]
                firstname = row[1]
                lastname = row[2]
                ah = row[3]
                pg = row[4]
                ac = row[5]
                im = row[6]
                csi = row[7]

                BannerIDs.append(bannerID)
                FirstNames.append(firstname)
                LastNames.append(lastname)
                FullNames.append(str(firstname + ' ' + lastname))
                Scores.append([ah, pg, ac, im, csi])

        for case in range(len(BannerIDs)):
            getResults(case)

    else:
        print("Sorry - you must choose a csv file.")



    
    

window = Tk()
window.title("Student Readiness Program")
window.geometry('650x300')

t = Label(window, text = "Student Readiness Program", font = ("Tahoma", 18))       
t.pack(fill=X, pady = 40)

lbl = Label(window, text = "Please choose the data file you would like to upload." , font = ("Tahoma", 14))
lbl.pack(fill=X, pady = 20)

btn = Button(window, text = "Choose file", command = clickedBtn)
btn.pack(ipadx = 10, pady = 30)

window.mainloop()










