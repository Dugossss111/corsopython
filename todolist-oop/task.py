
import uuid
from tag import Tag, TagLibrary
from category import Category

class Task:
    def __init__(self, title):
        self.id = str(uuid.uuid4())
        self.set_title(title) 
        self.isComplete = False
        self.tag_list : list[Tag] = []
        self.category: Category = None


    
    def get_id_(self):
        """Return the task id"""
        return self.id

    def get_title(self) -> str:
        """Return the task title"""
        return self.title
    
    def set_title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("new_title must be a str instance.") 
        
        if  not new_title or not new_title.strip():
            raise ValueError("new_title should not be empty.")

        self.title = new_title

    def add_tag(self, name: str, color: str, tag_library: TagLibrary):
        """Add a tag to the task, using the provided TagLibrary to ensure uniqueness."""
        tag = tag_library.add_tag(name, color)
        if tag not in self.tag_list:
            self.tag_list.append(tag)

    def remove_tag(self, tag_id: str):
        self.tag_list = [t for t in self.tag_list if t.get_id() != tag_id]

    def set_category(self, category: Category):
        self.category = category
