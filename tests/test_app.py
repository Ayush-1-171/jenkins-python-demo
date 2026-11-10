from app import greet

def test_greet():
    assert greet("Ayush") == "Hello, Ayush! Welcome to DevOps CI/CD."

def test_greet_another_user():
    assert greet("Jenkins") == "Hello, Jenkins! Welcome to DevOps CI/CD."