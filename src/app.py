from datetime import datetime


def get_status():
    return {
        "application": "Azure DevOps CI/CD Demo",
        "status": "healthy",
        "environment": "development",
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    print(get_status())
