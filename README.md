# CLI Programming journal
#### Video Demo:  <URL HERE>

#### Description

I wanted to create a journal to keep track of what I worked on or learned each day.  I have a fairly terrible memory,
so I'm used to detailing things in various journals and calendars, just to keep my life in some semblance of order.

I love a nice, well-made paper journal.  The problem with paper, as always, is that it is time-consuming to search
through and the information stored in its pages is not easily transferable. Now that CS50P has taught me just enough
Python to be dangerous, I thought this was an easily solvable problem. 


I wanted to keep the program simple, with just a few functions:
1. enter a journal entry
2. search for entries containing an entered query
3. display all entries in the journal

+ I threw in a quote at program exit just to give me a little laugh after a programming/learning session.


#### Structure

The program is split into two main files: project.py and datamanager.py.  
+ project.py is the main program script. It handles displaying data to the user, calls functions as needed, and does a bit of file handling with quotes.json
+ datamanager.py creates a DataManager to, well, manage.  It handles all database operations and passes the data back to project.py



project.py functions:
```python
main()
    Loop through the program until the user exits

display_menu()
    Display menu of user choices

get_user_choice()
    Get user's entry from menu choices and call assigned functions

get_quote()
    Load a funny quote about programming from a JSON file

display_entries(entries)
    Display entries from journal 
```



DataManager methods:
```python
__init__()
    Connect to database. Call create_table()

create_table()
    Create journal table if one doesn't already exist

insert_entry()
    Insert new journal entry into table

search_entries(query)
    Search journal entries for query string
    
select_all_entries()
    Select all rows of the journal table
```

I waffled a bit between writing journal entries to a text file or use a database to manage them.  Obviously, the 
database won out in the end.  I don't think that I'd end up with an extremely long text file, but on the off chance 
that I continue to use the journal for a while, the safer bet was to use a database.  I chose to use SQLite3 mostly 
because it's built-in and easy to use once you get the dialect down.


#### Upgrades?
+ GUI with the CustomTkinter library?  I like using terminal commands, though, so this is my biggest undecided
+ Option to search entries by date. Could be useful on those days when I feel like I'm making no progress at all.
+ Option to display journal entries one at a time or leave as displaying all entries at once
+ Option to print selected entries to a local printer
+ Keep or remove the line clearing the terminal of the previous loop's output

#### License

Quotes provided by https://github.com/fortrabbit/quotes/blob/master/quotes.json under WTFPL license
