import os
import sys

def scan_xcode_project(directory_path, output_file="xcode_project_code.txt"):
    """
    Scan an Xcode project directory and collect source code into a single file.
    
    Args:
        directory_path (str): Path to the Xcode project directory
        output_file (str): Name of the output file to store the collected code
    """
    # Common Xcode source file extensions
    source_extensions = {'.swift', '.m', '.h', '.mm', '.cpp', '.c'}
    
    # Files and directories to ignore
    ignore_dirs = {'Pods', 'build', '.git', 'DerivedData'}
    ignore_files = {'Podfile', 'Podfile.lock'}
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Walk through directory tree
            for root, dirs, files in os.walk(directory_path):
                # Skip ignored directories
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                
                for file in files:
                    # Skip ignored files
                    if file in ignore_files:
                        continue
                    
                    file_ext = os.path.splitext(file)[1].lower()
                    
                    # Process only source files
                    if file_ext in source_extensions:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, directory_path)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                
                                # Write file info and content to output file
                                outfile.write(f"\n{'='*80}\n")
                                outfile.write(f"File: {relative_path}\n")
                                outfile.write(f"{'='*80}\n\n")
                                outfile.write(content)
                                outfile.write("\n")
                                
                            print(f"Processed: {relative_path}")
                            
                        except UnicodeDecodeError:
                            print(f"Skipped (binary or encoding issue): {relative_path}")
                        except Exception as e:
                            print(f"Error processing {relative_path}: {str(e)}")
                            
        print(f"\nScan complete! Output written to: {output_file}")
        print(f"File size: {os.path.getsize(output_file) / 1024:.2f} KB")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    # Check if directory path is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/xcode/project")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Verify directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory")
        sys.exit(1)
    
    scan_xcode_project(directory_path)

if __name__ == "__main__":
    main()