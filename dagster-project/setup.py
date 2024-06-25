from setuptools import find_packages, setup

setup(
    name="ecommerce_dema",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster==1.7.10",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-postgres",
        "pandas",
        "dbt-core",
        "dbt-postgres",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
