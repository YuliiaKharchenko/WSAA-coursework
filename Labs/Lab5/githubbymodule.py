# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg


apikey = cfg["Forlab5"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
  #print(repo.name)

# make sure this replository exists, and that the path is correct
repo = g.get_repo("YuliiaKharchenko/aprivateone")
# print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)
'''
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)
newContents = contentOfFile + " more stuff 2 \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
'''
