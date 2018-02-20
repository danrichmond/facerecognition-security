from urllib2 import Request, urlopen

values = """
  {
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'YOURAPPID',
  'app_key': 'YOURAPPKEY'
}
request = Request('https://api.kairos.com/gallery/view', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
