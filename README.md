# 📝 Text boundaries 

## 📖 Overview

**Text boundaries ** is a powerful Python script designed to help you clean, preprocess, and analyze text data! 🚀 This script reads a text file, filters lines containing only alphabetical characters, removes duplicates, sorts them, and generates detailed statistics about the data. It’s perfect for finding the boundaries of datasets for machine learning models, natural language processing, or validating dataset quality. 🧑‍💻

## ✨ Features

- 🔍 **Filter Lines**: Retains only lines with alphabetical characters to ensure data consistency.
- 🗑️ **Remove Duplicates**: Ensures every line is unique for effective data preprocessing.
- 🔠 **Sort Case-Sensitively**: Keeps the data order sensitive to case, which is useful for NLP tasks.
- 📊 **Generate Statistics**: Provides insights such as:
  - Number of lines starting or ending with each letter.
  - Longest word starting with each letter.
  - First and last word starting with each letter.
- 📂 **Outputs**:
  - Cleaned dataset is saved back to `dataset.txt`.
  - Detailed statistics are written to `boundaries.log`.

## 🛠️ Prerequisites

- **Python 3.9+**: Make sure Python is installed and available in your system's PATH.

## 🚀 Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Add Your Data**: Place your text data in a file named `dataset.txt` in the repository directory.

3. **Run the Script**:
   ```bash
   python process_dataset.py
   ```

4. **Check the Outputs**:
   - Updated data in `dataset.txt`.
   - Statistics in `boundaries.log`.

## 🔍 Use Cases and Examples

### 1. **Finding Dataset Boundaries for NLP Preprocessing**

When working with text datasets, such as those used to train or fine-tune language models, it's essential to clean the data and identify the boundaries of valid input. This script helps in preprocessing text data by removing invalid entries and generating useful statistics that help define the boundaries of a valid dataset.

#### **Example: NLP Dataset Validation**

Given an input file `dataset.txt` containing:

```
apple
Banana
!@#$%^
carrot
apple
Apricot
123456
dragonfruit
apple
Banana
```

Running the script will produce:

- **Filtered and Cleaned Data** in `dataset.txt`:

    ```
    Apricot
    Banana
    apple
    carrot
    dragonfruit
    ```

- **Detailed Statistics** in `boundaries.log`:

    ```
    Total rows: 5
    A: Starts 2, Ends 0, Longest Apricot, First Apricot, Last Apricot
    B: Starts 1, Ends 0, Longest Banana, First Banana, Last Banana
    C: Starts 1, Ends 0, Longest carrot, First carrot, Last carrot
    D: Starts 1, Ends 0, Longest dragonfruit, First dragonfruit, Last dragonfruit
    ```

This allows you to quickly understand the composition and range of your dataset, helping ensure that your data meets the requirements for training NLP models.

### 2. **Identifying Boundaries in Large Language Model (LLM) Training Data**

When preparing datasets for LLMs, understanding the range of data (such as the first and last words alphabetically, or the longest word per letter) can be critical in optimizing data loading, tokenization strategies, or even debugging unexpected behavior in trained models.

#### **Example: Preparing Data for LLM Training**

Imagine you have a dataset of vocabulary terms that will be used to fine-tune an LLM. The dataset contains words from various domains, but you need to identify the longest word and the range of starting letters to manage tokenization effectively.

Given the input file `dataset.txt`:

```
neuroscience
abracadabra
xylophone
Quantum
algorithm
Artificial
Zoo
nightmare
alpha
```

After running the script, `boundaries.log` provides insights like:

```
Total rows: 9
A: Starts 3, Ends 1, Longest Artificial, First Artificial, Last algorithm
N: Starts 2, Ends 0, Longest neuroscience, First neuroscience, Last nightmare
Q: Starts 1, Ends 0, Longest Quantum, First Quantum, Last Quantum
X: Starts 1, Ends 0, Longest xylophone, First xylophone, Last xylophone
Z: Starts 1, Ends 0, Longest Zoo, First Zoo, Last Zoo
```

From this output, you can see that:
- The dataset has a balanced mix of starting letters.
- The longest word is **"neuroscience"**.
- Words start with different letters, from **A** to **Z**.

### 3. **Finding Boundaries in Multi-language Datasets**

For multi-language datasets, especially when developing multilingual LLMs, you might want to check that your dataset contains a balanced range of entries across different languages. This script helps in identifying such patterns.

#### **Example: Multi-language Dataset Analysis**

Input file `dataset.txt`:

```
こんにちは
Hello
Bonjour
Hola
안녕하세요
Hallo
你好
Hola
Bonjour
```

Running the script will yield:

- **Filtered Data** (since non-Latin characters will be filtered out):

    ```
    Bonjour
    Hello
    Hola
    ```

- **Statistics**:

    ```
    Total rows: 3
    B: Starts 1, Ends 0, Longest Bonjour, First Bonjour, Last Bonjour
    H: Starts 2, Ends 0, Longest Hello, First Hello, Last Hola
    ```

You can use this information to adjust your dataset for balanced language representation or decide on additional preprocessing steps.

## 🖥️ Automate with GitHub Actions

Automate your dataset processing with GitHub Actions! 🤖 Whenever `dataset.txt` is updated, the script runs and updates the results automatically.

### 🔄 Workflow Configuration

To set up automation, create a `.github/workflows/process_dataset.yml` file with:

```yaml
name: Process Dataset

on:
  workflow_dispatch:
  push:
    paths:
      - 'dataset.txt'  # Trigger the workflow when dataset.txt is updated

jobs:
  update-dataset:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        echo 'No dependencies to install'

    - name: Process dataset
      run: python process_dataset.py

    - name: Commit changes
      run: |
        git config --global user.name 'Fabrizio Salmi'
        git config --global user.email 'fabrizio.salmi@gmail.com'
        git add dataset.txt boundaries.log
        git commit -m "Update dataset and boundaries"
        git push
```

## 🤝 Contributing

Contributions are welcome! 🎉 If you have ideas to improve the script or find a bug, feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
