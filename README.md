# Plate Validator Indonesia

Aplikasi web berbasis Flask untuk melakukan validasi format plat nomor kendaraan Indonesia menggunakan:

- Deterministic Finite Automata (DFA)
- Regular Expression (Regex)

---

## Fitur

- Validasi Plat Nomor Indonesia
- Simulasi DFA
- Riwayat Validasi
- Statistik Validasi
- Export CSV
- Dashboard Bootstrap 5
- Chart.js

---

## Struktur Project

```
plat-validator/
│
├── app.py
├── dfa.py
├── regex_validator.py
├── export.py
├── requirements.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── base.html
    ├── index.html
    ├── simulator.html
    └── about.html
```

---

## Instalasi

Clone repository

```
git clone https://github.com/USERNAME/plat-validator.git
```

Masuk folder

```
cd plat-validator
```

Install dependency

```
pip install -r requirements.txt
```

Jalankan

```
python app.py
```

Browser

```
http://127.0.0.1:5000
```

---

## Format Plat

Contoh valid

```
D 1234 ABC
B 1 A
AB 999 CD
F 7777 ZZ
```

Contoh tidak valid

```
123 ABC
AAAA123
D123456AA
D123ABCD
```

---

## Teknologi

- Python
- Flask
- Bootstrap 5
- Chart.js
- DFA
- Regex

---

## Penulis

Muhammad Faris

NIM : 301240055

Universitas Bale Bandung"# indonesia-plate-validator" 
"# indonesia-plate-validator" 
