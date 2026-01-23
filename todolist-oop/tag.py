import uuid

class Tag:
    def __init__(self, name: str, color: str, category_id: str = None):
        self.id = str(uuid.uuid4())
        self.set_name(name)
        self.set_color(color)
        self.category_id = category_id

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a str instance.")
        if not name or not name.strip():
            raise ValueError("name should not be empty.")
        self.name = name

    def set_color(self, color: str):
        if not isinstance(color, str):
            raise TypeError("color must be a str instance.")
        if not color or not color.strip():
            raise ValueError("color should not be empty.")
        self.color = color

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name
    
    def get_color(self) -> str:
        return self.color


class TagLibrary:
    def __init__(self):
        self.tags: list[Tag] = []

    def add_tag(self, name: str, color: str, category_id: str = None) -> Tag:
        """Create a new tag if it doesn't exist, otherwise return existing one (based on name)."""
        # Check if tag with same name already exists
        for tag in self.tags:
            if tag.get_name() == name:
                 # Logic for "If the tag already exists inside the tag libray, should not be duplicated."
                 # We return the existing tag.
                 return tag
        
        new_tag = Tag(name, color, category_id)
        self.tags.append(new_tag)
        return new_tag

    def remove_tag(self, tag_id: str):
        self.tags = [t for t in self.tags if t.get_id() != tag_id]

    def update_tag(self, tag_id: str, name: str = None, color: str = None):
        for tag in self.tags:
            if tag.get_id() == tag_id:
                if name:
                    tag.set_name(name)
                if color:
                    tag.set_color(color)
                return
        raise ValueError(f"Tag with id {tag_id} not found.")

    def get_tag_by_id(self, tag_id: str) -> Tag | None:
        for tag in self.tags:
            if tag.get_id() == tag_id:
                return tag
        return None