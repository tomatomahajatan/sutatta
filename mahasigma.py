nim = ["10121001", "10121002", "10121003"]
nama = ["Asep", "Budi", "Cecep"]

nilai = [
    
    [50, 70, 40, 80],   
    [78, 78, 80, 65],   
    [57, 58, 67, 69]    
]

rata_mahasiswa = []
for i in range(len(nim)):
    avg = sum(nilai[i]) / len(nilai[i])
    rata_mahasiswa.append(avg)

max_index = rata_mahasiswa.index(max(rata_mahasiswa))
print(f"Mahasiswa Terpintar         : {nama[max_index]} (Nilai: {rata_mahasiswa[max_index]:.2f})")


mk_rata = []
for j in range(len(nilai[0])):  
    total = 0
    for i in range(len(nilai)): 
        total += nilai[i][j]
    mk_rata.append(total / len(nilai))

min_index = mk_rata.index(min(mk_rata))
print(f"Mata Kuliah Nilai Terkecil  : MK{min_index+1} ({mk_rata[min_index]:.2f})")