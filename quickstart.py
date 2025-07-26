#!/usr/bin/env python3
"""
Quick start script for DevShowcase development
"""
import os
import sys
import subprocess

def main():
    print("🚀 Starting DevShowcase Quick Setup...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists('venv'):
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])
    
    # Determine pip path based on OS
    if os.name == 'nt':  # Windows
        pip_path = os.path.join('venv', 'Scripts', 'pip')
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:  # Unix/Linux/Mac
        pip_path = os.path.join('venv', 'bin', 'pip')
        python_path = os.path.join('venv', 'bin', 'python')
    
    # Install requirements
    print("📚 Installing requirements...")
    subprocess.run([pip_path, 'install', '-r', 'requirements.txt'])
    
    # Create necessary directories
    dirs_to_create = [
        'media/devshowcase/profile_pics',
        'media/devshowcase/project_images',
        'staticfiles'
    ]
    
    for dir_path in dirs_to_create:
        os.makedirs(dir_path, exist_ok=True)
    
    # Check if config.ini exists
    config_path = 'devshowcase/config.ini'
    if not os.path.exists(config_path):
        print("⚙️  Creating config.ini from example...")
        if os.path.exists('devshowcase/config.ini.example'):
            import shutil
            shutil.copy('devshowcase/config.ini.example', config_path)
            print("📝 Please update devshowcase/config.ini with your settings")
    
    # Run migrations
    print("🗄️  Running migrations...")
    subprocess.run([python_path, 'manage.py', 'makemigrations', '--settings=devshowcase.settings_dev'])
    subprocess.run([python_path, 'manage.py', 'migrate', '--settings=devshowcase.settings_dev'])
    
    print("\n✅ Setup complete!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Create superuser:")
    print("   python manage.py createsuperuser --settings=devshowcase.settings_dev")
    print("3. Run the server:")
    print("   python manage.py runserver --settings=devshowcase.settings_dev")
    print("\n🌐 Visit http://localhost:8000 to see your portfolio platform!")

if __name__ == "__main__":
    main()
