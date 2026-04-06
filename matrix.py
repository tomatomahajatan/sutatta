def input_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            val = int(input(f"Masukkan elemen [{i+1},{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mul_matrix(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

while True:
    print("\n=== MENU OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Exit")

    pilihan = input("Pilih menu (1-4): ")
    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid, coba lagi.")
        continue

    if pilihan == "4":
        print("Program selesai. Terima kasih!")
        break

    n = int(input("Masukkan jumlah baris matriks: "))
    m = int(input("Masukkan jumlah kolom matriks: "))

    print("\nInput Matriks A:")
    A = input_matrix(n, m)

    print("\nInput Matriks B:")
    B = input_matrix(n, m)

    if pilihan == "1":
        print("\nHasil Penjumlahan:")
        print_matrix(add_matrix(A, B))
    elif pilihan == "2":
        print("\nHasil Pengurangan:")
        print_matrix(sub_matrix(A, B))
    elif pilihan == "3":
        if len(A[0]) != len(B):
            print("Perkalian tidak bisa dilakukan (jumlah kolom A ≠ jumlah baris B).")
        else:
            print("\nHasil Perkalian:")
            print_matrix(mul_matrix(A, B))