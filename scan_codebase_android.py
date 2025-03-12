import os
import datetime

# Specify the root directory of your Android project
PROJECT_DIR = "/Users/username/project"  # Replace with your project folder path
OUTPUT_FILE = f"/Users/username/output/android_project_code_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# File extensions to include (common Android project files)
INCLUDED_EXTENSIONS = (".java", ".kt", ".xml", ".gradle", ".json", ".yml", ".yaml")

def collect_project_files(project_dir):
    """Recursively collect all relevant files from the project directory."""
    code_content = []
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(project_dir):
        # Skip common directories that don't contain relevant code
        if any(ignore in root for ignore in [".git", "build", "gradle", "app/build"]):
            continue
        
        for file in files:
            # Check if the file has an included extension
            if file.endswith(INCLUDED_EXTENSIONS):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_dir)
                
                # Read the file content
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        # Add file path and content to the output
                        code_content.append(f"\n=== File: {relative_path} ===\n{content}\n")
                except Exception as e:
                    code_content.append(f"\n=== File: {relative_path} ===\n[Error reading file: {str(e)}]\n")
    
    return code_content

def save_to_file(content, output_file):
    """Save the collected content to a single text file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Generated on: {datetime.datetime.now()}\n\n")
        f.writelines(content)
    print(f"Project code saved to {output_file}")

def main():
    if not os.path.exists(PROJECT_DIR):
        print(f"Error: Directory '{PROJECT_DIR}' does not exist. Please update the PROJECT_DIR variable.")
        return
    
    print(f"Collecting code from {PROJECT_DIR}...")
    code_content = collect_project_files(PROJECT_DIR)
    save_to_file(code_content, OUTPUT_FILE)

if __name__ == "__main__":
    main()