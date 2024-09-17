# Custom User Model Django Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Models](#models)
6. [URLs](#urls)
7. [Requirements](#requirements)
8. [Additional Notes](#additional-notes)

## Project Overview

This project demonstrates a Django application with a customized user model that extends the default `AbstractUser`. The custom user model includes additional fields such as phone number, photo, and address. It also establishes many-to-many relationships with the `Group` and `Permission` models, allowing for robust user management.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```sh
    git clone "https://github.com/alishermutalov/USER_DASHBOARD.git"
    cd USER_DASHBOARD
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the application in your web browser at `http://localhost:8000`. The following endpoints are available:

- **Home:** `/`
- **Profile:** `/profile/`
- **Update Profile:** `/profile/update/`
- **Register:** `/register/`
- **Change Password:** `/password/change/`
- **Login:** `/login/`
- **Password Change Done:** `/password/change/done`
- **Logout:** `/logout/`

## Project Structure

The project consists of several key files and directories:

- `models.py`: Defines the custom user model.
- `urls.py`: Defines URL patterns for the application.
- `requirements.txt`: Lists the dependencies required for the project.
- `views.py`: Contains view functions and classes (not shown in this readme but assumed to be present).
- `templates/`: Directory containing HTML templates for rendering views (assumed to be present).

## Models

### CustomUser Model

The `CustomUser` model extends Django's `AbstractUser` and includes additional fields:

- `phone_number`: A CharField to store the user's phone number.
- `photo`: An ImageField to store the user's avatar photo.
- `address`: A CharField to store the user's address.

The model also includes many-to-many relationships with `Group` and `Permission`:

- `groups`: Allows a user to belong to multiple groups.
- `user_permissions`: Allows a user to have multiple permissions.

These relationships use the `related_name` attribute for reverse lookups.

### Example Usage

To get all groups a user belongs to:
```python
user.groups.all()
```

To get all users in a group:
```python
group.customuser_set.all()
```

To get all permissions of a user:
```python
user.user_permissions.all()
```

To get all users with a specific permission:
```python
permission.customuser_set.all()
```

## URLs

The URL patterns defined in `urls.py` route requests to the appropriate views. Some key patterns include:

- `path('', HomeView.as_view(), name='home')`: The home page.
- `path('profile/', UserAccountListView.as_view(), name='profile')`: User profile page.
- `path('profile/update/', CustomUserUpdateView.as_view(), name='update_url')`: Update profile page.
- `path('register/', RegisterView.as_view(), name='register')`: User registration page.
- `path('password/change/', CustomPasswordChangeView.as_view(), name='change_password')`: Change password page.
- `path('login/', CustomLoginView.as_view(), name='login')`: User login page.
- `path('password/change/done', password_change_done, name='password_change_done')`: Password change done page.
- `path('logout/', user_logout, name='logout')`: User logout.

## Requirements

The project dependencies are listed in `requirements.txt`:

- asgiref==3.8.1
- Django==5.0.6
- django-ranged-response==0.2.0
- django-simple-captcha==0.6.0
- pillow==10.3.0
- sqlparse==0.5.0
- tzdata==2024.1

Install them using:
```sh
pip install -r requirements.txt
```

## Additional Notes

- **Customization:** By specifying `related_name`, the reverse relation names are customized for better readability and consistency.
- **Best Practices:** It is a good practice to specify `related_name` to avoid clashes and provide meaningful names for reverse relations.
- **Default Behavior:** If `related_name` is not specified, Django uses the lowercase name of the related model followed by "_set" as the default reverse relation name.
