from setuptools import setup, find_packages

setup(
    name='mathematics quiz',
    version='0.1.0',
    packages=find_packages(),
    # install_requires=[
    #     # List your package dependencies here if any
    # ],
    entry_points={
        'console_scripts': [
            'math_quiz = mathquiz.__main__:main',
        ],
    },
    # Additional metadata
    author='Rabin BK',
    description='Mathematical quiz game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-package-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
