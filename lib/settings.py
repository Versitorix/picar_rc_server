"""Application settings dict."""
import json

file = open('./settings/dev.json', 'r')

SETTINGS = json.load(file)
