import requests
import json

from requests.auth import HTTPDigestAuth

################# _1_ #################

req = requests.get("https://api.github.com/users/GefMar/repos")

def repos(user, file_name):
    req = requests.get("https://api.github.com/users/"+user+"/repos")
    data = json.loads(req.text)
        
    repo_list = []
    for i in range(len(data)):
        repo_list.append(data[i]['name'])
    
    with open(file_name, 'w') as f:
        json.dump(data, f)

    print(repo_list)
    return repo_list

repos('GefMar', 'git_repo.json')

################# _2_ #################

url = 'https://httpbin.org/digest-auth/auth/user/pass'
user = 'user'
pass_= 'pass'
file_name = 'sample_js.json'
def sample_req(url, user, pass_, file_name):
    req = requests.get(url, auth=HTTPDigestAuth(user, pass_))
    data = json.loads(req.text)
    with open(file_name, 'w') as f:
        json.dump(data, f)
        
sample_req(url, user, pass_, file_name)
