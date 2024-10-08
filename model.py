import torch.nn as nn 
import torch
import os 
from const import load_vocabular


class LM(nn.Module):
    def __init__(self, hidden_dim, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_dim, padding_idx=word2ind.get('pad', 0))
        self.LSTM = nn.LSTM(hidden_dim, int(hidden_dim / 2), num_layers = 3, batch_first = True, dropout = 0.1)
          
        self.linear = nn.Sequential(
            nn.Linear(int(hidden_dim / 2), hidden_dim),
            nn.Tanh(),
            nn.Dropout(p=0.3)
        )
        self.prediction = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 2)
        )
        
    def forward(self, input_batch):
        embeddings = self.embedding(input_batch)
        
        output, (hidden, cell) = self.LSTM(embeddings)
        output = output.mean(dim = 1)
        
        return self.prediction(self.linear(output))
    

def load_model():
    global word2ind, ind2word
    word2ind, ind2word = load_vocabular()
    
    if os.path.exists('full_model.pth'):
        model = torch.load('full_model.pth')
        print("Model was loaded")
    else:
        print("Model wasn't found")
        model = LM(128, 100000)  # Use random model if loading fails
    
    return model