import json

text_color = (0, 0, 0)
bg_color = (255, 255, 255)
input_box_color = (200, 200, 200)

input_box_width = 650
width_eps = 50
input_box_height = 50
max_line_length = 35 
visible_lines_count = 9

display_size = (800, 600)

title_text = ['Write or copy-paste your email for check', 'for moving down use arrows']
title_text_coordinates = [(70, 10), (170, 50)]

word2ind = {}
ind2word = {}

def load_vocabular():
    with open('word2ind.json', 'r') as f:
        word2ind = json.load(f)

    with open('ind2word.json', 'r') as f:
        ind2word = json.load(f)

    return word2ind, ind2word
