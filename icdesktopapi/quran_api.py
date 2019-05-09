import os
import sqlite3

class Quran_Api():
    """
    This class is used to fetch quran data from SQLite3 database

    Methods
    -------
    get_sura_names()
        Fetches list of all sura names from database
    get_ruku_count()
        Fetches the number of rukus in the given sura
    get_ayat_range()
        Fetches the start and end ayat for the given sura and ruku
    get_ayat_text()
        Fetches the ayat text for the given sura and ruku        
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
            msg  =  "Database Error. Details: " + "Unable To Connect To The Database!."
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
        
        msg        = "Database error: Details: " + details + "."
        if last_query != "":
            msg += " Last query: " + last_query
        
        print(msg)
           
    def get_ayat_text(self, sura, ruku):
        """It fetches and returns the ayat text for the given sura and ruku
        
        Parameters
        -------
        sura
            The sura number
        ruku
            The ruku number
            
        Returns
        -------
        ayat_list
            The list of ayas
        """
        
        ayat_list = []
        data      = self.get_ayat_range(sura, ruku)
        args      = [str(sura), str(data['start']), str(data['end'])]
        
        sql       = "SELECT translated_text from `ic_quranic_text-u`"
        sql       += " where sura=?"
        sql       += " and sura_ayat_id>=?"
        sql       += " and sura_ayat_id<=?"
            
        try:
            cur       = self.conn.cursor()
            cur.execute(sql, args)
            rows      = cur.fetchall()
            for row in rows:
                ayat_list.append(row[0])
            cur.close()
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")

        return ayat_list
                
    def get_sura_names(self):
        """It fetches and returns list of all sura names from database
        
        Returns
        -------
        sura_list
            The list of sura names
        """
        
        sura_list = []
        sql       = "SELECT tname, ename from ic_quranic_suras_meta"
        
        try:
            for row in self.conn.execute(sql):
                sura_name = (row[0] + " (" + row[1] + ")")
                sura_list.append(sura_name)
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")
            
        return sura_list        
        
    def get_ruku_count(self, sura):
        """It returns the number of rukus in the given sura
        
        Parameters
        ----------
        sura : int
            The sura number
            
        Returns
        -------
        ruku_count
            The number of rukus in the given sura
        """
        
        args       = [str(sura)]
        ruku_count = 1
        sql        = "SELECT rukus from ic_quranic_suras_meta where sindex=?"
        
        try:
            cur        = self.conn.cursor()
            cur.execute(sql, args)
            row        = cur.fetchone()
            ruku_count = int(row[0])
            cur.close()            
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")
            
        return ruku_count
        
    def get_ayat_range(self, sura, ruku):
        """It returns the start and end ayat number for the given sura and ruku
        
        Parameters
        ----------
        sura : int
            The sura number
        ruku : int
            The ruku number          
            
        Returns
        -------
        ayat_data
            The start and end ayat numbers 
        """
        
        args       = [str(sura), str(ruku)]
        ayat_data  = {"start": "1", "end": "1"}
        ruku_count = 0
        sql        = "SELECT sura_ayat_id from ic_quranic_meta_data"
        sql        += " where sura=?"
        sql        += " and sura_ruku=?"
        query      = sql + " order by id asc"
        
        try:
            cur                = self.conn.cursor()
            cur.execute(query, args)
            row                = cur.fetchone()
            ayat_data['start'] = int(row[0])
            
            query              = sql + " order by id desc"
            cur                = self.conn.cursor()
            cur.execute(query, args)
            row                = cur.fetchone()
            ayat_data['end']   = int(row[0])
            cur.close()            
        except sqlite3.Error as e:
            self._display_error(e.args[0], "")            
        
        return ayat_data
