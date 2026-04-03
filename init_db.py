from app import create_app, db
from app.models.config import SystemConfiguration

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()
    print("✅ Tables created")

    # Insert default config (important)
    if not SystemConfiguration.query.first():
        default = SystemConfiguration(
            key="maintenance_mode",
            value="False",
            description="Maintenance Mode Toggle"
        )
        db.session.add(default)
        db.session.commit()
        print("✅ Default config added")

    print("🚀 DB ready")