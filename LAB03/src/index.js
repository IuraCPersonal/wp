import "./style.css";

import Todo from "./components/Todo";
import Storage from "./components/Storage";
import TodoList from "./components/TodoList";

const storage = new Storage();

Todo(storage);
TodoList(storage, "all");
