from app import create_app, db

# 🔥 IMPORTANT: सभी models import करो
from app.models.user import User
from app.models.config import SystemConfiguration
# (अगर और models हैं तो वो भी add कर)

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully")   