from setuptools import setup


setup(
        author="Adrian Toral",
        author_email="adriantoral@sertor.es",
        version="1.0.0",
        description="Generate Fake data by API requests",
        name="fakerapi",
        install_requires=["requests", "fire"],
        package_dir={"": "src"},
        packages=["fakerapi"],
        entry_points = {
            'console_scripts': [
                'fake=fakerapi.main:main'
                ]
            }
        )
