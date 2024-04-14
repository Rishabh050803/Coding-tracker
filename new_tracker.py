"""
Daily Coding Tracker

This program helps you track your daily coding activity, manage fines for insufficient study time, and view your coding performance over time.

Features:
- Track your daily coding activity.
- Input coding time, topic studied, and reason for insufficient study time.
- View an overview of your coding performance.
- Check your coding activity for every day.

Instructions:
1. Run the program.
2. Use the buttons to navigate between different features:
    - Instructions: Read guidelines and usage instructions.
    - Today's Data: Input your coding details for the current day.
    - Overview: View an overview of your coding performance.
    - Every Day Data: Check your coding activity for every day.
    - Customize: Customize the minimum study hours required.
    - Exit: Close the program.
3. Follow the on-screen prompts and instructions for each feature.

Author:
Rishabh Kumar Patel


Version:
1.0

Contact:
9340191803

Email:  
rishu050803@gmail.com

Disclaimer:
This program is provided as-is without any guarantees or warranties. Use it at your own risk.
"""






"""
Import Statements and Libraries

This section imports necessary modules and libraries for the application.
"""

# Importing the main tkinter module for GUI development
from tkinter import *

# Importing the themed tkinter library for advanced widget styling
from tkinter import ttk

# Importing the tkinter messagebox module for displaying message boxes
import tkinter.messagebox as msg

# Importing the pickle module for serialization and deserialization of Python objects
import pickle

# Importing the os module for interacting with the operating system
import os

# Importing the datetime module for working with dates and times
import datetime



"""
Try Block: Threshold File Handling

This block attempts to open and read the threshold file containing the minimum study time threshold.
If successful, it sets the threshold value and calculates the maximum threshold.
If the file does not exist or an exception occurs, it sets default values for the threshold and maximum threshold.
"""

try:
    # Attempt to open the threshold file for reading
    threshold_file = open("C:\\coding tracker\\treshhold.pkl", 'rb')
    
    # Load the threshold value from the file and convert it to an integer
    threshold = int(pickle.load(threshold_file))
    
    # Close the threshold file
    threshold_file.close()
    
    # Calculate the maximum threshold by adding 60 minutes to the threshold value
    max_treshhold = threshold + 60

# Handle exceptions, such as file not found or unpickling errors
except Exception as e:
    # Set default threshold value to 60 minutes
    threshold = 60
    
    # Calculate the maximum threshold using the default value
    max_threshold = threshold + 60




"""
Display a congratulatory message for putting in extra study hours.
"""

def hurray(fine):
    """
    Display a message box congratulating the user for extra study hours.
    
    Parameters:
    - fine (int): Amount of fine reduction applied to the current fine.
    """
    msg.showinfo("Hurray!", f"Great! You've put in extra study hours today.\nFine reduced by {fine}.")



"""
Customize Function

This function creates a window for users to customize the daily study time threshold.
Users can select a new threshold value from a dropdown menu and save the changes.

Parameters:
- None

Returns:
- None
"""
def Customize():
    """
    Create a window to customize the daily study time threshold.
    
    Allows users to select a new threshold value and save the changes.
    """
    
    # Function to update the label text when a new value is selected from the dropdown menu
    def on_select(event):
        selected_value = combo.get()
        label.config(text=f"Selected: {selected_value}")

    # Function to save the selected threshold value and close the window
    def save_selected():
        selected_value = combo.get()
        Customize_window.destroy()
        threshold_file = open("C:\\coding tracker\\treshhold.pkl", 'wb')
        pickle.dump(int(selected_value), threshold_file)
        threshold_file.close()
        msg.showinfo("Updated", f"Minimum value changed to {int(selected_value)} minutes.")

    # Create a new Tkinter window for customization
    Customize_window = Tk()
    Customize_window.geometry("300x300")
    Customize_window.minsize(300, 250)
    Customize_window.maxsize(300, 250)
    Customize_window.title("Customize Daily Target Window")

    # Load the current threshold value from the file
    threshold_file = open("C:\\coding tracker\\treshhold.pkl", 'rb')
    threshold = pickle.load(threshold_file)
    threshold_file.close()

    # Create a label to display the current threshold value
    label = Label(Customize_window, text=f"Selected - {threshold}")
    label.pack(pady=10)

    # Options for the dropdown menu
    options = ['60', '90', '120', '150', '180', '210', '240', '270', '300', '330', '360']

    # Create a combobox with predefined options and set the current threshold value as default
    combo = ttk.Combobox(Customize_window, values=options, state="readonly")
    combo.set(f'{threshold}')
    combo.pack(pady=10)
    combo.bind("<<ComboboxSelected>>", on_select)

    # Button to save the selected value and close the window
    save_button = Button(Customize_window, text='Update', command=save_selected)
    save_button.pack(pady=10)

    # Start the Tkinter event loop
    Customize_window.mainloop()



"""
Backup Data

This section attempts to create a backup of the coding tracker data file.
If successful, it saves a copy of the current data into a separate file for backup.

Parameters:
- None

Returns:
- None
"""
try:
    # Attempt to open the coding tracker data file for reading
    task_file = open("C:\\coding tracker\\coding_tracker.pkl", "rb")
    
    # Load the data from the file
    data = pickle.load(task_file)
    
    # Close the file after reading
    task_file.close()
    
    # Attempt to open a new file for writing as backup
    task_file = open("C:\\coding tracker\\backup.pkl", "wb")
    
    # Dump the loaded data into the backup file
    pickle.dump(data, task_file)
    
    # Close the backup file after writing
    task_file.close()

# Handle exceptions, such as file not found or unpickling errors
except Exception as e:
    # If any exception occurs, do nothing and continue
    pass


"""
First Time Setup

This section checks if the coding tracker data file exists. If it doesn't, it creates a new file
and initializes it with default data. It also creates a separate file for storing the threshold value.

Parameters:
- None

Returns:
- None
"""

if not os.path.exists("C:\\coding tracker\\coding_tracker.pkl"):
    # Create the directory if it doesn't exist
    os.mkdir("C:\\coding tracker")
    
    # Open a new file for the coding tracker data and initialize it with default data
    task_file = open("C:\\coding tracker\\coding_tracker.pkl", "wb")
    daily_data = [{'date': 0, "time": 0, "time_coded": 0, 'topic': 0, "fine": 0, 'reason': 0}]
    pickle.dump(daily_data, task_file)
    task_file.close()
    
    # Create a separate file for storing the threshold value and set it to a default value of 60
    threshold_file = open("C:\\coding tracker\\treshhold.pkl", 'wb')
    pickle.dump(60, threshold_file)
    threshold_file.close()
    
    # Show a welcome message to the user
    msg.showinfo("Welcome", "Welcome to CodePulse!\n\nFor the best experience, we recommend checking the instructions for first-time use.")


"""
Load Data

This section retrieves the current date and time, and then loads the coding tracker data from a file.

Parameters:
- None

Returns:
- date_time: Current date and time as a datetime object.
- cur_date: Current date as a datetime object.
- data: Loaded coding tracker data as a list of dictionaries.
"""

# Retrieve the current date and time
date_time = datetime.datetime.now()
cur_date = datetime.datetime.now()

# Open the coding tracker data file for reading
task_file = open("C:\\coding tracker\\coding_tracker.pkl", "rb")

# Load the data from the file
data = pickle.load(task_file)

# Close the file after loading
task_file.close()


"""
Forgotten Days

This section handles the scenario where there are forgotten days with no recorded coding activity.
It calculates the number of forgotten days, creates entries for each forgotten day with no coding activity,
and appends them to the coding tracker data.

Parameters:
- data: Loaded coding tracker data as a list of dictionaries.
- cur_date: Current date as a datetime object.

Returns:
- None
"""

# Check if there are at least two entries in the data list
if len(data) >= 2:
    count = 0
    
    # Calculate the number of forgotten days by iterating backwards from the current date
    while cur_date.date() != data[-1]['date']:
        count += 1
        cur_date -= datetime.timedelta(days=1)

    # Reset the current date to the current datetime
    cur_date = datetime.datetime.now()
    j = 1
    
    # Iterate over the range of forgotten days and create entries for each day
    for i in range(count - 1, 0, -1):
        j += 1
        cur_date -= datetime.timedelta(days=i)
        fill = {
            'date': cur_date.date(),
            'time': cur_date.time(),
            'time_coded': 0,
            'topic': 'No study',
            'fine': 40 * j // 2,
            'reason': 'forgotten'
        }
        
        # Append the new entry to the coding tracker data
        data.append(fill)
        
        # Reset the current date to the current datetime
        cur_date = datetime.datetime.now()

# Open the coding tracker data file for writing
task_file = open("C:\\coding tracker\\coding_tracker.pkl", "wb")

# Save the updated data back to the file
pickle.dump(data, task_file)

# Close the file after writing
task_file.close()


"""
Feed Data

This function adds today's coding activity data to the coding tracker file.

Parameters:
- time_coded: Amount of time spent coding today, in minutes.
- topic: Brief description of the coding topic studied today.
- reason: Reason for not meeting the minimum study hours, if applicable.

Returns:
- None
"""

def feed_data(time_coded, topic, reason):
    # Open the coding tracker data file for reading
    file = open("C:\\coding tracker\\coding_tracker.pkl", 'rb')
    
    # Load the existing data from the file
    data = pickle.load(file)
    
    # Close the file after loading
    file.close()

    # Calculate the fine for today's coding activity
    fine = fine_calculator(time_coded, reason)
    
    # Create a dictionary containing today's coding activity data
    fill = {
        'date': cur_date.date(),
        'time': cur_date.time(),
        'time_coded': time_coded,
        'topic': topic,
        'fine': fine,
        'reason': reason
    }
    
    # Append the new data to the existing data list
    data.append(fill)
    
    # Open the coding tracker data file for writing
    file = open("C:\\coding tracker\\coding_tracker.pkl", 'wb')
    
    # Save the updated data back to the file
    pickle.dump(data, file)
    
    # Close the file after writing
    file.close()
    
    # Display a message indicating successful saving
    msg.showinfo("SAVED", "Saved Successfully")



"""
Fine Calculator

This function calculates the fine for the coding activity based on the time studied and the reason for not meeting the minimum study hours.

Parameters:
- time_studied: Amount of time spent coding, in minutes.
- reason: Reason for not meeting the minimum study hours. Default is "nil".

Returns:
- Fine amount calculated based on the time studied and reason.
"""

def fine_calculator(time_studied, reason="nil"):
    fine = 1  # Default fine value
    
    # Open the coding tracker data file for reading
    file = open("C:\\coding tracker\\coding_tracker.pkl", "rb")
    
    # Load the existing data from the file
    data = pickle.load(file=file)
    
    # Close the file after loading
    file.close()

    # Check if the number of records is less than or equal to 8
    if len(data) <= 8:
        # Check if the time studied is within the threshold range
        if threshold <= time_studied <= max_treshhold:
            return 0  # No fine if the time studied is within the threshold range
        
        # Check if there is a reason provided
        if str(reason) != 'nil':
            return 0  # No fine if there is a reason provided
        
        # Check if the time studied is below the threshold and above 30 minutes
        if threshold > time_studied >= 30:
            return threshold - time_studied  # Calculate the fine based on the time difference
        
        # Check if the time studied exceeds the maximum threshold
        elif time_studied > max_treshhold:
            hurray(((time_studied - max_treshhold) * (1.5)))  # Display a message for extra study hours
            return -((time_studied - max_treshhold) * (1.5))  # Calculate the fine for exceeding the maximum threshold
        
        else:
            return 30  # Default fine if other conditions are not met
    
    else:
        work_list = []
        # Retrieve the time coded data for the last 8 days
        for i in range(-1, -9, -1):
            work_list.append(data[i]['time_coded'])

        work_behind = 0

        # Calculate the number of days behind the threshold
        for i in range(8):
            if work_list[i] >= threshold:
                break
            else:
                work_behind += 1

        # Update the fine based on the number of days behind the threshold
        if work_behind <= 1:
            fine = 1
        elif work_behind == 2:
            fine = 1.5
        elif work_behind == 3:
            fine = 2
        elif work_behind == 4:
            fine = 2.5
        elif work_behind <= 7:
            fine = 3
        else:
            fine = 5

        work_behind = 0

        # Check if the time studied is within the threshold range
        if threshold <= time_studied <= max_treshhold:
            return 0  # No fine if the time studied is within the threshold range
        
        # Check if there is a reason provided
        if reason != 'nil':
            return 0  # No fine if there is a reason provided
        
        # Check if the time studied is below the threshold and above 30 minutes
        if threshold > time_studied >= 30:
            return (threshold - time_studied) * fine  # Calculate the fine based on the time difference
        
        # Check if the time studied exceeds the maximum threshold
        elif max_treshhold + 60 >= time_studied > max_treshhold:
            hurray(((time_studied - max_treshhold) * (1.5)))  # Display a message for extra study hours
            return -((time_studied - max_treshhold) * (1.5))  # Calculate the fine for exceeding the maximum threshold
        
        # Check if the time studied exceeds the maximum threshold by more than 60 minutes
        elif time_studied > max_treshhold + 60:
            hurray(((time_studied - max_treshhold) * (2)))  # Display a message for extra study hours
            return -((time_studied - max_treshhold) * (2))  # Calculate the fine for exceeding the maximum threshold
        
        else:
            return (threshold // 2) * fine  # Default fine if other conditions are not met



def instructions():
    """
    Display Instructions

    This function displays instructions for using the CodePulse coding activity manager.

    Parameters:
    - None

    Returns:
    - None
    """

    # Create a new window for instructions
    instruction_window = Tk()
    instruction_window.geometry('900x600')
    instruction_window.maxsize(900, 600)
    instruction_window.minsize(900, 600)
    instruction_window.title('Instructions')
    instruction_window.config(bg='gray10')

    # Text containing the instructions
    instructions_text = (
        "              Welcome to the CodePulse !\n\n"
        "Track and boost your coding skills with daily coding activity manager.\n\n"
        "Instructions:\n"
        "1. Code for a minimum of 60 minutes every day.\n"
        "2. Failure to meet the daily minimum or forgetting to log will result in fines based on your history.\n"
        "3. If you code for more than 180 minutes, fines will be reduced.\n"
        "4. Logging twice a day is not allowed.\n"
        "5. You can customize the minimum study hours, but it must not be below 60 minutes.\n"
        "6. Increasing the minimum study hours will raise the rewarding limit.\n\n"
        "Usage:\n"
        "1. Click on 'Today's Data' to input your coding details.\n"
        "2. Enter coding time and a brief topic description.\n"
        "3. If you fall short of the minimum study hours, provide a reason.\n"
        "4. Click 'Save' to store your coding data.\n"
        "5. View your data in 'Every Day Data'.\n"
        "6. 'Overview' provides an overview of your coding performance.\n\n"
        "Tips:\n"
        "- Consistently update your coding data for accurate monitoring.\n"
        "- Keep coding and enhance your skills!\n\n"
    )

    # Function to close the instruction window
    def Exit():
        instruction_window.destroy()

    # Label to display instructions
    instructions_label = Label(instruction_window, text=instructions_text, bg='gray10', fg='deep sky blue',
                               font="lucida 13 ", justify='left', padx=20, pady=20,)
    instructions_label.pack(side='top')

    # Button to exit the instruction window
    Button(instruction_window, text='   Exit   ', command=Exit, height=3, width=15, bg='gray15', fg='snow').pack()

    instruction_window.mainloop()



def todays_data():
    """
    Input Today's Coding Data

    This function allows users to input their coding data for the current day.

    Parameters:
    - None

    Returns:
    - None
    """

    # Function to create a window for inputting daily coding data
    entry_window = Tk()
    entry_window.geometry('500x600')
    entry_window.maxsize(600, 300)
    entry_window.minsize(600, 300)
    entry_window.config(bg='gray10')

    # Function to validate input for time coded
    def is_digit_or_backspace(char):
        return char.isdigit() or char == '\b'  # '\b' represents the backspace character

    def on_validate(P):
        return all(is_digit_or_backspace(char) for char in P)

    # Function to retrieve values and show a new window for reason if coding time is insufficient
    def get_values():
        coding_time_value.set(int(coding_time.get()))
        topic_value.set(topic.get())
        entry_window.destroy()
        valid = False

        # Check if coding time is insufficient and ask for a reason if true
        if coding_time_value.get() < threshold:
            valid = msg.askyesno('Poor Performance', 'Is there a valid reason for not fulfilling the minimum study hours for today?')

        if valid:
            # Function to get the reason for insufficient coding time
            def get_reason():
                reason_value.set(reason.get())
                reason_window.destroy()
                # Check if it's a double entry for the same day
                if date_time.date() == data[-1]["date"]:
                    msg.showerror("Double Entry", "You cannot save data twice in a day")
                else:
                    feed_data(coding_time_value.get(), topic_value.get(), reason_value.get())

            # Create a window for entering the reason
            reason_window = Tk()
            reason_window.geometry('300x100')
            reason_window.maxsize(height=200, width=800)
            reason_window.minsize(height=200, width=300)
            reason_window.title("Poor Performance")
            reason_window.config(bg='gray10')

            Label(reason_window, text='Write the reason', bg='gray10', fg='deep sky blue', font="lucida 13 ",
                  pady=10).pack()
            reason = Entry(reason_window, width=100)
            reason.pack(padx=30)

            Button(reason_window, text='Save', command=get_reason).pack(pady=20)
            reason_window.mainloop()

        else:
            reason_value.set("nil")
            # Check if it's a double entry for the same day
            if date_time.date() == data[-1]["date"]:
                msg.showerror("Double Entry", "You cannot save data twice in a day")
            else:
                feed_data(coding_time_value.get(), topic_value.get(), reason_value.get())

    coding_time_value = IntVar()
    topic_value = StringVar()
    reason_value = StringVar()

    # Entry widgets for coding time, topic, and reason
    Label(entry_window, text='How much time did you study ', bg='gray10', fg='deep sky blue', font="lucida 13 ", pady=10).pack()
    coding_time = Entry(entry_window, width=35, validate="key", validatecommand=(entry_window.register(on_validate), "%P"),
                        textvariable=coding_time_value)
    coding_time.insert(0, '00')
    coding_time.pack()

    Label(entry_window, text='Topic studied', bg='gray10', fg='deep sky blue', font="lucida 13 ", pady=10).pack()
    topic = Entry(entry_window, width=35, textvariable=topic_value)
    topic.insert(0, 'No Study')
    topic.pack()

    Label(entry_window, text='', bg='gray10', fg='deep sky blue', font="lucida 13 ", pady=10).pack()
    Button(entry_window, text='Save', command=get_values).pack()

    entry_window.mainloop()



def totals():
    """
    Display Totals and Performance Tables
    
    This function creates a window to display totals related to coding activity,
    including total study time, total fine, days with poor performance, days with no coding, and days with extra work.
    It also creates two tables to display poor performance and above performance based on predefined thresholds.

    Parameters:
        None

    Returns:
        None
    """
    total_window=Tk()
    total_window.title("totals")
    total_window.geometry("600x300")
    total_window.minsize(750,300)
    total_window.maxsize(750,400)
    upper_frame=Frame(total_window,background='gray',borderwidth=3)
    upper_frame.pack(side='top',fill=X)
    task_file=open("C:\\coding tracker\\coding_tracker.pkl","rb")
    data=pickle.load(task_file)
    task_file.close()
    zero_work=0
    total_fine=0
    over_work=0
    poor_peformace=0
    total_Study_time=0
    for i in range(1,len(data)):
        if data[i]['time_coded']==0:
            zero_work+=1
        if data[i]['time_coded']>=180:
            over_work+=1
        if data[i]['time_coded']<threshold:
            poor_peformace+=1
        total_Study_time+=data[i]['time_coded']
        total_fine+=data[i]['fine']

    text = f'''
Total Study Time  :   {total_Study_time} minutes\n
Total Fine  :   {total_fine}\n
Days with poor performace  :   {poor_peformace}\n
Days with No Coding  :   {zero_work}\n
Days with Extra Work  :   {over_work}\n'''
    label=Label(upper_frame,text=text,background='gray10',foreground='white',)
    label.pack(fill='both')


    bottomeFrame=Frame(total_window,background='pink')
    bottomeFrame.pack(side='bottom',fill=BOTH)

    left_frame=Frame(bottomeFrame,background='black',borderwidth=3)
    left_frame.pack(fill='both',side='left')
    label=Label(left_frame,text="\tpoor performace table  \t\t")
    label.pack()
    tree1=ttk.Treeview(left_frame,columns=('Date','time coded','fine',))
    tree1['show']='headings'
    tree1.heading('Date',text='Date',anchor='center')
    tree1.heading('time coded',text='time coded',anchor='center')
    tree1.heading('fine',text='fine',anchor='center')
    tree1.column('Date',anchor='center',width=15)
    tree1.column('time coded',anchor='center',width=10)
    tree1.column('fine',anchor='center',width=10)
    for i in range(1,len(data)):
        if data[i]['time_coded']<threshold or data[i]['fine']>0:
            tree1.insert('',1,values=(data[i]['date'],data[i]['time_coded'],data[i]['fine']))
    scrollbar1=ttk.Scrollbar(left_frame,orient='vertical',command=tree1.yview)
    tree1.configure(yscrollcommand=scrollbar1.set)
    scrollbar1.pack(side='right',fill=Y)
    tree1.pack(expand=True,fill=BOTH)    

    
    right_frame=Frame(bottomeFrame,background='gray5',borderwidth=3)
    right_frame.pack(fill='both',side='right')  
    label=Label(right_frame,text="\t\t\t\tabove performace table\t\t\t\t\t")
    label.pack() 
    tree2=ttk.Treeview(right_frame,columns=('Date','time coded','topic','fine',))
    tree2['show']='headings'
    tree2.heading('Date',text='S.No.',anchor='center')
    tree2.heading('time coded',text='time coded',anchor='center')
    tree2.heading('topic',text='topic',anchor='center')
    tree2.heading('fine',text='fine',anchor='center')
    tree2.column('Date',anchor='center',width=10)
    tree2.column('time coded',anchor='center',width=10)
    tree2.column('topic',anchor='center')
    tree2.column('fine',anchor='center',width=10)
    for i in range(1,len(data)):
        if data[i]['time_coded']>max_treshhold and data[i]['fine']<=0:
            tree2.insert('',1,values=(data[i]['date'],data[i]['time_coded'],data[i]['topic'],data[i]['fine']))
    scrollbar2=ttk.Scrollbar(right_frame,orient='vertical',command=tree2.yview)
    tree2.configure(yscrollcommand=scrollbar2.set)
    scrollbar2.pack(side='right',fill=Y)
    tree2.pack(expand=True,fill=BOTH) 
    total_window.mainloop()




def Every_day_data():
    """
    Display Every Day Data

    This function creates a window to display data for each day including the date, duration of study,
    topic studied, fine, and reason.

    Parameters:
    - None

    Returns:
    - None
    """

    # Create the data window
    data_window = Tk()
    data_window.title("Every Day Data")

    # Create a Treeview widget for displaying the data
    tree = ttk.Treeview(data_window, columns=("S.No.", 'Date', "Duration of study", "Topic", "Fine", "Reason"))
    tree['show'] = "headings"

    # Define column headings
    tree.heading('S.No.', text='ID', anchor='center')
    tree.heading('Date', text='Date', anchor='center')
    tree.heading('Duration of study', text='Duration of study', anchor='center')
    tree.heading('Topic', text='Topic', anchor='center')
    tree.heading('Fine', text='Fine', anchor='center')
    tree.heading('Reason', text='Reason', anchor='center')

    # Define column widths
    tree.column('S.No.', anchor='center', width=10)
    tree.column('Date', anchor='center', width=10)
    tree.column('Duration of study', anchor='center', width=10)
    tree.column('Topic', anchor='center')
    tree.column('Fine', anchor='center', width=10)
    tree.column('Reason', anchor='center')

    # Read data from the file
    task_file = open("C:\\coding tracker\\coding_tracker.pkl", "rb")
    data = pickle.load(task_file)
    task_file.close()

    # Insert data into the Treeview
    for i in range(1, len(data)):
        tree.insert('', i, values=(f'{i}', f'{data[i]["date"]}', f'{data[i]["time_coded"]}', f'{data[i]["topic"]}',
                                   f"{data[i]['fine']}", f"{data[i]['reason']}"))

    # Add scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(data_window, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill=Y)
    tree.pack(expand=True, fill=BOTH)

    data_window.mainloop()



#funciton for exit
def Exit():
    about_window.destroy()
    exit()



# Create the main window
about_window = Tk()
about_window.geometry('600x200+300+100')
about_window.maxsize(750, 200)
about_window.minsize(750, 200)
about_window.config(bg='gray10')
about_window.title("Daily Coding Tracker")

# Label for the title
title_label = Label(about_window, text='Daily Coding Tracker', bg='gray10', fg='deep sky blue', font="lucida 15 bold")
title_label.pack(pady=10)

# Frame for buttons
button_frame = Frame(about_window, bg='gray10')
button_frame.pack(pady=15)

# Buttons for different functionalities
btn_instructions = Button(button_frame, text='Instructions', command=instructions, width=15, height=2, bg='gray15', fg='snow')
btn_instructions.grid(row=0, column=0, padx=10)

btn_todays_data = Button(button_frame, text='Today\'s Data', command=todays_data, width=15, height=2, bg='gray15', fg='snow')
btn_todays_data.grid(row=0, column=1, padx=10)

btn_totals = Button(button_frame, text='Overview', command=totals, width=15, height=2, bg='gray15', fg='snow')
btn_totals.grid(row=0, column=2, padx=10)

btn_every_day_data = Button(button_frame, text='Every Day Data', command=Every_day_data, width=15, height=2, bg='gray15', fg='snow')
btn_every_day_data.grid(row=0, column=3, padx=10)

btn_customize = Button(button_frame, text="Customize", command=Customize, width=15, height=2, bg='gray15', fg='snow')
btn_customize.grid(row=0, column=4, padx=10)

btn_exit = Button(button_frame, text="Exit", command=Exit, width=15, height=2, bg='gray15', fg='snow')
btn_exit.grid(row=1, column=2, padx=10, pady=20)

about_window.mainloop()
