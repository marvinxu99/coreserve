# run.py
from app import create_app

app = create_app("development")

if __name__ == "__main__":
    # app.logger.info("Starting coreserve application...")
    # app.logger.error("This is a test error log to check file logging.")
    app.run(host="0.0.0.0", port=8080, debug=True)