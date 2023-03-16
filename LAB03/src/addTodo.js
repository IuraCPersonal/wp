import Todos from "./todos";
import { showTodos } from "./showTodos";

const todosList = new Todos();

const addTodo = (() => {
  const addTodoBtn = document.getElementById("todo-input-btn");
  const addTodoInput = document.getElementById("todo-input-form");

  addTodoBtn.addEventListener("click", (event) => {
    // 👇 Prevent the web page to refresh.
    event.preventDefault();

    const completed = true;
    const index = todosList.list.length + 1;
    const description = addTodoInput.value.trim();
    const id = `id${Math.random().toString(16).slice(2)}`;

    const newTodo = {
      id,
      description,
      completed,
      index,
    };

    if (description) {
      todosList.addTodo(newTodo);
      showTodos();
    }

    addTodoInput.value = "";
  });

  showTodos();
})();

export { addTodo, todosList };
