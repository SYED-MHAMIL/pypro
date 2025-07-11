# # x= ['masla','lemon','ginger']
# # y = enumerate(x,start = 10)
# # print(list(y))
# import json



# def load_Json():
#     try:
#         with open('youtube.txt','r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# def save_data_helper(videos):
#     with open('youtube.txt','w') as f:
#         json.dump(videos,f) 


# def list_All_Videos(vidoes):
#     for a,ob in enumerate(vidoes,start=1):
#         print(f'{a}. name :{ob['name']}  tiemestap:{ob['time']}')


# def add_list(videos):
#     v_name = input("Enter video name: ")
#     time = input("Enter video time when you will see: ")
#     videos.append({"name":v_name,"time":time})
#     save_data_helper(videos)

# def update_list(videos):
#     list_All_Videos(videos)
#     index= int(input("What index want to delete"))
#     if 1 <= index <=len(videos):
#         New_Vname = input("enter new video name")
#         time =input("enter new video Time")
#         videos[index-1]['name'] =New_Vname
#         videos[index-1]['time'] =time
#         save_data_helper(videos)


# def delete_list(videos):
#     list_All_Videos(videos)
#     index= int(input("What index want to delete"))
#     if 1 <= index <=len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
#     save_data_helper(videos)

# def main():    
#     videos = load_Json()
#     while True:
#         print('\n Youtube manager | Choose an option given below')
#         print('1. LIST A  VIDEO  VIDEO')
#         print('2. ADD A  YOUTUBE VIDEO')
#         print('3. UPDATE A YOUTUBE VIDEO DETAILED')
#         print('2. DELETE  A  YOUTUBE VIDEO DETAILED')
#         print("5. EXit  the app")        
#         choise = input("Enter your choise")
#         print(videos)
#         match choise:   
#             case "1":
#                 list_All_Videos(videos) 
#             case '2':
#                 add_list(videos)
#             case '3':
#                 update_list(videos)
#             case '4':
#                 delete_list(videos)
#             case '5':
#                 break
#             case _:
#                 print("Invalid Choise")
        
            
# if __name__ == "__main__":
#     main()
import json

def load_data():
    try:
       with open("youtube.txt",'r') as f:
          return json.load(f)
    except FileNotFoundError:
       return []
    
def save_video_handlder(video):
    with open("youtube.txt",'w') as f:
       json.dump(video,f)

def add_video(video):
    name = input("enter the name")
    time = input("enter the time")
    video.append({"name": name , "time" : time})
    save_video_handlder(video)

def list_video(video):
   for index,obj in enumerate(video,start=1):
      print(f'{index}. {obj}')
        
def update_video(video):
    list_video(video)
    index= int(input("enter the index that you want  to update")) 
    if 1<=index <= len(video):
       name = input("enter new name")
       time = input("enter new time")
       video[index-1].append({"name":name , "time": time})
       save_video_handlder(video)

   
def delete_video(video):
    list_video(video)
    index= int(input("enter the index that you want  to update")) 
    if 1<=index <= len(video):
       del video[index-1]
       save_video_handlder(video)
   

def main():
   videos = load_data()
   while True:
     print("""
        1. see the item 
        2. add the item
        3. update the item 
        4. delete the item
       """)
     num =int( input("Entere the chhoise you want"))
     match num:
        case 1:
            list_video(videos)
        case 2:
           add_video(videos)
        case 3:
           update_video(videos)
        case 4:
            delete_video(videos)
        case _:
           print("Invalid choise")
           
          

   




if __name__ == "__main__":
    main()
