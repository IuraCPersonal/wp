const TodoList = (storage, group) => {
  let sortedTodos = [];
  const todosContainer = document.querySelector(".todos");

  if (group === "done") {
    sortedTodos = storage.list
      .sort((a, b) => b.index - a.index)
      .filter((todo) => todo.completed);
  } else {
    sortedTodos = storage.list.sort((a, b) => b.index - a.index);
  }

  // -------------------------------------------------------------------- //

  let todosContent = "";

  sortedTodos.forEach(({ completed, description, id }) => {
    let lableClass = `inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border-2 border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 peer-checked:border-blue-600 hover:text-gray-600 dark:peer-checked:text-gray-300 peer-checked:text-gray-600 hover:bg-gray-50 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700`;
    let todoClass = completed ? " line-through" : "";

    todosContent += `  
                <li>
                    <input type="checkbox" id="${id}" value="" class="hidden peer on-complete-task" required="">
                    <label id="${id}" for="${id}" class="${lableClass}">                           
                        <div class="flex justify-between content-center w-full flex-row">
                            <div class="w-full text-lg inline-block align-middle font-semibold${todoClass} unselectable">${description}</div>
                            <div class="flex">
                                ${
                                  !completed
                                    ? `<span
                                      id="pomodoro-${id}"
                                      class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-200 rounded-full dark:bg-gray-700 dark:text-gray-300"
                                    >
                                      25:00
                                    </span>
                                    <a href="#" id="on-start-task" class="inline-flex items-center mx-1 px-4 py-1 text-sm unselectable font-medium text-center text-green-900 bg-white border border-green-300 rounded-lg hover:bg-green-100 focus:ring-4 focus:outline-none focus:ring-green-200 dark:bg-green-800 dark:text-white dark:border-green-600 dark:hover:bg-green-700 dark:hover:border-green-700 dark:focus:ring-green-700">Start</a>
                                  `
                                    : ""
                                }
                                <a href="#" id="on-delete-task" class="inline-flex items-center mx-1 px-4 py-1 text-sm unselectable font-medium text-center text-red-900 bg-white border border-red-300 rounded-lg hover:bg-red-100 focus:ring-4 focus:outline-none focus:ring-red-200 dark:bg-red-800 dark:text-white dark:border-red-600 dark:hover:bg-red-700 dark:hover:border-red-700 dark:focus:ring-red-700">Delete</a>
                            </div>
                        </div>
                    </label>
                </li>
            `;
  });

  todosContainer.innerHTML = todosContent;

  const completeTodo = document.querySelectorAll(".on-complete-task");
  const deleteTodo = document.querySelectorAll("#on-delete-task");
  const startTodo = document.querySelectorAll("#on-start-task");

  completeTodo.forEach((todo) => {
    todo.addEventListener("change", (event) => {
      const { id } = event.target;

      storage.onToggleTodo(id);
      event.target.parentNode.lastElementChild.classList.toggle("checked");

      TodoList(storage);
    });
  });

  deleteTodo.forEach((todo) => {
    todo.addEventListener("click", (event) => {
      const task = event.target.closest("label[id]");

      task.parentNode.remove();

      storage.onDeleteTodo(task.id);
    });
  });

  startTodo.forEach((todo) => {
    todo.addEventListener("click", (event) => {
      const task_id = event.target.closest("label[id]").id;
      const target_task = document.getElementById(`pomodoro-${task_id}`);

      let timeLeft = parseInt(target_task.textContent) * 60;

      const countdown = setInterval(() => {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;

        target_task.textContent = `${minutes
          .toString()
          .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

        timeLeft--;

        if (timeLeft < 0) {
          clearInterval(countdown);
          target_task.textContent = "25:00";
        }
      }, 1000); // Run the function every second (1000 milliseconds)
    });
  });
};

export default TodoList;
