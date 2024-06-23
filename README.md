
# Fullstack Test Mekar

[![BE and FE Docker CI/CD](https://github.com/Hadesisback/mekar_project/actions/workflows/be-fe.yml/badge.svg)](https://github.com/Hadesisback/mekar_project/actions/workflows/be-fe.yml)

Berikut hasil pengerjaan test fullstack

## Documentation

- FrontEnd: NextJS
- Backend: Python Flask
- UI Framework: Shadcn, AceternityUI, MUI
- DB: MongoDB

## Edit 
Edit .env files di file backend dan frontend untuk mengubah endpoint, listen host, dan port

## Unit Testing
- Module: Flask_Testing
- File: backend_test.py
    - Request valid
    - Name check
    - Duplicate Entry
    - NIK dan Date of Birth mismatch
    - Date of Birth Format
    - Invalid Date of Birth
    - NIK length mismatch
    - Empty Fields
## Docker
Dockerfile berada di folder backend dan frontend

## Environment Variables
- Backend:
    - MONGODB_URL: mongodb path
    - LISTEN_HOST_BE: bind ip backend
    - LISTEN_PORT_BE: bind port backend
- Frontend:
    - BACKEND_ENDPOINT: backend endpoint path



## API

 - Frontend: /api/formsubmit : Submit form request (POST)
 - Backend: 
    - /submitform : Push data to MongoDB (POST)
    - /getdata : Check DB content (GET)

## Form Validation
 - Module: Zod
    - Email Validation
    - Identity Number validation:
        - Diasumsikan menggunakan format NIK, 16 digit, digit 7-12 sesuai dengan Date of Birth 
            - (untuk demo bisa menggunakan dummy info dengan dengan format digit NIK ke 7-12 yang sesuai dengan tanggal lahir)
        - Numerical (regex)
    - Nama
        - Exclude angka dan symbol
## Demo
- Frontend:
    - http://mekar.febrian.me
- Backend:
    - http://febrian.me:5000/getdata
    - http://febrian.me:5000/submitform
