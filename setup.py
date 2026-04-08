from setuptools import setup

setup(
    # 1. Identität
    name = "todo-tool",
    version = "1.0.0",
    author = "tayblade",
    description = "This is a CLI-Todo-Tool for your Terminal.",

    # 2. Was gehört dazu? 
    py_modules=["main"],

    # 3. Was muss installiert werden ? 
    install_requires=[
        "rich",
    ],

    # 4. Terminal befehl einstellen. 
    entry_points={
        "console_scripts": [
            "todo=main:main",
        ],
    },
)