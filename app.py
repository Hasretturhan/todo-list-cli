import os
import pyfiglet
import readchar
import re

class Task:
    def __init__(self, text, deadline=None):
        self.text = text
        self.deadline = deadline
        self.validate = False
    
    def validate_task(self):
        self.validate = True
        return self
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        if task.deadline:
            print(f"Görev eklendi: {task.text} | Bitiş tarihi: {task.deadline} | Onay: {task.validate}")
        else:
            print(f"Görev eklendi: {task.text} | Onay: {task.validate}")

    def view_tasks(self):
        if not self.tasks:
            print("Listede görev yok.")
            return
        for i, task in enumerate(self.tasks, 1):
            if task.deadline:
                print(f"{i}. {task.text} | Bitiş tarihi: {task.deadline} | Onay: {task.validate}")
            else:
                print(f"{i}. {task.text} | Onay: {task.validate}")

    def remove_task(self, index):
        if 0 <= index - 1 < len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Silinen görev: {removed_task.text}")
        else:
            print("Geçersiz görev numarası.")

    def validate_task_by_index(self, index):
        if 0 <= index - 1 < len(self.tasks):
            validate_task = self.tasks[index - 1].validate_task()
            print(f"Görev onaylandı: '{validate_task.text}'")
        else:
            print("Geçersiz görev numarası.")

def welcome_page():
    clear_screen()
    # 'starwars' fontu bulunamazsa hata almamak için yedekle
    try:
        title = pyfiglet.figlet_format("TO DO LIST APP", font="starwars")
    except Exception:
        title = pyfiglet.figlet_format("TO DO LIST APP")
    print(title)
    print("-- Hasret Turhan --\n\nDevam etmek için bir tuşa basın")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = ToDoList()
    welcome_page()
    readchar.readkey()  # Açılış ekranından geçmek için
    clear_screen()

    options = ["Görev ekle", "Görev sil", "Görevi onayla", "Çıkış"]
    current_option = 0

    while True:
        clear_screen()
        print("-- Mevcut Görevler --\n")
        todo_list.view_tasks()

        print("\nYapılacaklar Uygulaması")
        for index, option in enumerate(options):
            prefix = ">> " if index == current_option else "   "
            print(f"{prefix}{option}")

        key = readchar.readkey()
        if key == readchar.key.UP and current_option > 0:
            current_option -= 1
        elif key == readchar.key.DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == readchar.key.ENTER:
            if current_option == 0:
                clear_screen()
                task_text = input("Görev girin: ")
                while not task_text:
                    task_text = input("Göreve bir ad vermelisiniz.\nGörev girin: ")
                
                def is_valid_date(date):
                    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((19|20)\d\d)$"
                    return re.match(pattern, date) is not None

                deadline = input("Bitiş tarihi (gg/aa/yyyy) (OPSİYONEL): ")
                while deadline and not is_valid_date(deadline):
                    print("Geçersiz tarih formatı. Lütfen gg/aa/yyyy formatında geçerli bir tarih girin.")
                    deadline = input("Bitiş tarihi (opsiyonel): ")

                todo_list.add_task(Task(task_text, deadline))
                readchar.readkey()
            elif current_option == 1:
                clear_screen()
                todo_list.view_tasks()
                try:
                    index = int(input("\nSilinecek görev numarasını girin: "))
                    todo_list.remove_task(index)
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")
                readchar.readkey()
            elif current_option == 2:
                clear_screen()
                todo_list.view_tasks()
                try:
                    index = int(input("\nTamamladığınız görevin numarasını girin: "))
                    todo_list.validate_task_by_index(index)
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")
                readchar.readkey()
            elif current_option == 3:
                print("Uygulamadan çıkılıyor.")
                break

if __name__ == "__main__":
    main()
