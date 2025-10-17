import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "weather_data",
    version = "0.0.1",
    author = "dousti mohamadreza",
    author_email = "mohamadrezadoustii84@gmail.com",
    description = "a simple client api module to get weather data from open weather",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mohamadreza-dousti/weather_app",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)