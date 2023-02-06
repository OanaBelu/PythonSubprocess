"""
Menu
  1. Create file (opens an existing file).
  2. Write to file.
  3. Display file's contents.
  4. Exit.
Select the operation: 

"""

import subprocess
#
# x = subprocess.call(r'./app.exe', stdin=2, stdout=subprocess.PIPE, stderr=None)
# print(x.stdout)

def run_app():
    # Deschid app.exe
    process = subprocess.Popen([r'./app.exe'],
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               bufsize=5,
                               universal_newlines=True)

    # Lista pentru a stoca rezultatele - outputul
    results = []

    # Itereaza prin fiecare input
    for i in range(1, 5):
        # Trimite inputul

        # subprocess.Popen.wait(timeout=2)
        process.stdin.write(f"{i}\n")
        process.stdin.flush()
        # process.returncode

        # Citesc output-ul
        output = process.stdout.readline()

        # Adauga output-ul in lista
        results.append(output)
        print(output)
        print("sdf")

        # Verifica daca procesul s-a terminat
        if process.poll() is not None:
            break

    # Inchide procesul
    process.stdin.close()
    process.stdout.close()

    # Returneaza lista cu rezultate
    return results

# Ruleaza functia
results = run_app()

# Scrie rezultatele in fisier
with open("results.txt", "w") as f:
    for result in results:
        f.write(result)
        
