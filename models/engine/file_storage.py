import json
from pathlib import Path
from models.base_model import BaseModel

class FileStorage:
    """Storage class responsible for processing and storing data."""

    def __init__(self, file_path="file.json"):
        self.file_path = file_path
        self.objects = {}  # Dictionary to store objects

    def all(self):
        """Return a dictionary of all objects."""
        return self.objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        """Serialize objects and write them to the JSON file."""
        serialized_objects = {}
        for key, obj in self.objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.file_path, "w") as file:
            json.dump(serialized_objects, file, indent=4)

    def reload(self):
        """Deserialize the JSON file into objects."""
        if Path(self.file_path).exists():
            with open(self.file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
            for key, obj_data in data.items():
                class_name = obj_data["__class__"]
                del obj_data["__class__"]
                obj = eval(class_name)(**obj_data)
                self.objects[key] = obj
