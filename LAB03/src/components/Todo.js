import TodoList from "./TodoList";

const Todo = (storage) => {
  const addTodoBtn = document.getElementById("todo-input-btn");
  const addTodoInput = document.getElementById("todo-input-form");

  const dashboard = document.getElementById("dashboard-group");
  const done = document.getElementById("done-group");

  const clearTodos = document.getElementById("clear-todos");

  // -------------------------------------------------------------------- //

  dashboard.addEventListener("click", () => {
    TodoList(storage, "all");
  });

  done.addEventListener("click", () => {
    TodoList(storage, "done");
  });

  clearTodos.addEventListener("click", () => {
    storage.clearTodoList();
    TodoList(storage, "all");
  });

  // -------------------------------------------------------------------- //

  addTodoBtn.addEventListener("click", (event) => {
    // 👇 Prevent the web page to refresh.
    event.preventDefault();

    const completed = false;
    const index = storage.list.length + 1;
    const description = addTodoInput.value.trim();
    const id = `id${
      Date.now().toString(36) + Math.random().toString(36).substr(2)
    }`;

    const newTodo = {
      id,
      description,
      completed,
      index,
    };

    if (description) {
      storage.addTodo(newTodo);
      TodoList(storage);
    }

    addTodoInput.value = "";
  });

  // -------------------------------------------------------------------- //
};

export default Todo;
