# DevShowcase

A modern, feature-rich portfolio platform for developers to showcase their projects with customizable themes.

## Features

- **User Authentication**: Secure registration and login system
- **Project Management**: Add, edit, and delete projects with rich details
- **Customizable Profiles**: Add bio, skills, and social media links
- **Multiple Portfolio Themes**: Choose from 4 different showcase themes
- **Project Details**: Include tech stack, GitHub links, live demos, and project images
- **Responsive Design**: Works perfectly on all devices
- **Media Upload**: Support for profile pictures and project images
- **Skills Showcase**: Display your technical skills
- **Social Integration**: Link to GitHub, LinkedIn, Twitter, and personal website

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4
- **Forms**: Django Crispy Forms with Bootstrap 4
- **File Storage**: Local storage with WhiteNoise for static files
- **Deployment**: Heroku-ready with Gunicorn

## Installation

### Quick Setup (Development)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devshowcase.git
cd devshowcase
```

2. Run the setup script:
```bash
chmod +x setup_dev.sh
./setup_dev.sh
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Run migrations:
```bash
python manage.py makemigrations --settings=devshowcase.settings_dev
python manage.py migrate --settings=devshowcase.settings_dev
```

5. Create a superuser:
```bash
python manage.py createsuperuser --settings=devshowcase.settings_dev
```

6. Run the development server:
```bash
python manage.py runserver --settings=devshowcase.settings_dev
```

7. Visit http://localhost:8000

## Project Structure

```
devshowcase/
├── showcase/           # Main Django app
│   ├── models.py       # User and Project models
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   └── urls.py         # URL patterns
├── devshowcase/        # Project settings
│   ├── settings.py     # Production settings
│   └── settings_dev.py # Development settings
├── templates/          # HTML templates
├── static/             # CSS, JS, and static files
├── media/              # User uploaded files
└── requirements.txt    # Python dependencies
```

## Usage

1. **Register/Login**: Create an account or login with your credentials
2. **Update Profile**: Add your bio, skills, profile picture, and social links
3. **Add Projects**: Click "Add Projects" to showcase your work
4. **Choose Theme**: Select from 4 different showcase themes
5. **Share Portfolio**: Your public portfolio URL is `/showcase/<your-user-id>/`
