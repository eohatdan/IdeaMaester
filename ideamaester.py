

# This code is to help you choose what project to work on today.
# To choose a project to work on, click on the 'run-all' icon.
# Then open the console and view the last lines to see what to work on today.

# To add a project, copy the last line of line 4, paste it at the bottom of 140, edit it so that
#                         the project name, project description and next task reflects the new project.
# Don't worry about creating duplicates, adding a project actually replaces any with the same name.

# Instrumentation package that controls printing debugging messages
def dprint(msg): # print the message if the debug variable = True.
       if debug:
              print(msg)
def tprint(msg): # print msg if trace variable = True
       if trace:
              print(msg)
def ddprint(msg): # To make it easier to enable/disable dprint
       pass       # If called, ddprint does nothing.  To enable dprint, change ddprint to dprint.

# Functions used by main routine.
      
       
def initProjectsDictionary():
       return({'':[]})


def initProjectsHistory():
    return({'':[]})





def saveProjects(pd,pdName): # Save Projects dictionary/history
        # Store data (serialize)
        import pickle
        empty_list = []
        pickle.HIGHEST_PROTOCOL = 4
        
        if pdName == 'projects_dict' :
            filename = './projects_dict_04.pickle'
            try:
                   with open(filename, 'wb') as handle:
                       pickle.dump(pd, handle, protocol=pickle.HIGHEST_PROTOCOL)
                   tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))
            except:  # if dict not already saved.
                openfile = open(filename,'wb')
                pickle.dump(empty_list,openfile)
            dprint('Saving projects_dict')
            
        elif pdName == 'projects_hist' :
               filename = './projects_hist_04.pickle'
               tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))

               dprint('Saving projects_hist')
               with open(filename, 'wb') as handle:
                    pickle.dump(pd, handle, protocol=pickle.HIGHEST_PROTOCOL)
               
        else: print('Unable to save ',pdName)
        

def restoreProjects(pd,pdName):
       # Restore serialized data
        import pickle
        pickle.HIGHEST_PROTOCOL = 4
        
        if pdName == 'projects_dict' :
            filename = './projects_dict_04.pickle'
            dprint('Restoring projects_dict')
            try:
                   with open(filename, 'rb') as handle:
                       return(pickle.load(handle))
            except:
                    # Need to create a new projects dictionary file and initialize it.
                    
                    tprint('No dict file found.')
                    empty_dict = {'root' : 'start'}
                    
                    tprint('Filename = ' + filename)
                    newfile = open(filename,'x') # Creates a new file
                    newfile.close()
                    # Initialize the file with a dummy entry.
                    with open(filename,'wb') as handle:
                        pickle.dump(empty_dict,handle,protocol=pickle.HIGHEST_PROTOCOL)
                    handle.close()
                    tprint('New dict file created.')
                    # Return the newly initialized projects dictionary
                    with open(filename, 'rb') as handle:
                       return(pickle.load(handle))
                    
        if pdName == 'projects_hist' :
            
               filename = './projects_hist_04.pickle'
               dprint('Restoring projects_hist')
               try:
                   with open(filename, 'rb') as handle:
                       return(pickle.load(handle))
               except:
                    # Need to create a new projects history file and initialize it.
                    
                    tprint('No hist file found.')
                    empty_dict = {'root' : 'start'}
                    
                    tprint('Filename = ' + filename)
                    newfile = open(filename,'x') # Creates a new file
                    newfile.close()
                    # Initialize the file with a dummy entry.
                    with open(filename,'wb') as handle:
                        pickle.dump(empty_dict,handle,protocol=pickle.HIGHEST_PROTOCOL)
                    handle.close()
                    tprint('New dict file created.')
                    # Return the newly initialized projects history
                    with open(filename, 'rb') as handle:
                       return(pickle.load(handle))
                    
def addToProjectsHistory(pd,key,desc,next_todo):
    key = key.strip(' ')
    tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))
    dprint('Key = '+key+' with length = '+str(len(key)))
    dprint('Adding to project_hist: ' + key + ': ' + desc + ' ' + next_todo)
    try:
        pd[key] = [desc,next_todo]
    except:
        completedTask = key
        print('unable to add ', completedTask, ' to project history.')
      
def listProjects(pd):
       spd = sortByKey(pd)
       for project in spd:
              print(project,spd[project])
       return()

def createProjectsList(pd):
        plist = []
        for p in pd:
            plist.append(p)
        return(plist)
def createProjectsHistory(pd):
  plist = []
  for p in pd:
       plist.append(p)
  return(plist)

def ProjectsChooser(pd): # Choose a project to work on based on random number whose range is the length of the dictionary.
       
        import random
        pdlen = len(pd)
        tprint("Dictionary Length: "+str(pdlen))
        if pdlen >1 :
            r = random.randint(1,pdlen-1)
            projects_list = createProjectsList(pd)
            key = projects_list[r] # The integer, r, returns just the key of dictionary
            print(key,':',pd[key][0],'\nNext task:',pd[key][1])
            return()
        else:
            dprint("Length of dict <= 0; Cannot suggest idea to work on.")
        return()

def ShowProjectsHistory(pd):  # Print the list of completed tasks.
       # projects_history = createProjectsHistory(pd)
       for p in pd:
              if p!= None:
                     dprint('In ShowProjectsHistory' + str(p) + str(pd[p]))
              

def deleteProjects(pd,key):
       #  key = key + ' '
       dprint('deleteProjects entered with key: ' + key)
       try:
                   del pd[key]
                   print('key ', key, ' deleted from Projects dictionary')
       except:
                   print('Unable to delete ', key)

def deleteHistory(pd,key):
       #  key = key + ' '
       dprint('deleteHistory entered with key: ' + key)
       try:
                   del pd[key]
                   print('key ', key, ' deleted from Projects history')
       except:
                   print('Unable to delete ', key)
                   
def getDebug():
       return(debug)

def setDebug(flag):
       if flag: return(True)
       else:    debug = (False)
def setTrace(flag):
       if flag: return(True)
       else:    trace = (False)


def sortByKey(pd):
   my_result = dict()
   for key in sorted(pd):
       my_result[key] = sorted(pd[key])
   return(my_result) 

def getArgs(adict): # -s: show history; -a: add to-do; -d: delete project -h: help
       import tkinter as tk
       global myAction
       global myDesc
       global myToDo
       root= tk.Tk()
       # Define window
       canvas1 = tk.Canvas(root, width = 600, height = 500)
       canvas1.pack()
       root.title('IdeaMaester -- Manage your ideas.')
       # Create text entry windows
       labela = tk.Label(root, text= 'Action: '+myAction)
       canvas1.create_window(100,40,window=labela)
       labelb = tk.Label(root, text= 'Project: '+myProject)
       canvas1.create_window(100,80,window=labelb)
       labelc = tk.Label(root, text= 'Description: '+myDesc)
       canvas1.create_window(100,120,window=labelc)
       labeld = tk.Label(root, text= 'Next task: '+myToDo)
       canvas1.create_window(100,150,window=labeld)
       entry1 = tk.Entry (root) # Action
       canvas1.create_window(250, 40, window=entry1)
       entry2 = tk.Entry (root) # Project key
       canvas1.create_window(250, 80, window=entry2)
       entry3 = tk.Entry (root) # Project description
       canvas1.create_window(250, 120, window=entry3)
       entry4 = tk.Entry (root) # Project todo
       canvas1.create_window(250, 150, window=entry4)
       def getArgsSub ():
       # Get the values entered in the text entry fields
              global myAction
              global myProject
              global myDesc
              global myToDo
              myAction = entry1.get()
              myProject = entry2.get()
              myDesc = entry3.get()
              myToDo = entry4.get()
              #setAction(action)
              tprint('myAction = ' + myAction)
              # Echo the values for each field
              label1 = tk.Label(root, text= 'Action '+myAction)
              label2 = tk.Label(root, text= 'Project '+myProject)
              label3 = tk.Label(root, text= 'Description '+myDesc)
              label4 = tk.Label(root, text= 'ToDo '+ myToDo)
              canvas1.create_window(200, 250, window=label1)
              canvas1.create_window(200, 270, window=label2)
              canvas1.create_window(200, 300, window=label3)
              canvas1.create_window(200, 330, window=label4)
       def close(): # Close window and continue
              root.destroy()
       # Create the button to allow fields to be entered
       button1 = tk.Button(text='Process command', command=getArgsSub)
       canvas1.create_window(200, 180, window=button1)
       # Create the button to close window and continue
       button2 = tk.Button(text='Continue', command=close)
       canvas1.create_window(200, 220, window=button2)
       root.mainloop()
       tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))
       
       tprint('myAction = ' + myAction)

       if (myAction == '-h'): #Help
              print('IdeaMaester help:')
              print('-a: Add a task to the project dictionary.')
              print('-c: Mark a task complete and add to project history.')
              print('-h: Provide help.')
              print('-l: List the active tasks in the project dictionary.')
              print('-n: Add a note to the project history.')
              print('-r: Remove a task from the project dictionary.')
              print('-s: Show history and notes.')
              print('-x: Remove a note from the project history.')
              print('-z: Choose next task')
              
       if (myAction == '-a'): # If the add_task argument has been chosen
           tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))
           addToProjectsHistory(adict,myProject,myDesc,myToDo)
           return('a')

       if (myAction == '-s'): # show_history is set to True if -s is entered on the command prompt
              # Add code here to show projects_hist
              tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))
              print('Ideas/Project history/notes: \n')
              listProjects(projects_hist)
              return('s')
              
       if (myAction == '-l'):  # list all pending todo's
              print('Ideas/Projects: \n ')
              listProjects(projects_dict)
              return('l')

       if (myAction == '-r'): # remove a task from projects_dict based on key.
              # Add code here to delete task
              deleteProjects(adict,myProject)
              return('r')

       if (myAction == '-c'): #Complete a task based on key.
                            
              # Logic:
              # 1.) see if key is in dictionary
              #    a.) if so, get the dictionary entry into a variable
              #      i.) add the variable as a dictionary entry into the history dictionary
              #      ia.) save the history dictionary.
              #      ii.) delete the entry with key in the projects dictionary
              #      iii.) print message that the task has been recorded as complete
              #    b.) if not,
              #      i.) print mesage that task with key not found in projects dictionary.
              
              if  projects_dict.get(myProject) != None:
                     avar = projects_dict.get(myProject)
                     addToProjectsHistory(projects_hist,myProject,myDesc,myToDo)
                     saveProjects(projects_hist,'projects_hist')
                     deleteProjects(projects_dict,myProject)
                     print('Task with key: '+ myProject + 'has been marked complete and recorded in projects history.')
              else:
                      print('Unable to find '+myProject+' in projects dictionary.')
              return('c')
       
       if (myAction == '-n'): #Add a note to project history.
              addToProjectsHistory(projects_hist,myProject,myDesc,myToDo)
              saveProjects(projects_hist,'projects_hist')
              return('n')
       
       if (myAction == '-x'): #Remove a note from project history.
              deleteHistory(projects_hist,myProject)
              saveProjects(projects_hist,'projects_hist')
              return('-x')
       
       return('z') # No action was specified.  

# Main: Here's where the code execution begins.
if (__name__ == '__main__'): #Note: this keeps the module from executing if imported
       import inspect
       debug = setDebug(False)  # Global variable controlling dprint
       trace = setTrace(True)   # Glogal variable controlling tprint
       # Create global variables to capture GUI inputs
       myAction = '';myProject = '';myDesc = '';myToDo = ''
       projects_dict = initProjectsDictionary() # Define and initialze the projects dictionary.
       projects_hist = initProjectsHistory()    # Define and initialze the projects history dictionary.

       tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))

       ddprint(str(projects_hist) + str(type(projects_hist)))

       # Restore projects_dict from local disk.
       projects_dict  = restoreProjects(projects_dict,'projects_dict')
       tprint('At line: ' + str(inspect.getframeinfo(inspect.currentframe()). lineno))

       dprint('Projects_dict:\n' + str(projects_dict))
       projects_hist = restoreProjects(projects_hist,'projects_hist')
       dprint('Projects_hist:\n' + str(projects_hist))
       key = ''; desc = ''; action = ''
       ###### Main trigger
       flags = getArgs(projects_dict) # getArgs will add any new task to projects_dict and return the indicator of the type of argument supplied
       
       saveProjects(projects_dict,'projects_dict') # Save the projects dictionary, including any added tasks.

       # Update projects history.
       if debug: listProjects(projects_dict)
       if (flags == 'z'):
              print(ProjectsChooser(projects_dict))
       


