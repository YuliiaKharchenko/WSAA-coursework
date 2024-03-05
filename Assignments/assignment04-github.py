# The program reads a file from a repository, and then replaces all the instances of the text "Andrew" with the name "Yuliia", 
# then commits those changes and pushes the file back to the repository. Authorisation is used. 


from github import Github
import requests
from config import config as cfg 
 

apikey = cfg["Keyforrepo4"]

g = Github(apikey)
#for repo in g.get_user().get_repos():
  #print(repo.name)

repo = g.get_repo("YuliiaKharchenko/4assignment4")

fileInfo = repo.get_contents("Replace.txt")

urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

# print (contentOfFile) # print old content 

newContent = contentOfFile.replace("Andrew","Yuliia") # replace the text fragment "Andrew" with my name.

# print (newContents) # print out new content 

updatedrepocontent=repo.update_file(fileInfo.path, "Assignment4 done", newContent, fileInfo.sha)

print (updatedrepocontent) # print out the result to check (commit:sha, content:path)