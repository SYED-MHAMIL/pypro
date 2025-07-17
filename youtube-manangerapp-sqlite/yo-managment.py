import sqlite3
con = sqlite3.Connection('youtube_videos.db')

cur = con.cursor()
# create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL ,
             time TEXT NOT NULL
            )
''')
con.commit()
print("database created")

def add_data():
     try:
        name = input("enter the video name")
        time = input("enter the video time")
        cur.execute('INSERT INTO videos (name,time) VALUES (?, ?)',(name,time) )
        con.commit()
     except sqlite3.IntegrityError as e :
          print(f'something wen wrong {e}')
          
def delete_Data():
    id = input("enter your id what you wanto deleted")
    cur.execute('DELETE FROM videos WHERE id= ?',id)
    con.commit()
def updatedata():
    read_Data()
    id = input('which you want to edit video so give id')
    name = input(' enter new  name') 
    time = input(' enter new  time')
    cur.execute('UPDATE videos SET name = ?,time = ? WHERE id = ?',(name,time,id)) 
    con.commit()
def read_Data():
    cur.execute("SELECT * FROM videos")
    videos = cur.fetchall()
    for id,name,time in videos:
        print(f" the id of {id} your movie {name} and also time is {time}")

def close_dataConnection():
    con.close() 



def main():
    while True:
            print("""
        1. for add
        2. for read .
        3. for update.
        4. for  delete .
        5. for quit
                
    """)
            try:
                n= int(input("what you want to operation"))
            except ValueError as e:
                    print("you just give integer!")
                    continue
            match n:
                  case 1:
                       add_data()
                    
                  case 2:
                      read_Data()
                  case 3:
                      updatedata()
                  case 4:
                      delete_Data()
                  case 5:
                      break
                  case _:
                      print("invalid choise")

    close_dataConnection()
                      
                    
            
       
if __name__ == "__main__":
     main()
              
              
              
              
         