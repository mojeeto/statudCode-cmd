from urllib import request
import requests as req
import sys

link = sys.argv[1]

statusCode = req.get(link).status_code

print(statusCode)
