# Spam-filter application 
![Pygame](https://img.shields.io/badge/Pygame-2.6.0-red)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.0-green)
![Torchvision](https://img.shields.io/badge/Torchvision-0.16.1-orange)
![NLTK](https://img.shields.io/badge/NLTK-3.7-blue)
![Issues](https://img.shields.io/github/issues/AndreRab/Spam-filter)

## The Spam-filter application is designed to assist you in detecting spam in your emails.

### Description
In today’s world, almost everyone uses email, and it's frustrating to waste time on irrelevant or unwanted messages. That's why most email services have a spam section. I became curious about how these systems determine what qualifies as spam and what doesn’t, leading me to conduct a study where I compared three different types of neural networks for this classification task.

My project is divided into two main components:
1. A **Pygame** application, which you can use to predict whether an email is spam or ham.
2. A **Jupyter Notebook**, where I compare the performance of different neural network architectures and describe the entire process of model training.

Feel free to explore the project and see if your emails are classified as spam or ham!

## Table of Contents

| Section                      | Description                                                         |
|-------------------------------|---------------------------------------------------------------------|
| [Running the application](#running-application) | Instructions for running the Pygame application               |
| [Training Datasets](#training-datasets)   | Information about the datasets used for training models      |
| [Jupyter Notebook](#notebook-description)   | A detailed breakdown of the notebook, where it's located, and which models have been used |

## Running the application
1. **Clone the Repository**:
   Open a terminal and clone the repository:
   ```bash
   git clone https://github.com/AndreRab/Spam-filter.git
   ```
2. **Navigate to the Project Directory**:
   Change your directory to the project folder:
    ```bash
    cd Spam-filter
    ```

3. **Install the necessary libraries**:
   Install the necessary libraries for properly application working:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**
   ```bash
   python scripts/main.py
   ```

## Training Datasets
For training datasets, I used the following sources: [Spam Email Classification Dataset](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset). In this dataset, there are only two columns: text and labels. Therefore, I didn't need to perform any preprocessing before training my models.


## Jupyter Notebook
The notebook is located in the **research** folder. There, you can see that I first created a vocabulary, where each word is assigned a unique ID. If a word is not in the vocabulary, it is assigned an unknown token.

Next, I defined three different architectures using the following blocks: vanilla RNN, GRU, and LSTM. All of them achieved good results, but the best-performing model was the one using GRU blocks. You can also find a plot showing its learning process.

![image](https://github.com/user-attachments/assets/d9296d29-f5e9-4a3e-8e26-512560f719cf)

