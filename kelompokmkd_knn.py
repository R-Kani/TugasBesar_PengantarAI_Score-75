# -*- coding: utf-8 -*-
"""KelompokMKD_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a1Gb898YVHj3Ajt0YCO2Ey5IQRu7AtTS
"""

# import modul yang dibutuhkan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # modul untuk membuat diagram batang

"""# **Read Data**


"""

# masukkan URL ke variable 'file_url'
# Data tersebut merupakan data 'arrhythmia.data'
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/arrhythmia.data'

# baca dengan pd.read_csv() dengan argumen header=None(menandakan tidak ada baris header) dan na_values='?'(semua nilai '?' diubah menjadi NaN)
dataf = pd.read_csv(file_url, header=None, na_values='?')

# Rename semua column sesuai 'arrhythmia.names'
dataf.set_axis(["Age", "Sex", "Height", "Weight", "QRS Duration", "P-R Interval", "Q-T Interval", "T Interval", "P Interval", "QRS Vector_A", "T Vector_A", "P Vector_A", "QRST Vector_A",
               "J Vector_A", "Heart Rate","Q Wave_W_DI", "R Wave_W_DI", "S Wave_W_DI", "R` Wave_W_DI", "S` Wave_W_DI", "Intrinsic_Deflect_DI", "R_R Wave DI", "D_D_R Wave DI", "R_P Wave DI",
               "D_D_P Wave DI", "R_T Wave DI", "D_D_T Wave DI","Q Wave_W_DII", "R Wave_W_DII", "S Wave_W_DII", "R` Wave_W_DII", "S` Wave_W_DII", "Intrinsic_Deflect_DII", "R_R Wave DII", "D_D_R Wave DII",
               "R_P Wave DII", "D_D_P Wave DII", "R_T Wave DII", "D_D_T Wave DII","Q Wave_W_DIII", "R Wave_W_DIII", "S Wave_W_DIII", "R` Wave_W_DIII", "S` Wave_W_DIII", "Intrinsic_Deflect_DIII",
               "R_R Wave DIII", "D_D_R Wave DIII", "R_P Wave DIII", "D_D_P Wave DIII", "R_T Wave DIII", "D_D_T Wave DIII","Q Wave_W_AVR", "R Wave_W_AVR", "S Wave_W_AVR", "R` Wave_W_AVR", "S` Wave_W_AVR",
               "Intrinsic_Deflect_AVR", "R_R Wave AVR", "D_D_R Wave AVR", "R_P Wave AVR", "D_D_P Wave AVR", "R_T Wave AVR", "D_D_T Wave AVR","Q Wave_W_AVL", "R Wave_W_AVL", "S Wave_W_AVL", "R` Wave_W_AVL",
               "S` Wave_W_AVL", "Intrinsic_Deflect_AVL", "R_R Wave AVL", "D_D_R Wave AVL", "R_P Wave AVL", "D_D_P Wave AVL", "R_T Wave AVL", "D_D_T Wave AVL","Q Wave_W_AVF", "R Wave_W_AVF", "S Wave_W_AVF",
               "R` Wave_W_AVF", "S` Wave_W_AVF", "Intrinsic_Deflect_AVF", "R_R Wave AVF", "D_D_R Wave AVF", "R_P Wave AVF", "D_D_P Wave AVF", "R_T Wave AVF", "D_D_T Wave AVF","Q Wave_W_V1", "R Wave_W_V1",
               "S Wave_W_V1", "R` Wave_W_V1", "S` Wave_W_V1", "Intrinsic_Deflect_V1", "R_R Wave V1", "D_D_R Wave V1", "R_P Wave V1", "D_D_P Wave V1", "R_T Wave V1", "D_D_T Wave V1","Q Wave_W_V2", "R Wave_W_V2",
               "S Wave_W_V2", "R` Wave_W_V2", "S` Wave_W_V2", "Intrinsic_Deflect_V2", "R_R Wave V2", "D_D_R Wave V2", "R_P Wave V2", "D_D_P Wave V2", "R_T Wave V2", "D_D_T Wave V2","Q Wave_W_V3", "R Wave_W_V3",
               "S Wave_W_V3", "R` Wave_W_V3", "S` Wave_W_V3", "Intrinsic_Deflect_V3", "R_R Wave V3", "D_D_R Wave V3", "R_P Wave V3", "D_D_P Wave V3", "R_T Wave V3", "D_D_T Wave V3","Q Wave_W_V4", "R Wave_W_V4",
               "S Wave_W_V4", "R` Wave_W_V4", "S` Wave_W_V4", "Intrinsic_Deflect_V4", "R_R Wave V4", "D_D_R Wave V4", "R_P Wave V4", "D_D_P Wave V4", "R_T Wave V4", "D_D_T Wave V4","Q Wave_W_V5", "R Wave_W_V5",
               "S Wave_W_V5", "R` Wave_W_V5", "S` Wave_W_V5", "Intrinsic_Deflect_V5", "R_R Wave V5", "D_D_R Wave V5", "R_P Wave V5", "D_D_P Wave V5", "R_T Wave V5", "D_D_T Wave V5","Q Wave_W_V6", "R Wave_W_V6",
               "S Wave_W_V6", "R` Wave_W_V6", "S` Wave_W_V6", "Intrinsic_Deflect_V6", "R_R Wave V6", "D_D_R Wave V6", "R_P Wave V6", "D_D_P Wave V6", "R_T Wave V6", "D_D_T Wave V6","JJ Wave_Amp_DI", "Q Wave_Amp_DI",
               "R Wave_Amp_DI", "S Wave_Amp_DI", "R` Wave_Amp_DI", "S` Wave_Amp_DI", "P Wave_Amp_DI", "T Wave_Amp_DI", "QRSA DI", "QRSTA DI","JJ Wave_Amp_DII", "Q Wave_Amp_DII", "R Wave_Amp_DII", "S Wave_Amp_DII",
               "R` Wave_Amp_DII", "S` Wave_Amp_DII", "P Wave_Amp_DII", "T Wave_Amp_DII", "QRSA DII", "QRSTA DII","JJ Wave_Amp_DIII", "Q Wave_Amp_DIII", "R Wave_Amp_DIII", "S Wave_Amp_DIII", "R` Wave_Amp_DIII",
               "S` Wave_Amp_DIII", "P Wave_Amp_DIII", "T Wave_Amp_DIII", "QRSA DIII", "QRSTA DIII","JJ Wave_Amp_AVR", "Q Wave_Amp_AVR", "R Wave_Amp_AVR", "S Wave_Amp_AVR", "R` Wave_Amp_AVR", "S` Wave_Amp_AVR",
               "P Wave_Amp_AVR", "T Wave_Amp_AVR", "QRSA AVR", "QRSTA AVR","JJ Wave_Amp_AVL", "Q Wave_Amp_AVL", "R Wave_Amp_AVL", "S Wave_Amp_AVL", "R` Wave_Amp_AVL", "S` Wave_Amp_AVL", "P Wave_Amp_AVL",
               "T Wave_Amp_AVL", "QRSA AVL", "QRSTA AVL","JJ Wave_Amp_AVF", "Q Wave_Amp_AVF", "R Wave_Amp_AVF", "S Wave_Amp_AVF", "R` Wave_Amp_AVF", "S` Wave_Amp_AVF", "P Wave_Amp_AVF", "T Wave_Amp_AVF", "QRSA AVF",
               "QRSTA AVF","JJ Wave_Amp_V1", "Q Wave_Amp_V1", "R Wave_Amp_V1", "S Wave_Amp_V1", "R` Wave_Amp_V1", "S` Wave_Amp_V1", "P Wave_Amp_V1", "T Wave_Amp_V1", "QRSA V1", "QRSTA V1","JJ Wave_Amp_V2",
               "Q Wave_Amp_V2", "R Wave_Amp_V2", "S Wave_Amp_V2", "R` Wave_Amp_V2", "S` Wave_Amp_V2", "P Wave_Amp_V2", "T Wave_Amp_V2", "QRSA V2", "QRSTA V2","JJ Wave_Amp_V3", "Q Wave_Amp_V3", "R Wave_Amp_V3",
               "S Wave_Amp_V3", "R` Wave_Amp_V3", "S` Wave_Amp_V3", "P Wave_Amp_V3", "T Wave_Amp_V3", "QRSA V3", "QRSTA V3","JJ Wave_Amp_V4", "Q Wave_Amp_V4", "R Wave_Amp_V4", "S Wave_Amp_V4", "R` Wave_Amp_V4",
               "S` Wave_Amp_V4", "P Wave_Amp_V4", "T Wave_Amp_V4", "QRSA V4", "QRSTA V4","JJ Wave_Amp_V5", "Q Wave_Amp_V5", "R Wave_Amp_V5", "S Wave_Amp_V5", "R` Wave_Amp_V5", "S` Wave_Amp_V5", "P Wave_Amp_V5",
               "T Wave_Amp_V5", "QRSA V5", "QRSTA V5","JJ Wave_Amp_V6", "Q Wave_Amp_V6", "R Wave_Amp_V6", "S Wave_Amp_V6", "R` Wave_Amp_V6", "S` Wave_Amp_V6", "P Wave_Amp_V6", "T Wave_Amp_V6", "QRSA V6", "QRSTA V6",
               "Class"], axis = "columns", inplace =True)

"""# **Output Isi Data**"""

# output isi dataframe dataf
dataf

# output 5 baris pertama dataf
dataf.head()

# output 5 baris terakhir dataf
dataf.tail()

# output informasi dataf termasuk jumlah baris dan kolom, tipe data kolom
dataf.info()

# output informasi statisk dataf termasuk count, mean, std, min, quartil, dan max
dataf.describe()

"""# **Data Preprocessing**

## **Handle missing values**
"""

# function untuk check missing values
def check_missing_values(df):
    missing_values = {}
    total_rows = len(df)

    for column in df.columns:
        missing_count = df[column].isna().sum()
        if missing_count > 0:
            missing_values[column] = missing_count

    # Jika tidak ada missing values pada datagram frame akan keluar dari function
    if len(missing_values) == 0:
        print(f'Tidak ada missing values pada Data Frame ini')
        return

    for column, count in missing_values.items():
        percentage = (count / total_rows) * 100
        print(f"Column '{column}': {count} missing value(s) ({percentage:.2f}%)")

    # buat bar chart
    if len(missing_values) > 0:
        # buat list columns, count missing value(s), dan persen
        columns = list(missing_values.keys())
        counts = list(missing_values.values())
        percentages = [(count / total_rows) * 100 for count in counts]

        # Plot missing value(s) menggunakan bar chart
        fig, ax = plt.subplots()
        ax.bar(columns, counts)

        # tambah label persen
        for i, count in enumerate(counts):
            ax.text(i, count, f"{percentages[i]:.2f}%", ha='center', va='bottom')

        # Set labels dan titles
        ax.set_xlabel('Columns')
        ax.set_ylabel('Missing Value Count')
        ax.set_title('Missing Values')
        ax.set_xticklabels(columns, rotation=90)

        plt.tight_layout()
        plt.show()

# panggil procedure
check_missing_values(dataf)

"""Dataframe dengan missing value yang lebih dari 80% akan di drop dimana hanya column 'J Vector_A' dengan 376 missing values akan di drop. Untuk column lain dengan data frame yang ada missing value(s) akan diisi dengan nilai mean berdasarkan columnnya."""

# Drop column 'J Vector_A'
dataf = dataf.drop('J Vector_A', axis=1)
dataf

# isi sisa missing values yang ada di dataframe dengan mean values tiap column
mean_values = dataf.mean()
dataf = dataf.fillna(mean_values)
dataf

# Cek ulang missing values
check_missing_values(dataf)

"""## **Handle data bernilai nol**"""

# function hapus column yang data bernilai nol lebih dari threshold
def drop_columns_with_zeros(data, threshold):
    total_rows = len(data)
    zero_values = data[data == 0].count()
    zero_percentages = zero_values / total_rows * 100

    columns_to_drop = zero_percentages[zero_percentages > threshold].index
    data = data.drop(columns_to_drop, axis=1)

    dropped_columns = pd.DataFrame({'Column': columns_to_drop, 'Zero Percentage': zero_percentages[columns_to_drop]})

    print("Dropped Columns:\n")
    print(f"Columns\t\tZero Percantage")
    for _, row in dropped_columns.iterrows():
        print(f"{row['Column']}\t{row['Zero Percentage']:.2f}%")

    return data

# function hapus rows yang data bernilai nol lebih dari threshold
def drop_rows_with_zeros(data, threshold):
    total_columns = len(data.columns)
    zero_counts = (data == 0).sum(axis=1)
    zero_percentages = zero_counts / total_columns * 100

    rows_to_drop = zero_percentages[zero_percentages > threshold].index
    dropped_rows = data.loc[rows_to_drop]
    data = data.drop(rows_to_drop)

    print("Dropped Rows:\n")
    print(f"Index\t\tZero Percentage")
    for idx, row in dropped_rows.iterrows():
        print(f"{idx}\t\t{zero_percentages.loc[idx]:.2f}%")

    return data

# set dulu supaya column sex tidak dihapus (karena dijelaskan di 'arrhythmia.names' bahwa sex 0 = male dan 1 = female, jdi tidak boleh dihapus)
dataf['Sex'] = dataf['Sex'].replace(0, 2)

# panggil function hapus column dengan threshold 50%
dataf = drop_columns_with_zeros(dataf, 50)

"""148 dari 279 column dihapus karena memiliki lebih dari 50% data yang bernilai nol."""

# panggil function hapus baris dengan threshold 30%
dataf = drop_rows_with_zeros(dataf, 30)

"""1 dari 452 column dihapus karena memiliki lebih dari 30% data yang bernilai nol."""

# set balik column sex
dataf['Sex'] = dataf['Sex'].replace(2, 0)

# cek hasil data frame setelah data processing
dataf

"""# **Output data setelah preprocessing**"""

# output informasi dataf termasuk jumlah baris dan kolom, tipe data kolom
dataf.info()

# output informasi statisk dataf termasuk count, mean, std, min, quartil, dan max
dataf.describe()

"""# **Metode KNN**"""

# output ukuran/dimensi dataf
dataf.shape

# Shuffle Data
dataf = dataf.sample(len(dataf)).reset_index(drop=True)
dataf

# Melakukan folding pada data
fold_indices = np.arange(len(dataf))
fold_size = len(dataf) // 10  # Menghitung ukuran setiap lipatan

f1 = fold_indices[:fold_size]
f2 = fold_indices[fold_size:2 * fold_size]
f3 = fold_indices[2 * fold_size:3 * fold_size]
f4 = fold_indices[3 * fold_size:4 * fold_size]
f5 = fold_indices[4 * fold_size:5 * fold_size]
f6 = fold_indices[5 * fold_size:6 * fold_size]
f7 = fold_indices[6 * fold_size:7 * fold_size]
f8 = fold_indices[7 * fold_size:8 * fold_size]
f9 = fold_indices[8 * fold_size:9 * fold_size]
f10 = fold_indices[9 * fold_size:]

fold1 = (dataf.iloc[f1].reset_index(drop=True), dataf.iloc[np.concatenate([f2, f3, f4, f5, f6, f7, f8, f9, f10])].reset_index(drop=True))
fold2 = (dataf.iloc[f2].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f3, f4, f5, f6, f7, f8, f9, f10])].reset_index(drop=True))
fold3 = (dataf.iloc[f3].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f4, f5, f6, f7, f8, f9, f10])].reset_index(drop=True))
fold4 = (dataf.iloc[f4].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f5, f6, f7, f8, f9, f10])].reset_index(drop=True))
fold5 = (dataf.iloc[f5].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f6, f7, f8, f9, f10])].reset_index(drop=True))
fold6 = (dataf.iloc[f6].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f5, f7, f8, f9, f10])].reset_index(drop=True))
fold7 = (dataf.iloc[f7].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f5, f6, f8, f9, f10])].reset_index(drop=True))
fold8 = (dataf.iloc[f8].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f5, f6, f7, f9, f10])].reset_index(drop=True))
fold9 = (dataf.iloc[f9].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f5, f6, f7, f8, f10])].reset_index(drop=True))
fold10 = (dataf.iloc[f10].reset_index(drop=True), dataf.iloc[np.concatenate([f1, f2, f3, f4, f5, f6, f7, f8, f9])].reset_index(drop=True))

test, train = fold5
print(train)

# Normalizations
# Melakukan normalisasi data dengan min-max normalization
def norm(df):
  df = (df - df.min()) / (df.max() - df.min())
  return df

# Assign fitur dan kelas
x = dataf.drop('Class', axis=1) # Menghapus kolom Class(Karena akan kita gunakan sebagai arrhythmia Class)
y = dataf.Class # Class arrhythmia sebagai kelas

X = norm(x) # Melakukan normalisasi untuk data fitur
X

# Menghitung jarak menggunakan euclidean distance
def euclidean(x1, x2):
  return np.sqrt(np.sum((x1 - x2)**2))

# Euclidean distance dari baris pertama dan kedua
euclidean(X.iloc[0], X.iloc[1])

# Training KNN
def knn(X_train, y_train, X_test, k): # k sebagai banyaknya neighbors yang ditentukan

  dist = []
  # Menghitung distance dari data training dan data testing
  for row in range(X_train.shape[0]):
    dist.append(euclidean(X_train.iloc[row], X_test))

  data = X_train.copy()
  data['Dist'] = dist     # Menambahkan data distance pada data
  data['Class'] = y_train # Menambahkan class pada data
  data = data.sort_values(by= 'Dist').reset_index(drop=True) # Mengurutkan data berdasarkan distance

  y_pred = data.iloc[:k].Class.mode() # Mengambil label kelas yang paling sering muncul diantara k-NN
  return y_pred[0]

# Menghitung akurasi dari output berdasarkan label kelas
def acc(y_pred, y_true):
  true = 0
  for i in range(len(y_pred)):
    if y_pred[i] == y_true[i]:
      true += 1
  return true/len(y_pred)

# Evaluasi model dengan menggunakan data fold
def evaluate(fold, k):
  test, train = fold
  X_train, y_train = train.drop('Class', axis=1), train.Class
  X_test, y_test = test.drop('Class', axis=1), test.Class
  X_train = norm(X_train)
  X_test = norm(X_test)
  y_preds = []
  for row in range(X_test.shape[0]):
    y_preds.append(knn(X_train, y_train, X_test.iloc[row],k))

  return (acc(y_preds, y_test))

# Evaluasi hasil setiap fold dan ambil rata-rata akurasi
k = 16
accs = []
folds = [fold1, fold2, fold3, fold4, fold5, fold6, fold7, fold8, fold9, fold10]
for i in range(len(folds)):
  accs.append(evaluate(folds[i], k))

average_accuracy = sum(accs) / 10

print(f'Menggunakan k: {k}, dengan rata-rata akurasi: {average_accuracy}\n')

# visualisasi
plt.figure(figsize=(6, 4))
plt.bar(['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5', 'fold6', 'fold7', 'fold8', 'fold9', 'fold10'], accs)
plt.axhline(average_accuracy, color='r', linestyle='--', label='Rata-rata Akurasi')
plt.xlabel('Fold')
plt.ylabel('Akurasi')
plt.title('Akurasi pada Setiap Fold')
plt.legend()
plt.ylim(0, 1)
plt.show()