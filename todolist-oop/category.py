import uuid

class Category:
    def __init__(self, name: str, color: str):
        self.id = str(uuid.uuid4())
        self.set_name(name)
        self.set_color(color)

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


class CategoryLibrary:
    def __init__(self):
        self.categories: list[Category] = []

    def add_category(self, name: str, color: str) -> Category:
        """Create a new category if it doesn't exist, otherwise return existing one (based on name)."""
        for category in self.categories:
            if category.get_name() == name:
                 return category
        
        new_category = Category(name, color)
        self.categories.append(new_category)
        return new_category

    def remove_category(self, category_id: str):
        self.categories = [c for c in self.categories if c.get_id() != category_id]

    def update_category(self, category_id: str, name: str = None, color: str = None):
        for category in self.categories:
            if category.get_id() == category_id:
                if name:
                    category.set_name(name)
                if color:
                    category.set_color(color)
                return
        raise ValueError(f"Category with id {category_id} not found.")

    def get_category_by_id(self, category_id: str) -> Category | None:
        for category in self.categories:
            if category.get_id() == category_id:
                return category
        return None