from app.db.models import ToDo
from app.repositories.base_repository import Repository


class ToDoRepository(Repository):
    model = ToDo
