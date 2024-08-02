from backend.utils import Utils

class GenInterfaces:
    @staticmethod
    def acquire_sort_order(type):
        options = ["1","2","3","4"]
        while True:
            print(f"+-----------+-----------+---------------+------------------+")
            print(f"| 1. Newest | 2. Oldest | 3. Most Liked | 4. Most Disliked |")
            print(f"+-----------+-----------+---------------+------------------+")
            choice = input("Choose sort option: ")
            if choice not in options:
                print("Invalid Choice. Please Select a Valid Option.\n")
            else:
                if choice == "1": # Newest
                    sort_type = f"{type}_date"
                    order = "DESC"
                if choice == "2": # Oldest
                    sort_type = f"{type}_date"
                    order = "ASC"
                if choice == "3": # Most Likes
                    sort_type = "likes"
                    order = "DESC"
                if choice == "4": # Most Dislikes
                    sort_type = "dislikes"
                    order = "DESC"
                return sort_type, order
    