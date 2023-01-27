# Start template

Django starter project with react integration.

## Django project

---

- The default project folder is named `backend`. In order to start the development server, an environment variable named PROJECT_NAME must be specified. The variable must have the same name as your project folder.

      PROJECT_NAME = "backend"

  Note: The variable `PROJECT_NAME` variable should be changed accordingly if you rename yout project folder.

- To render a view call the `render_react_page util` inside your view and pass it the `request`, a unique `id` and the `context data`. See the following example.

  ```python
  # views.py
  from django.core import serializers
  from utils import render_react_page
  from .models import Todo

  def home_view(request):
      context = serializers.Serializer(Todo.objects.all())

      return render_react_page(
        request=request,
        element_id="homepage",
        page_context={"todos": context},
      )
  ```

## React frontend

---

- packages installed:

  - material-ui
  -

- The react app is located inside the frontend directory.

- Specify a mounting point for your view inside your `index.tsx`

  ```ts
  // index.tsx
  import React from "react";

  const HomePage = React.lazy(() => import("./pages/HomePage"));

  declarePage("homepage", HomePage);
  ```

  Notice that we're using the same id (`homepage`) as we used in our python view.

- Inside your component, you can access the context data by using the `usePageContext util`.

  ```ts
  // ./pages/HomePage.tsx
  import { usePageContext } from "../../utils";

    type Todo = {
        id: number;
        title: string
    }

    type Context = {
        todos: Todo[]
    }

  const HomePage = () => {
      const const pageContext = usePageContext<Context>();
      const todos = pageContext?.todos

      return (<>Do something ...</>)
  }

  ```

  Note that the key `todos` is a context-key specified inside `views.py`.

## Get started

---

- Build react app in frontend directory and start watching for changes in frontend folder:

  ```sh
  cd frontend
  yarn start
  ```

- Start the livereload server (in another console):

  ```sh
  python manage.py livereload
  ```

- Start the django development server as usual (in another):

  ```sh
  python manage.py runserver
  ```
