import React from "react";
import { usePageContext } from "../../utils/usePageContext";

const TodosIndexPage = () => {
  let pageContext = usePageContext();
  let todos = pageContext?.todos;

  return (
    <>
      <h1>Todos List</h1>

      <ul>
        {todos?.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </>
  );
};

export default TodosIndexPage;
