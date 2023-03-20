class Storage {
  constructor() {
    this.list = localStorage.getItem("todos")
      ? JSON.parse(localStorage.getItem("todos"))
      : [];
  }

  addTodo = (todo) => {
    this.list.push(todo);
    localStorage.setItem("todos", JSON.stringify(this.list));
  };

  onToggleTodo = (id) => {
    const targetTodo = this.list.findIndex((el) => el.id == id);
    this.list[targetTodo].completed = !this.list[targetTodo].completed;
    localStorage.setItem("todos", JSON.stringify(this.list));
  };

  onDeleteTodo = (id) => {
    this.list = this.list.filter((todo) => todo.id !== id);

    this.list.forEach((todo, index) => {
      todo.index = index + 1;
    });

    localStorage.setItem("todos", JSON.stringify(this.list));
  };

  clearTodoList = () => {
    this.list = [];
    localStorage.setItem("todos", JSON.stringify(this.list));
  };
}

export default Storage;
