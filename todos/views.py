from utils import render_react_page

from todos.models import Todo
from todos.serializers import TodoSerializer


def index_view(request):
    if request.method == "GET":
        todos = TodoSerializer(Todo.objects.all(), many=True).data

        return render_react_page(
            request=request,
            element_id="todos-index",
            page_context={"todos": todos},
        )
