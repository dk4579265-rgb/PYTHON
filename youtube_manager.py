
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    print("\n" + "*"*70)
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. Title: {video['title']}, Duration: {video['time']}")
    print("*"*70 + "\n")

def add_video(videos):
    title = input("Enter video title: ")
    time = input("Enter video duration: ")
    videos.append({'title': title, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the number of the video to update: "))
    if 1 <= index <= len(videos):
        title = input("Enter new video title: ")
        time = input("Enter new video duration: ")
        videos[index - 1] = {'title': title, 'time': time}
        save_data_helper(videos)
        print("Video updated successfully!")
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the number of the video to delete: "))
    if 1 <= index <= len(videos):
        videos.pop(index - 1)
        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid index selected")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()



  
