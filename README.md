## i. Penjelasan Singkat Algoritma Greedy

Algoritma greedy yang diterapkan memilih target berlian berdasarkan rasio "nilai/jarak" paling tinggi dari posisi bot saat ini. Strategi ini dianggap efisien karena memprioritaskan pengambilan berlian bernilai tinggi yang terdekat. Jika jumlah berlian yang dibawa bot mencapai 4 atau lebih, maka bot langsung menuju base.

## ii. Requirement Program dan Instalasi

### A. Game Engine
- **Node.js**: https://nodejs.org/en
- **Docker Desktop**: https://www.docker.com/products/docker-desktop/
- **Yarn**:
  ```bash
  npm install --global yarn
  ```

### Langkah Instalasi Game Engine
1. Download dan extract game engine dari release.
2. Masuk ke folder hasil extract dan jalankan:
   ```bash
   yarn
   ```
3. Setup environment:
   - **Windows**:
     ```bash
     ./scripts/copy-env.bat
     ```
   - **Linux/macOS**:
     ```bash
     chmod +x ./scripts/copy-env.sh
     ./scripts/copy-env.sh
     ```
4. Setup database:
   - Jalankan Docker Desktop.
   - Di terminal:
     ```bash
     docker compose up -d database
     ```
   - Jalankan setup DB:
     - **Windows**:
       ```bash
       ./scripts/setup-db-prisma.bat
       ```
     - **Linux/macOS**:
       ```bash
       chmod +x ./scripts/setup-db-prisma.sh
       ./scripts/setup-db-prisma.sh
       ```
5. Build dan jalankan game engine:
   ```bash
   npm run build
   npm run start
   ```

## iii. Cara Menjalankan Bot

### A. Requirement Bot
- **Python**: https://www.python.org/downloads/

### Langkah Instalasi dan Konfigurasi
1. Download dan extract starter pack bot dari release.
2. Masuk ke folder dan jalankan:
   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Bot
- Satu bot:
  ```bash
  python main.py --logic GreedyDiamond --email=your_email@example.com --name=your_name --password=your_password --team etimo
  ```
- Beberapa bot:
  - **Windows**:
    ```bash
    ./run-bots.bat
    ```
  - **Linux/macOS**:
    ```bash
    ./run-bots.sh
    ```

Pastikan logic `GreedyDiamondLogic` sudah didaftarkan di `CONTROLLERS` pada `main.py`.

## iv. Author

- **Aditya Hot Martua Sihite** (123140114)
- **Andre Prasetya Daely** (123140131)
- **Exaudi Amin Hutasoit** (123140161)

## Catatan Tambahan

Bot ini tidak menggunakan AI atau pembelajaran mesin. Seluruh logika berbasis pada aturan deterministik dan probabilistik ringan yang disusun manual.

Cocok digunakan sebagai dasar untuk eksperimen lebih lanjut dalam strategi permainan grid.
