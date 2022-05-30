import setuptools

setuptools.setup(
    name="model_api",
    version="0.0.1",
    author="Bas de Kan",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
