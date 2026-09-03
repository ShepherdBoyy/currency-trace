<div align="center">

# Currency Trace — Frontend

React client application

</div>

## Tech Stack

| Technology       | Purpose                                    | Version |
| ---------------- | ------------------------------------------ | ------- |
| React            | UI Library                                 | 18.2.0  |
| React Router DOM | Client-side routing                        | 6.23.0  |
| Axios            | HTTP requests to the backend detection API | 1.6.8   |
| Vite             | Build tool & dev server                    | 5.0.8   |

## Installation

1. Navigate into the frontend directory

```bash
    cd frontend
```

2. Install dependencies

```bash
    npm install
```

3. Start the development server

```bash
    npm run dev
```

4. Open your browser and go to the local URL shown in the terminal (usually `http://localhost:5173`)

> **Note:** The Recognize page is configured to call the live backend at
> `https://currency-trace-backend.onrender.com`. To run it against a local backend instead,
> update the URL in `src/pages/recognize/Recognize.jsx` to point to your local backend,
> such as `http://localhost:5000`.

## Project Structure

```
frontend/
├── src/
│   ├── pages/
│   │   ├── home/
│   │   ├── recognize/
│   │   ├── convert/
│   │   └── catalog/
│   ├── database/
│   │   ├── philippines/
│   │   ├── us-dollar/
│   │   ├── euro/
│   │   ├── british-pound/
│   │   └── kuwait-dinar/
│   ├── assets/
│   ├── App.jsx
│   ├── Navbar.jsx
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

## License

This project is licensed under the [MIT License](../LICENSE).