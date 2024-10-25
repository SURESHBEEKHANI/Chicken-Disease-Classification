import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Version and project metadata
__version__ = "0.0.1"  # Updated the version to 0.0.1 for clarity
REPO_NAME = "Chicken-Disease-Classification--Project"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "SURESHBEEKHANI26@gmail.com"

# Package setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Suresh Beekhni",
    author_email="SURESHBEEKHANI26@gmail.com",
    description="A Python package for CNN-based Chicken Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Specify the source directory
    packages=setuptools.find_packages(where="src"),  # Finds all packages in the src folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Ensuring compatibility with Python 3.7 and above
    install_requires=[  # You can add necessary dependencies here
        # "tensorflow",  # Example dependency
        # "numpy",
        # "scikit-learn"
    ],
)
