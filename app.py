import os
import csv
from faker import Faker

# Crée le goat
fake = Faker()

# Vérifie l'existence du ficheir "output"
output_folder = "."
output_file = os.path.join(output_folder, "data.csv")
os.makedirs(output_folder, exist_ok=True)

# Génération du CSV 
def generate_csv(file_path, num_records):
    with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["id", "name", "age", "email"])

        # GOOOOAAAAT
        for i in range(1, num_records + 1):
            name = fake.name()
            age = fake.random_int(min=18, max=80)
            email = fake.email()
            writer.writerow([i, name, age, email])

    print(f"Fichier généré : {file_path}")


# Doit être fait 100 fois
if __name__ == "__main__":
    generate_csv(output_file, 100)