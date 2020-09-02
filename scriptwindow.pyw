import requests
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'heaveandevouror', 'password': 'r@vi1234'}
auth = requests.auth.HTTPBasicAuth('8iUjcmERT83ycw', 'uhovFSwvksFbElgoNnPpeLNf-NA')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'change wallpaper everyday'},
		  auth=auth)
d = r.json()
token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'heaveandevouror'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])