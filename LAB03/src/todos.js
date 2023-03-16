class Todos {
  constructor() {
    this.list = localStorage.getItem("todos")
      ? JSON.parse(localStorage.getItem("todos"))
      : [];
  }

  addTodo(todo) {
    this.list.push(todo);
    localStorage.setItem("todos", JSON.stringify(this.list));
  }
}

export default Todos;
