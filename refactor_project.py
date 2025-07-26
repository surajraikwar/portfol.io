#!/usr/bin/env python3
"""
Script to refactor and rename the project from devshowcase to DevShowcase
"""
import os
import re
import shutil

# Configuration
OLD_NAME = "devshowcase"
OLD_NAME_READABLE = "DevShowcase"
OLD_NAME_LOWER = "devshowcase"
OLD_APP_NAME = "showcase"

NEW_NAME = "devshowcase"
NEW_NAME_READABLE = "DevShowcase"
NEW_NAME_LOWER = "devshowcase"
NEW_APP_NAME = "showcase"

# Files and directories to rename
RENAME_MAPPING = {
    "devshowcase": "devshowcase",
    "showcase": "showcase",
    "templates/devshowcase": "templates/showcase",
    "media/devshowcase": "media/devshowcase",
    "static/showcase_theme1.css": "static/showcase_theme1.css",
    "static/showcase_theme1.js": "static/showcase_theme1.js",
    "static/showcase_theme2.css": "static/showcase_theme2.css",
    "static/showcase_theme3.css": "static/showcase_theme3.css",
    "static/showcase_theme4.css": "static/showcase_theme4.css",
}

# Patterns to replace in files
CONTENT_REPLACEMENTS = [
    # Python imports and references
    (r"devshowcase", "devshowcase"),
    (r"portfol\.io", "devshowcase"),
    (r"Portfol\.io", "DevShowcase"),
    (r"showcase", "showcase"),
    (r"showcase", "showcase"),  # Old references
    
    # Template references
    (r"portfolio_template(\d+)", r"showcase_theme\1"),
    (r"'devshowcase/", r"'showcase/"),
    (r'"devshowcase/', r'"showcase/'),
    
    # URL patterns
    (r"devshowcase:", "showcase:"),
    (r"showcase:", "showcase:"),
    
    # Media paths
    (r"devshowcase/profile_pics", "devshowcase/profile_pics"),
    (r"devshowcase/project_images", "devshowcase/project_images"),
    (r"devshowcase/project_snaps", "devshowcase/project_snaps"),
    (r"devshowcase", "devshowcase"),  # Typo in original
    
    # Static files
    (r"portfolio_template(\d+)\.(css|js)", r"showcase_theme\1.\2"),
    
    # App name in Django settings
    (r"'showcase'", "'showcase'"),
    (r'"showcase"', '"showcase"'),
    
    # Model references
    (r"showcase\.Account", "showcase.Account"),
    (r"showcase\.Project", "showcase.Project"),
]

def rename_files_and_dirs():
    """Rename files and directories according to mapping"""
    print("📁 Renaming files and directories...")
    
    # Sort by length (descending) to rename nested paths first
    sorted_mapping = sorted(RENAME_MAPPING.items(), key=lambda x: len(x[0]), reverse=True)
    
    for old_path, new_path in sorted_mapping:
        if os.path.exists(old_path):
            print(f"  Renaming: {old_path} -> {new_path}")
            # Create parent directory if needed
            new_parent = os.path.dirname(new_path)
            if new_parent and not os.path.exists(new_parent):
                os.makedirs(new_parent, exist_ok=True)
            os.rename(old_path, new_path)

def update_file_contents(file_path, content_replacements):
    """Update file contents with replacements"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old_pattern, new_pattern in content_replacements:
            content = re.sub(old_pattern, new_pattern, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"    ⚠️  Error processing {file_path}: {e}")
        return False

def process_all_files():
    """Process all Python, HTML, CSS, JS, and config files"""
    print("\n📝 Updating file contents...")
    
    file_extensions = ['.py', '.html', '.css', '.js', '.yml', '.yaml', '.txt', '.md', '.ini', '.sh']
    files_updated = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and common non-code directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '__pycache__', 'node_modules']]
        
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                if update_file_contents(file_path, CONTENT_REPLACEMENTS):
                    print(f"  ✓ Updated: {file_path}")
                    files_updated += 1
    
    print(f"\n✅ Updated {files_updated} files")

def update_templates():
    """Update template file names"""
    print("\n📄 Updating template file names...")
    
    template_dir = "templates/showcase"
    if os.path.exists(template_dir):
        for file in os.listdir(template_dir):
            if file.startswith("portfolio_template"):
                old_path = os.path.join(template_dir, file)
                new_file = file.replace("portfolio_template", "showcase_theme")
                new_path = os.path.join(template_dir, new_file)
                print(f"  Renaming: {old_path} -> {new_path}")
                os.rename(old_path, new_path)

def create_new_readme():
    """Create updated README with new name"""
    readme_content = """# DevShowcase

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

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("\n📄 Created new README.md")

def main():
    print("🚀 Starting DevShowcase refactoring...")
    print("=" * 50)
    
    # Step 1: Rename directories and files
    rename_files_and_dirs()
    
    # Step 2: Update file contents
    process_all_files()
    
    # Step 3: Update template file names
    update_templates()
    
    # Step 4: Create new README
    create_new_readme()
    
    print("\n" + "=" * 50)
    print("✨ Refactoring complete!")
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Update any hardcoded references")
    print("3. Run migrations: python manage.py makemigrations")
    print("4. Test the application")
    print("\n💡 Remember to update:")
    print("- Git remote URLs")
    print("- Environment variables")
    print("- Deployment configurations")
    print("- Database names (if needed)")

if __name__ == "__main__":
    main()
