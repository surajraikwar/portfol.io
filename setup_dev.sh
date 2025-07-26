#!/bin/bash

# Create a Python virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create config.ini from example if it doesn't exist
if [ ! -f devshowcase/config.ini ]; then
    echo "Creating config.ini..."
    cp devshowcase/config.ini.example devshowcase/config.ini
    echo "Please update devshowcase/config.ini with your settings"
fi

# Create media directories
echo "Creating media directories..."
mkdir -p media/devshowcase/profile_pics
mkdir -p media/devshowcase/project_images

# Create a default profile picture if it doesn't exist
if [ ! -f media/devshowcase/profile_pics/default.jpg ]; then
    echo "Creating default profile picture..."
    # Create a simple default image using Python
    python3 -c "
from PIL import Image, ImageDraw
img = Image.new('RGB', (200, 200), color='#e0e0e0')
draw = ImageDraw.Draw(img)
# Draw a simple user icon
draw.ellipse([50, 50, 150, 150], fill='#9e9e9e')
img.save('media/devshowcase/profile_pics/default.jpg')
print('Default profile picture created')
"
fi

echo "Setup complete! Next steps:"
echo "1. Update devshowcase/config.ini with your database settings"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python manage.py makemigrations"
echo "4. Run: python manage.py migrate"
echo "5. Run: python manage.py createsuperuser"
echo "6. Run: python manage.py runserver"
