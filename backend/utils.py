class Utils:
    @staticmethod
    def format_content(text):
        formated_text = ""
        if text is not None:
            lines = []
            max_width = 50
            remaining_text = text
            while len(remaining_text) > max_width:
                # Find the index of the last space within the max_width
                last_space_index = remaining_text.rfind(' ', 0, max_width)
                if last_space_index == -1:
                    # No space found within max_width, break the word
                    lines.append(remaining_text[:max_width])
                    remaining_text = remaining_text[max_width:]
                else:
                    # Split the text at the last space within max_width
                    lines.append(remaining_text[:last_space_index])
                    remaining_text = remaining_text[last_space_index + 1:]
            lines.append(remaining_text)  # Add the remaining text as the last line

            for line in lines:
                formated_text += line + "\n"
            return formated_text
        else:
            return None

    @staticmethod
    def truncate_string(string):
        if len(string) > 15:
            return string[:15] + "..."
        return string
    
    @staticmethod
    def acquire_string_input(adjective, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter {adjective.capitalize()} {info_type.capitalize()}: ").strip()
            if not user_input:
                print(f"{info_type.capitalize()} cannot be empty. Please enter valid {info_type}.")
                continue

            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                return user_input

            
    @staticmethod
    def acquire_multi_string_input(adjective, info_type):
        confirmed = False
        while not confirmed:
            user_input = input(f"Enter {adjective.capitalize()} {info_type.capitalize()} (separated by commas): ").strip()
            if not user_input:
                print(f"{info_type.capitalize()} cannot be empty. Please enter a valid {info_type}.")
                continue

            confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            while confirm_input not in ["y", "n"]:
                print("Please choose a valid option.")
                confirm_input = input(f"Accept {info_type.capitalize()}? (y/n): ").lower().strip()

            if confirm_input == "y":
                confirmed = True
                # split the input by commas and strip any extra whitespace
                word_list = [word.strip() for word in user_input.split(",") if word.strip()]
                if not word_list:
                    print(f"{info_type.capitalize()} cannot be empty after processing. Please enter valid {info_type}.")
                    confirmed = False
                    continue
                return word_list

