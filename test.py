import os
import shutil
import pylint
def main():
    """Main function"""
    print("Hello World!")
    current_time = datetime.now()
    print(f"Current time: {current_time}")
    
    data = {"message": "test"}
    print(json.dumps(data))
    
    print("Testing single file analysis...")
    v=10
    while v>3 :
        print('in while')
    x=9
    print(input())
    analyze_single_file_cli("clean_analyzer.py")
    return True
print("Testing single file analysis...")
v=10
while v>3 :
    print('in while')
x=9
print(input())
analyze_single_file_cli("clean_analyzer.py")

if __name__ == "__main__":
    main()
