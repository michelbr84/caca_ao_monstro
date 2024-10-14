from setuptools import setup, find_packages

setup(
    name="caca_ao_monstro",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],  # Deixe vazio se não houver dependências externas
    entry_points={
        "console_scripts": [
            "caca_ao_monstro = game:main",  # Permite rodar o jogo pelo terminal
        ],
    },
    description="Um jogo de Caça ao Monstro em uma grade",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MichelBr",
    author_email="seu_email@example.com",
    url="https://github.com/michelbr84/caca_ao_monstro",  # Substitua pelo seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
