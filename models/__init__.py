#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()
# Call reload() on storage to load objects from JSON file
storage.reload()
