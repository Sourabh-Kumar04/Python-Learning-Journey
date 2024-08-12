from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient("mongodb+srv://2633:<password>@pythonyoutubemanager.mqgba.mongodb.net/")
# client = MongoClient("mongodb+srv://2633:2633>@pythonyoutubemanager.mqgba.mongodb.net/youtube_manager")
client = MongoClient("mongodb+srv://2633:2633@pythonyoutubemanager.mqgba.mongodb.net/", tlsAllowInvalidCertificates = True)
# Not a good idea to include id and password in code files

print(client)

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(F"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, 
        {'$set': {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos ")
        print("2. Add a new videos ")
        print("3. Update a videos ")
        print("4. Delete a videos ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case "3":
                video_id = input("Enter the video id to update: ")
                name = input("Enter the updated video name: ")
                time = input("Enter the updated video time: ")
                update_video(video_id, name, time)
            case "4":
                video_id = input("Enter the video id to deleted ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid Chioce ")


if __name__ == "__main__":
    main()