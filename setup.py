from setuptools import setup, find_packages

setup(
    name="credit-risk-ml",
    version="0.1.0",
    description="End-to-end credit risk modeling pipeline with MLOps",
    author="Harsh Kumar",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
)
