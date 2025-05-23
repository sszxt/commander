from setuptools import setup, find_packages

setup(
    name="commander",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "transformers",
        "torch",
        "peft",
        "accelerate",
        "safetensors",
    ],
    entry_points={
        "console_scripts": [
            "commander=commander.__main__:main",
        ],
    },
    package_data={
        "commander": ["model/checkpoint-750/*"]
    },
    author="Sam",
    description="Terminal AI Assistant using LoRA fine-tuned TinyLlama",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
