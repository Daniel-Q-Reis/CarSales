# 🚗 CarsHub - Django Car Marketplace

A Django-powered web application for buying and selling cars. This project was developed as a comprehensive study of the Django framework, covering everything from basic setup to deployment on AWS.

**Project Status:** In Development 🚧

---

### Key Features

* **User Authentication:** Secure user registration, login, and logout functionality.
* **Car Listings:** Users can create, view, update, and delete car advertisements.
* **Advanced Search & Filtering:** Powerful search capabilities based on model, brand, year, and price.
* **Database Management:** Utilizes PostgreSQL for robust data storage and Django ORM for queries.
* **Admin Interface:** A custom Django Admin panel for site management.
* **API Endpoints:** RESTful APIs built with Django REST Framework for potential mobile app integration.
* **Cloud Deployment:** Fully configured for deployment on AWS.

---

### Technologies Used

| Technology | Description |
| :--- | :--- |
| **Backend** | Python, Django, Django REST Framework |
| **Database** | PostgreSQL |
| **Deployment** | AWS, Gunicorn, Nginx |
| **Dev Tools** | Git, GitHub, VS Code |

---

### How to Run This Project

*(You will fill this section later)*

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Daniel-Q-Reis/carshub-django-project.git
    cd carshub-django-project
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
