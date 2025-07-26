# DevShowcase Project Structure

```
devshowcase/
│
├── showcase/                    # Main application (renamed from core_app)
│   ├── migrations/              # Database migrations
│   ├── templatetags/            # Custom template filters
│   │   └── custom_filters.py    # Split, trim filters
│   ├── __init__.py
│   ├── admin.py                 # Enhanced admin interface
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # Enhanced forms with new fields
│   ├── models.py                # Account & Project models
│   ├── urls.py                  # App-specific URLs
│   └── views.py                 # View functions
│
├── devshowcase/                 # Project settings (renamed from portfol_io)
│   ├── __init__.py
│   ├── asgi.py                  # ASGI configuration
│   ├── config.ini.example       # Configuration template
│   ├── settings.py              # Production settings
│   ├── settings_dev.py          # Development settings (SQLite)
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py                  # WSGI configuration
│
├── templates/
│   └── showcase/                # App templates (renamed from portfol_io)
│       ├── base.html            # Base template with navigation
│       ├── index.html           # Home/Dashboard page
│       ├── login.html           # Login page
│       ├── registration.html    # Registration page
│       ├── projects.html        # Projects listing
│       ├── add_projects.html    # Add project form
│       ├── update_profile.html  # Profile update form
│       ├── update_password.html # Password change form
│       ├── template_selector.html # Theme selector
│       ├── showcase_theme1.html # Modern theme
│       ├── showcase_theme2.html # Classic theme
│       ├── showcase_theme3.html # Minimal theme
│       └── showcase_theme4.html # Creative theme
│
├── static/
│   ├── style.css                # Main stylesheet
│   ├── devshowcase-logo.svg     # Project logo
│   ├── hero-image.svg           # Landing page hero image
│   ├── showcase_theme1.css      # Theme 1 styles
│   ├── showcase_theme1.js       # Theme 1 scripts
│   ├── showcase_theme2.css      # Theme 2 styles
│   ├── showcase_theme3.css      # Theme 3 styles
│   └── showcase_theme4.css      # Theme 4 styles
│
├── media/                       # User uploaded files
│   └── devshowcase/
│       ├── profile_pics/        # User profile pictures
│       └── project_images/      # Project images
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── runtime.txt                  # Python version for Heroku
├── Procfile                     # Heroku deployment configuration
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose configuration
├── setup_dev.sh                 # Development setup script
├── quickstart.py                # Quick setup script
├── refactor_project.py          # Project refactoring script
├── README.md                    # Project documentation
├── ENHANCEMENTS.md              # Enhancement documentation
└── PROJECT_STRUCTURE.md         # This file

## Key Naming Changes

### Django Apps
- `core_app` → `showcase`

### Project Package
- `portfol_io` → `devshowcase`

### Templates
- `portfolio_template1.html` → `showcase_theme1.html`
- `portfolio_template2.html` → `showcase_theme2.html`
- `portfolio_template3.html` → `showcase_theme3.html`
- `portfolio_template4.html` → `showcase_theme4.html`

### URLs
- `/portfolio/<id>/` → `/showcase/<id>/`
- `core_app:` namespace → `showcase:` namespace

### Static Files
- `portfolio_template*.css/js` → `showcase_theme*.css/js`

### Media Paths
- `media/portfol_io/` → `media/devshowcase/`

## Import Changes

### Python Imports
```python
# Old
from core_app.models import Account, Project
from portfol_io.settings import *

# New
from showcase.models import Account, Project
from devshowcase.settings import *
```

### Template References
```django
<!-- Old -->
{% extends 'portfol_io/base.html' %}
{% url 'core_app:projects' %}

<!-- New -->
{% extends 'showcase/base.html' %}
{% url 'showcase:projects' %}
```

### Settings Module
```bash
# Old
python manage.py runserver --settings=portfol_io.settings_dev

# New
python manage.py runserver --settings=devshowcase.settings_dev
```
