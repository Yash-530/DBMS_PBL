import tkinter as tk
from tkinter import ttk
import mysql.connector as c # or pymysql if you prefer

# Create a database connection
db = c.connect(
    host="localhost",
    user="Pbl",
    password="Pbl@123",
    db="mydb"
)

# Create a Tkinter application window
app = tk.Tk()
app.title("Database Management")
app["bg"]= "black"

# Function to load and display data for the Category table
def load_category_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Category")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in category_tree.get_children():
        category_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        category_tree.insert("", "end", values=row)

# Function to load and display data for the Event table
def load_event_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Event")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in event_tree.get_children():
        event_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        event_tree.insert("", "end", values=row)

# Function to load and display data for the Post table
def load_post_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Post")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in post_tree.get_children():
        post_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        post_tree.insert("", "end", values=row)

# Function to load and display data for the Comment table
def load_comment_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Comment")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in comment_tree.get_children():
        comment_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        comment_tree.insert("", "end", values=row)

# Function to load and display data for the Tag table
def load_tag_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Tag")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in tag_tree.get_children():
        tag_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        tag_tree.insert("", "end", values=row)

# Function to load and display data for the Post_Has_Tag table
def load_post_has_tag_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Post_Has_Tag")
    data = cursor.fetchall()
    cursor.close()

    # Clear existing data in the treeview
    for item in post_has_tag_tree.get_children():
        post_has_tag_tree.delete(item)

    # Insert data into the treeview
    for row in data:
        post_has_tag_tree.insert("", "end", values=row)


# Create tabs for Post, Comment, Tag, and Post_Has_Tag tables
tab_control = ttk.Notebook(app)
category_tab = ttk.Frame(tab_control)
event_tab = ttk.Frame(tab_control)
post_tab = ttk.Frame(tab_control)
comment_tab = ttk.Frame(tab_control)
tag_tab = ttk.Frame(tab_control)
post_has_tag_tab = ttk.Frame(tab_control)

tab_control.add(category_tab, text='Category')
tab_control.add(event_tab, text='Event')
tab_control.add(post_tab, text='Post')
tab_control.add(comment_tab, text='Comment')
tab_control.add(tag_tab, text='Tag')
tab_control.add(post_has_tag_tab, text='Post_Has_Tag')

tab_control.pack(expand=1, fill="both")

# Create a Treeview widget for displaying Category data
category_columns = ["Category_ID", "Category_Type"]
category_tree = ttk.Treeview(category_tab, columns=category_columns, show="headings")

for col in category_columns:
    category_tree.heading(col, text=col)

category_tree.pack(pady=40)
load_category_data()

# Create a Treeview widget for displaying Event data
event_columns = ["Event_ID", "Event_Name", "Event_Organiser_Name", "Category_Category_ID"]
event_tree = ttk.Treeview(event_tab, columns=event_columns, show="headings")

for col in event_columns:
    event_tree.heading(col, text=col)

event_tree.pack(pady=40)
load_event_data()

# Create a Treeview widget for displaying Post data
post_columns = ["Post_ID", "Post_Article", "Post_Views", "Event_Event_ID", "Event_Category_Category_ID"]
post_tree = ttk.Treeview(post_tab, columns=post_columns, show="headings")

for col in post_columns:
    post_tree.heading(col, text=col)

post_tree.pack(pady=40)
load_post_data()

# Create a Treeview widget for displaying Comment data
comment_columns = ["Comment_ID", "Comment_Data", "Post_Post_ID", "Post_Event_Event_ID", "Post_Event_Category_Category_ID"]
comment_tree = ttk.Treeview(comment_tab, columns=comment_columns, show="headings")

for col in comment_columns:
    comment_tree.heading(col, text=col)

comment_tree.pack(pady=40)
load_comment_data()

# Create a Treeview widget for displaying Tag data
tag_columns = ["Tag_ID", "Tag_Word"]
tag_tree = ttk.Treeview(tag_tab, columns=tag_columns, show="headings")

for col in tag_columns:
    tag_tree.heading(col, text=col)

tag_tree.pack(pady=40)
load_tag_data()

# Create a Treeview widget for displaying Post_Has_Tag data
post_has_tag_columns = ["Post_ID", "Event_ID", "Cat_ID", "Tag_ID"]
post_has_tag_tree = ttk.Treeview(post_has_tag_tab, columns=post_has_tag_columns, show="headings")

for col in post_has_tag_columns:
    post_has_tag_tree.heading(col, text=col)

post_has_tag_tree.pack(pady=40)
load_post_has_tag_data()

# Create entry fields and labels for inserting data into Category table
category_id_label = tk.Label(category_tab, text="Category ID")
category_id_label.pack()
category_id_entry = tk.Entry(category_tab)
category_id_entry.pack()

category_type_label = tk.Label(category_tab, text="Category Type")
category_type_label.pack()
category_type_entry = tk.Entry(category_tab)
category_type_entry.pack()

# Create entry fields and labels for inserting data into Event table
event_id_label = tk.Label(event_tab, text="Event ID")
event_id_label.pack()
event_id_entry = tk.Entry(event_tab)
event_id_entry.pack()

event_name_label = tk.Label(event_tab, text="Event Name")
event_name_label.pack()
event_name_entry = tk.Entry(event_tab)
event_name_entry.pack()

event_organiser_name_label = tk.Label(event_tab, text="Event Organiser Name")
event_organiser_name_label.pack()
event_organiser_name_entry = tk.Entry(event_tab)
event_organiser_name_entry.pack()

category_category_id_label = tk.Label(event_tab, text="Category Category ID")
category_category_id_label.pack()
category_category_id_entry = tk.Entry(event_tab)
category_category_id_entry.pack()

# Create entry fields for the Post table
post_id_label = tk.Label(post_tab, text="Post ID:")
post_id_label.pack()
post_id_entry = tk.Entry(post_tab)
post_id_entry.pack()

post_article_label = tk.Label(post_tab, text="Post Article:")
post_article_label.pack()
post_article_entry = tk.Entry(post_tab)
post_article_entry.pack()

post_views_label = tk.Label(post_tab, text="Post Views:")
post_views_label.pack()
post_views_entry = tk.Entry(post_tab)
post_views_entry.pack()

event_event_id_label = tk.Label(post_tab, text="Event Event ID:")
event_event_id_label.pack()
event_event_id_entry = tk.Entry(post_tab)
event_event_id_entry.pack()

event_category_id_label = tk.Label(post_tab, text="Event Category ID:")
event_category_id_label.pack()
event_category_id_entry = tk.Entry(post_tab)
event_category_id_entry.pack()

# Create entry fields for the Comment table
comment_id_label = tk.Label(comment_tab, text="Comment ID:")
comment_id_label.pack()
comment_id_entry = tk.Entry(comment_tab)
comment_id_entry.pack()

comment_data_label = tk.Label(comment_tab, text="Comment Data:")
comment_data_label.pack()
comment_data_entry = tk.Entry(comment_tab)
comment_data_entry.pack()

comment_post_id_label = tk.Label(comment_tab, text="Post ID:")
comment_post_id_label.pack()
comment_post_id_entry = tk.Entry(comment_tab)
comment_post_id_entry.pack()

comment_event_id_label = tk.Label(comment_tab, text="Event ID:")
comment_event_id_label.pack()
comment_event_id_entry = tk.Entry(comment_tab)
comment_event_id_entry.pack()

comment_category_id_label = tk.Label(comment_tab, text="Category ID:")
comment_category_id_label.pack()
comment_category_id_entry = tk.Entry(comment_tab)
comment_category_id_entry.pack()

# Create entry fields for the Tag table
tag_id_label = tk.Label(tag_tab, text="Tag ID:")
tag_id_label.pack()
tag_id_entry = tk.Entry(tag_tab)
tag_id_entry.pack()

tag_word_label = tk.Label(tag_tab, text="Tag Word:")
tag_word_label.pack()
tag_word_entry = tk.Entry(tag_tab)
tag_word_entry.pack()

# Create entry fields for the Post_Has_Tag table
post_has_tag_post_id_label = tk.Label(post_has_tag_tab, text="Post ID:")
post_has_tag_post_id_label.pack()
post_has_tag_post_id_entry = tk.Entry(post_has_tag_tab)
post_has_tag_post_id_entry.pack()

post_has_tag_event_id_label = tk.Label(post_has_tag_tab, text="Event ID:")
post_has_tag_event_id_label.pack()
post_has_tag_event_id_entry = tk.Entry(post_has_tag_tab)
post_has_tag_event_id_entry.pack()

post_has_tag_cat_id_label = tk.Label(post_has_tag_tab, text="Cat ID:")
post_has_tag_cat_id_label.pack()
post_has_tag_cat_id_entry = tk.Entry(post_has_tag_tab)
post_has_tag_cat_id_entry.pack()

post_has_tag_tag_id_label = tk.Label(post_has_tag_tab, text="Tag ID:")
post_has_tag_tag_id_label.pack()
post_has_tag_tag_id_entry = tk.Entry(post_has_tag_tab)
post_has_tag_tag_id_entry.pack()

# Function to insert data into Category table
def insert_category_data():
    category_id = category_id_entry.get()
    category_type = category_type_entry.get()
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO Category (Category_ID, Category_Type) VALUES (%s, %s)", (category_id, category_type))
    db.commit()
    cursor.close()
    
    category_id_entry.delete(0, tk.END)
    category_type_entry.delete(0, tk.END)
    
    load_category_data()

# Button to insert data into Category table
insert_category_button = tk.Button(category_tab, text="Insert Category",fg='black',bg='gray',borderwidth=5, command=insert_category_data)
insert_category_button.pack()

# Function to insert data into Event table
def insert_event_data():
    Event_ID = event_id_entry.get()
    Event_Name = event_name_entry.get()
    Event_Organiser_Name = event_organiser_name_entry.get()
    Category_Category_ID = category_category_id_entry.get()

    cursor = db.cursor()
    cursor.execute("INSERT INTO Event (Event_ID, Event_Name, Event_Organiser_Name, Category_Category_ID) VALUES (%s, %s, %s, %s)", (Event_ID, Event_Name, Event_Organiser_Name, Category_Category_ID))
    db.commit()
    cursor.close()
    
    event_id_entry.delete(0, tk.END)
    event_name_entry.delete(0, tk.END)
    event_organiser_name_entry.delete(0, tk.END)
    category_category_id_entry.delete(0, tk.END)
    
    load_event_data()

# Button to insert data into Event table
insert_event_button = tk.Button(event_tab, text="Insert Event",fg='black',bg='gray',borderwidth=5, command=insert_event_data)
insert_event_button.pack()


# Function to insert data into Post table
def insert_post_data():
    # Get data from entry fields
    post_id = post_id_entry.get()
    post_article = post_article_entry.get()
    post_views = post_views_entry.get()
    event_event_id = event_event_id_entry.get()
    event_category_id = event_category_id_entry.get()

    # Insert data into the Post table
    cursor = db.cursor()
    cursor.execute("INSERT INTO Post (Post_ID, Post_Article, Post_Views, Event_Event_ID, Event_Category_Category_ID) VALUES (%s, %s, %s, %s, %s)",
                   (post_id, post_article, post_views, event_event_id, event_category_id))
    db.commit()
    cursor.close()

    # Clear entry fields
    post_id_entry.delete(0, tk.END)
    post_article_entry.delete(0, tk.END)
    post_views_entry.delete(0, tk.END)
    event_event_id_entry.delete(0, tk.END)
    event_category_id_entry.delete(0, tk.END)

    # Reload data in the treeview
    load_post_data()

# Create an insertion button for Post table
insert_post_button = tk.Button(post_tab, text="Insert Post", command=insert_post_data,fg='black',bg='gray',borderwidth=5)
insert_post_button.pack()

# Function to insert data into Comment table
def insert_comment_data():
    # Get data from entry fields
    comment_id = comment_id_entry.get()
    comment_data = comment_data_entry.get()
    post_post_id = comment_post_id_entry.get()
    post_event_id = comment_event_id_entry.get()
    post_category_id = comment_category_id_entry.get()

    # Insert data into the Comment table
    cursor = db.cursor()
    cursor.execute("INSERT INTO Comment (Comment_ID, Comment_Data, Post_Post_ID, Post_Event_Event_ID, Post_Event_Category_Category_ID) VALUES (%s, %s, %s, %s, %s)",
                   (comment_id, comment_data, post_post_id, post_event_id, post_category_id))
    db.commit()
    cursor.close()

    # Clear entry fields
    comment_id_entry.delete(0, tk.END)
    comment_data_entry.delete(0, tk.END)
    comment_post_id_entry.delete(0, tk.END)
    comment_event_id_entry.delete(0, tk.END)
    comment_category_id_entry.delete(0, tk.END)

    # Reload data in the treeview
    load_comment_data()

# Create an insertion button for Comment table
insert_comment_button = tk.Button(comment_tab, text="Insert Comment",fg='black',bg='gray',borderwidth=5, command=insert_comment_data)
insert_comment_button.pack()

# Function to insert data into Tag table 
def insert_tag_data():
    # Get data from entry fields
    tag_id = tag_id_entry.get()
    tag_word = tag_word_entry.get()

    # Insert data into the Tag table
    cursor = db.cursor()
    cursor.execute("INSERT INTO Tag (Tag_ID, Tag_Word) VALUES (%s, %s)",
                   (tag_id, tag_word))
    db.commit()
    cursor.close()

    # Clear entry fields
    tag_id_entry.delete(0, tk.END)
    tag_word_entry.delete(0, tk.END)

    # Reload data in the treeview
    load_tag_data()

# Create an insertion button for Tag table
insert_tag_button = tk.Button(tag_tab, text="Insert Tag", fg='black',bg='gray',borderwidth=5,command=insert_tag_data,)
insert_tag_button.pack()


# Function to insert data into Post_Has_Tag table (similar to Post)
def insert_post_has_tag_data():
    # Get data from entry fields
    post_id = post_has_tag_post_id_entry.get()
    event_id = post_has_tag_event_id_entry.get()
    cat_id = post_has_tag_cat_id_entry.get()
    tag_id = post_has_tag_tag_id_entry.get()

    # Insert data into the Post_Has_Tag table
    cursor = db.cursor()
    cursor.execute("INSERT INTO Post_Has_Tag (Post_ID, Event_ID, Cat_ID, Tag_ID) VALUES (%s, %s, %s, %s)",
                   (post_id, event_id, cat_id, tag_id))
    db.commit()
    cursor.close()

    # Clear entry fields
    post_has_tag_post_id_entry.delete(0, tk.END)
    post_has_tag_event_id_entry.delete(0, tk.END)
    post_has_tag_cat_id_entry.delete(0, tk.END)
    post_has_tag_tag_id_entry.delete(0, tk.END)

    # Reload data in the treeview
    load_post_has_tag_data()

# Create an insertion button for Post_Has_Tag table
insert_post_has_tag_button = tk.Button(post_has_tag_tab, text="Insert Post_Has_Tag",fg='black',bg='gray',borderwidth=5, command=insert_post_has_tag_data)
insert_post_has_tag_button.pack()

# ... (previous code)

# Start the Tkinter event loop
app.mainloop()

# Close the database connection when the application is closed
db.close()


# Start the Tkinter event loop
app.mainloop()

# Close the database connection when the application is closed
db.close()
