from setuptools import setup, find_packages


with open("requirements.txt") as f:
    dependencies = [line for line in f]

setup(
    name='llama_index.bge_m3',
    version='1.0',
    packages=find_packages("llama_index"),
    package_dir={'': 'llama_index'},
    license='MIT License',
    author='',
    author_email='',
    description='Integrating BGE-M3 into Llama-index',
    python_requires='==3.11.5',
    install_requires=dependencies
)