import os
import subprocess
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

def welcome_message():
    welcome_text = "Welcome by Lothbrok9"
    for i in range(3):
        print(Fore.CYAN + Style.BRIGHT + f"\r{welcome_text}", end="")
        time.sleep(0.5)
        print(Fore.MAGENTA + Style.BRIGHT + f"\r{welcome_text}", end="")
        time.sleep(0.5)
    print("\n" + Fore.GREEN + Style.BRIGHT + "Initializing program...\n")
    time.sleep(1)

osint_tools = [
    ("1. TheHarvester", "https://github.com/laramies/theHarvester"),
    ("2. Sherlock", "https://github.com/sherlock-project/sherlock"),
    ("3. Recon-ng", "https://github.com/lanmaster53/recon-ng"),
    ("4. Amass", "https://github.com/OWASP/Amass"),
    ("5. dnsrecon", "https://github.com/darkoperator/dnsrecon"),
    ("6. OSINT-ToolKit", "https://github.com/dazz3d/OSINT-ToolKit"),
    ("7. Github Dorks", "https://github.com/techwhale/github-dorks"),
    ("8. gitrob", "https://github.com/michenriksen/gitrob"),
    ("9. SpiderFoot", "https://github.com/smicallef/spiderfoot"),
    ("10. Crt.sh", "https://github.com/gleeda/crt.sh")
]

def clone_repository(url, tool_name):
    tool_dir = tool_name.lower().replace(" ", "_")
    
    if os.path.exists(tool_dir):
        print(Fore.YELLOW + f"The tool '{tool_name}' is already installed in the current directory.")
    else:
        try:
            print(Fore.YELLOW + f"Cloning repository {url}...")
            subprocess.check_call(['git', 'clone', url])
            print(Fore.GREEN + "Cloning completed successfully!")
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error during cloning: {e}")
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")

def select_tool():
    print(Fore.CYAN + Style.BRIGHT + "Select an OSINT tool to clone:")
    
    for tool in osint_tools:
        print(Fore.YELLOW + tool[0])

    try:
        selection = int(input(Fore.GREEN + "\nEnter the number of the tool you want to clone: "))
        
        if selection < 1 or selection > len(osint_tools):
            print(Fore.RED + "Invalid selection. Choose a number between 1 and 10.")
            return None, None
        else:
            selected_name = osint_tools[selection - 1][0].split(".")[1].strip()
            selected_url = osint_tools[selection - 1][1]
            return selected_url, selected_name
    except ValueError:
        print(Fore.RED + "Error: You must enter a valid number.")
        return None, None
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        return None, None

def main():
    welcome_message()
    
    selected_url, selected_name = select_tool()
    
    if selected_url:
        clone_repository(selected_url, selected_name)
    else:
        print(Fore.RED + "No valid selection made. Exiting.")

if __name__ == "__main__":
    main()
