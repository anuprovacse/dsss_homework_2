# setup.py
from setuptools import setup, find_packages

setup(
    name="math_quiz_game",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz_game=math_quiz_game.math_quiz_game:main_function',
        ],
    },
)
