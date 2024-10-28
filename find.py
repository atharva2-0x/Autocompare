import os

# Directory containing the text files
input_dir = "dummy_files"
# File to store the search results
output_file = "search_results.txt"
# Words to search for
search_words = ["dummy", "testing", "specific"]

# Clear the output file if it already exists
with open(output_file, "w") as f:
    f.write("")

# Search each file for specified words
for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    
    # Check if the file is a .txt file
    if file_name.endswith(".txt"):
        with open(file_path, "r") as file:
            content = file.read()
            found_words = []
            
            # Check if any search word is in the file
            for word in search_words:
                if word in content:
                    found_words.append(word)
                    
            # If any word is found, write to the output file
            if found_words:
                with open(output_file, "a") as output:
                    output.write(f"File: {file_name} - Found words: {', '.join(found_words)}\n")

print(f"Search completed! Results saved to '{output_file}'.")
