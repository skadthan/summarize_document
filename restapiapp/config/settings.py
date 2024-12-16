import os

# Celery Configuration
BROKER_URL = 'pyamqp://guest@localhost//'  # RabbitMQ broker

# Redis Configuration
RESULT_BACKEND = 'redis://localhost:6379/0'  # Use Redis for storing task results


# File Uploads
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, '../uploads')

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
