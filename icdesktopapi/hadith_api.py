import os
import sqlite3

class Hadith_Api():
    """
    This class is used to fetch hadith data from SQLite3 database

    Methods
    -------
    get_source_list()
        Fetches list of all hadith sources from database
    get_book_list()
        Fetches list of all hadith books for the given
        source from database
    get_title_list()
        Fetches list of all hadith books and titles for given
        source from database
    get_hadith_text()
        Fetches the hadith text for the given source and book
    """
    
    def __init__(self, db_path):
        """It creates a connection to the SQLite3 database
 
        Parameters
        -------
        db_path
            The absolute path to the database
        """

        try:
            self.conn  = sqlite3.connect("file:" + db_path + "?mode=ro", uri = True)
        except sqlite3.Error as e:
            msg  =  "Database Error" + "Unable To Connect To The Database!."
            msg += " Db path: " + db_path
            msg += " Details: " + e.args[0]
            self._display_error(msg, "")

    def _display_error(self, details, last_query):
        """It displays the given error message.
        It appends the last error to the message
        
        Parameters
        -------
        details
            The error details
        last_query
            The last sql query
        """
        
        msg        = "Database error. Details: " + details + "."
        if last_query != "":
            msg += " Last query: " + last_query
        
        print(msg)
                
    def get_source_list(self):
        """It fetches and returns list of all hadith sources from database
        
        Returns
        -------
        source_list
            The list of hadith sources
        """
        
        source_list = []
        sql         = "SELECT DISTINCT source from ic_hadith_books_urdu"
        
        try:
            for row in self.conn.execute(sql):
                source_list.append(row[0])
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")
            
        return source_list
        
    def get_book_list(self, source):
        """It fetches and returns list of all hadith books in the given source
        
        Parameters
        -------
        source
            The hadith source
            
        Returns
        -------
        book_list
            The list of hadith books
        """
        
        book_list = []
        args      = [source]
        
        sql       = "SELECT id, book from ic_hadith_books_urdu"
        sql       += " where source=? group by book"
        
        try:
            cur       = self.conn.cursor()
            cur.execute(sql, args)
            rows      = cur.fetchall()
            for row in rows:
                book = [row[0], row[1]]
                book_list.append(book)
            cur.close()
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")

        return book_list
        
    def get_title_list(self, book):
        """It fetches and returns list of hadith titles for the given book
        
        Parameters
        -------
        book
            The hadith book id    
         
        Returns
        -------
        title_list
            The list of hadith titles
        """
        
        title_list = []
        args       = [book]
        
        sql       = "select id, title from ic_hadith_urdu where book_id=?"
        
        try:
            cur       = self.conn.cursor()
            cur.execute(sql, args)
            rows      = cur.fetchall()
            for row in rows:
                title = [row[0], row[1]]
                title_list.append(title)
            cur.close()
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")

        return title_list
        
    def get_hadith_text(self, hadith_id):
        """It fetches and returns the hadith text for the given hadith id
        
        Parameters
        -------
        hadith_id
            The hadith id   
         
        Returns
        -------
        hadith_text
            The hadith text
        """
        
        hadith_text = ""
        args        = [int(hadith_id)]
        
        sql         = "select hadith_text from ic_hadith_urdu where id=?"
        
        try:
            cur       = self.conn.cursor()
            cur.execute(sql, args)
            row       = cur.fetchone()
            hadith_text = row[0]
            cur.close()
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")

        return hadith_text
