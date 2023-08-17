GREETINGS = """Hello from Telegram Bot!

Here u can upload audio files to telegram chat and
add books and chapters to database.

My commands:
/start - greetings message;
/help - get helpful info;
/add_book - add book to database;
/get_book - get book from database;
/get_chapter - get chapter from database;
"""

HELP = """Here helpful info for all command:

/start - just write this command to get starting message;
/help - just write this command to get this message;
/add_book - just write this command like that: /add_book <title> <img_link> <bg_img_link>"
/get_book - just write this command like that: /get_book <title>
/add_chapter - just upload audio file with on name id of book and title. Example: 2 Prologue
/get_chapter - just write this command like that: /get_chapter <title>
"""

ADD_BOOK_INVALID = """Invalid usage. 

Use /add_book <title> <img_link> <bg_img_link>
"""

ADD_BOOK_SUCCES = "Book inserted successfully!"

ADD_BOOK_FAILED = "Failed to insert book."

GET_BOOK_INVALID = """Invalid usage. 

Use /get_book <title>
"""

GET_BOOK_FAILED = "Book not found."

ADD_CHAPTER_NO_AUDIO = "Please upload audiofile."

ADD_CHAPTER_SUCCES = "Chapter inserted successfully!"

ADD_CHAPTER_FAILED = "Failed to insert chapter."

GET_CHAPTER_INVALID = """Invalid usage. 

Use /get_chapter <title>
"""

GET_CHAPTER_FAILED = "Chapter not found."
