def todo_list():
    tasks = []

    print("=== To-Do List ===")
    print("Команди: додати, видалити, переглянути, вихід")

    while True:
        command = input("Введіть команду: ").strip().lower()

        if command == "додати":
            task = input("Введіть завдання: ").strip()
            tasks.append(task)
            print(f"Завдання '{task}' додано.")
        elif command == "видалити":
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            try:
                to_delete = int(input("Введіть номер завдання для видалення: "))
                removed_task = tasks.pop(to_delete - 1)
                print(f"Завдання '{removed_task}' видалено.")
            except (ValueError, IndexError):
                print("Некоректний номер.")
        elif command == "переглянути":
            print("Ваші завдання:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif command == "вихід":
            print("Завершення програми.")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    todo_list()
