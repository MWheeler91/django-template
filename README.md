# Django Template

This is a personal Django project starter template optimized for fast bootstrapping.  
It includes a reusable folder structure, virtual environment setup, configuration management, and Makefile automation.

---

### Quick Start

### 1. Clone the Repo

```bash
git clone <your-repo-url> my_project
cd my_project
```

### 2. Initialize the Project

Open the Makefile and change the PROJECT_NAME variable to your desired virtual environment name (default is django-template):

```bash
PROJECT_NAME=django-template
```


### 3. Initialize the Project

This will:
- Create a virtual environment
- Install dependencies
- Create `.gitignore`
- Rename `z_env.example` to `.env`
- Generate and apply a new Django `SECRET_KEY`

```bash
make init
```

### 4. Activate Virtual Environment

Show venv location

```bash
make activate
```

Activate:

```bash
source ~/venv/django-template/bin/activate
```

### 5. Run the Server

```bash
make run
```

---

##  Other Useful Commands

| Command         | Description                           |
|-----------------|---------------------------------------|
| `make install`  | Create venv and install requirements  |
| `make rebuild`  | Delete and recreate virtualenv        |
| `make migrate`  | Run migrations                        |
| `make test`     | Run tests                             |
| `make format`   | Format code with `black`              |
| `make clean`    | Remove Python cache files             |
| `make secret`   | Generate and update `.env` secret     |
| `make collectstatic` | Collect static files             |

---

##  Folder Layout

```
.
├── apps/
│   ├── core/
│   │   ├── account/
│   │   ├── common/
│   │   └── error_logging/
│   ├── infra/
│   └── services/
├── utils/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   └── logs/
├── z_requirements/
│   ├── linux_requirements.txt
│   └── windows_requirements.txt
├── z_env.example
├── manage.py
├── Makefile
└── .gitignore
```

---

##  Notes

- `.env` is ignored by Git and controls both dev and prod configurations.
- Adjust `z_requirements/` depending on platform or dependency set.
- `Makefile` is tailored for Linux. You may adapt it for Windows or Mac if needed.

---

##  Status

This project is actively maintained for personal use.  
If it helps you — feel free to clone, fork, or adapt.
