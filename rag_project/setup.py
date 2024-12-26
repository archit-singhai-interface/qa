from setuptools import setup, find_packages

setup(
    name='rag-policy-bot',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'python-dotenv',
        'langchain-community',
        'langchain-core',
        'openai',
        'faiss-cpu',
        'scikit-learn',
        'numpy',
        'tiktoken'
    ],
    author='Your Name',
    description='RAG Policy Analysis Bot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
