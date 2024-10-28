import os

# Directory to store text files
output_dir = "dummy_files"
os.makedirs(output_dir, exist_ok=True)

# Dummy text content
dummy_text = "This is a dummy text file for testing purposes."

# Create 100 text files with dummy text
for i in range(1, 101):
    file_path = os.path.join(output_dir, f"file_{i}.txt")
    with open(file_path, "w") as file:
        file.write(dummy_text)
        
print("100 text files created with dummy text!")
