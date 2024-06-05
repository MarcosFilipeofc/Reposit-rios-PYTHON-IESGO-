import csv
import flet as ft

# Dados dos alunos
students_data = [
    ["nome", "idade", "nota"],
    ["Alice", "14", "85"],
    ["Bob", "15", "90"],
    ["Charlie", "14", "78"],
    ["David", "15", "88"],
    ["Eve", "14", "92"]
]

# Escrevendo os dados no arquivo students.csv
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("Arquivo students.csv criado com sucesso.")

def read_students_csv(file_path):
    students = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"nome": row["nome"], "idade": int(row["idade"]), "nota": int(row["nota"])})
    return students

students = read_students_csv('students.csv')
print("Dados lidos do arquivo:", students)


def calculate_average(students):
    total_notas = sum(student["nota"] for student in students)
    average = total_notas / len(students)
    return average

average = calculate_average(students)
print("Média das notas:", average)


def write_students_with_average(students, average, file_path):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ["nome", "idade", "nota", "media"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            student["media"] = average
            writer.writerow(student)

write_students_with_average(students, average, 'students_with_average.csv')
print("Arquivo students_with_average.csv criado com sucesso.")


def find_max_min_notes(students):
    max_nota = max(students, key=lambda x: x["nota"])
    min_nota = min(students, key=lambda x: x["nota"])
    return max_nota, min_nota

max_nota, min_nota = find_max_min_notes(students)
print("Maior nota:", max_nota["nota"], "Aluno:", max_nota["nome"])
print("Menor nota:", min_nota["nota"], "Aluno:", min_nota["nome"])


import flet as ft

def main(page: ft.Page):
    students = read_students_csv('students.csv')
    average = calculate_average(students)
    max_nota, min_nota = find_max_min_notes(students)

    def load_data(e):
        students_data = read_students_csv('students.csv')
        students_table.rows.clear()
        for student in students_data:
            students_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(student["nome"])),
                    ft.DataCell(ft.Text(str(student["idade"]))),
                    ft.DataCell(ft.Text(str(student["nota"])))
                ])
            )
        avg_text.value = f"Média das notas: {average:.2f}"
        max_text.value = f"Maior nota: {max_nota['nota']} (Aluno: {max_nota['nome']})"
        min_text.value = f"Menor nota: {min_nota['nota']} (Aluno: {min_nota['nome']})"
        page.update()

    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Idade")),
            ft.DataColumn(ft.Text("Nota")),
        ],
        rows=[]
    )

    avg_text = ft.Text()
    max_text = ft.Text()
    min_text = ft.Text()

    load_data_btn = ft.ElevatedButton(text="Carregar Dados", on_click=load_data)

    page.add(
        load_data_btn,
        students_table,
        avg_text,
        max_text,
        min_text
    )

ft.app(target=main)

