"""This is a adapter function that returns True if the given url is valid"""
import validators

def is_url(url: str):
  if not validators.url(url):
    return False

  return True
