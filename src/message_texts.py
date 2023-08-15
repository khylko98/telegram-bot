GREETINGS = """Hello from Telegram Bot!

Here u can upload audio files to telegram chat and
add books and chapters to database.

My commands:
/start - greetings message;
/help - get helpful info;
/get_audio_link - get link to audiofile by file_id;
/add_book - add book to database;
/get_book - get book from database;
/add_chapter - add chapter to database (need book_id);
/get_chapter - get chapter from database;
"""

HELP = """Here helpful info for all command:

/start - just write this command to get starting message;
/help - just write this command to get this message;
...
"""  # TODO: write description for future commands;

ADD_BOOK_INVALID = """Invalid usage. 

Use /add_book <title> <img_link> <bg_img_link>
"""

ADD_BOOK_SUCCES = """Book inserted successfully!"""

ADD_BOOK_FAILED = """Failed to insert book."""
