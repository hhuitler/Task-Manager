from data_manager import load_data, save_data

def show_menu():
    print("\n--- Менеджер задач ---")
    print("1. Посмотреть задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить как выполненную")
    print("5. Очистить список")
    print("6. Выход")

def main():
    tasks = load_data()
    
    while True:
        show_menu()
        try:
            choice = input("Выберите действие (1-6): ")
            
            if choice == "1":
                if not tasks: print("Список пуст.")
                for i, t in enumerate(tasks, 1):
                    status = "[x]" if t['done'] else "[ ]"
                    print(f"{i}. {status} {t['title']}")
            
            elif choice == "2":
                title = input("Введите название задачи: ")
                tasks.append({"title": title, "done": False})
                save_data(tasks)
                
            elif choice == "3":
                idx = int(input("Номер для удаления: ")) - 1
                tasks.pop(idx)
                save_data(tasks)
                
            elif choice == "4":
                idx = int(input("Номер задачи: ")) - 1
                tasks[idx]['done'] = True
                save_data(tasks)
            
            elif choice == "5":
                tasks = []
                save_data(tasks)
                
            elif choice == "6":
                break
            else:
                print("Некорректный ввод!")
                
        except (ValueError, IndexError):
            print("Ошибка: введите корректный номер или данные.") # [cite: 36, 38]

if __name__ == "__main__":
    main()