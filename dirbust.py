#This script does the following:

    #It takes a URL, a wordlist file (which should contain a list of directory names to try), and an optional file extension as input.
    #It loops through the wordlist, makes an HTTP GET request to the {url}/{word_from_wordlist} for each word in the wordlist, and checks the HTTP response code.
    #If the response code is 200, it means that the directory exists, and the script prints it out.

#Remember to replace wordlist with the path to your own wordlist file. This could be a common wordlist like dirb's common wordlist, or a custom one you've created. The tool can be improved by adding error handling, support for different request types, headers, cookies, etc.

#Also, please keep in mind that using this tool on websites without proper permission is illegal and unethical. Always have explicit permission before running any kind of penetration testing tool.

#This is a basic version of a directory bruteforcing tool, and there are more robust tools out there like dirb or gobuster that do a similar job but with many more options and much faster, thanks to concurrent scanning.




import requests
import threading

def dir_bruteforcer(url, wordlist, extension=None):
    with open(wordlist, 'r') as wordlist_file:
        for line in wordlist_file:
            dir = line.strip()
            if extension:
                dir = f"{dir}.{extension}"

            target_url = f"{url}/{dir}"
            response = requests.get(target_url)

            if response.status_code == 200:
                print(f"[+] Discovered URL -- {target_url}")

url = input("Enter the URL to scan (with http/https): ")
wordlist = input("Enter the path to the wordlist file: ")
extension = input("Enter the file extension to search for (or leave blank): ")
if not extension:
    extension = None

dir_bruteforcer(url, wordlist, extension)
