from xml.etree import ElementTree
import argparse
import os 
import subprocess
from contextlib import redirect_stdout

def print_with_newline(string):
    print(string)
    print()

def print_node_text_note(node):
    if node.get('text') is None:
        return
    print_with_newline(node.get('text'))
    if '_note' in node.keys():
        print_with_newline(f"  ({node.get('_note')})")

def create_card(node, parent_node_list=[]):
    """
    Print front and back of the card following the format of ankdown
    (https://github.com/benwr/ankdown)
    """
    for parent in parent_node_list:
        print_node_text_note(parent)
    print_node_text_note(node) 
    print_with_newline("%")
    for child in node:
        print_node_text_note(child)
    print_with_newline("---")
        
def dfs(node, parent_node_list = []):
    if node.tag == "outline" and len(node) > 0:
        create_card(node, parent_node_list)
    parent_node_list.append(node)
    for child in node:
        dfs(child, parent_node_list.copy())
        
def create_deck(tree):
    # loop over all nodes
    for node in tree.getroot():
        dfs(node)
        
def get_basename_wo_extension(filepath):
    basename = os.path.basename(filepath)
    return basename.split(".")[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create Deck')
    parser.add_argument('input_path')
    args = parser.parse_args()
    
    with open(args.input_path, 'r', encoding='utf8') as f:
        tree = ElementTree.parse(f)
        
    result_dir = get_basename_wo_extension(args.input_path)
    os.makedirs(result_dir, exist_ok=True)
    
    with open(os.path.join(result_dir, 'deck.md'), 'w') as f:
        with redirect_stdout(f):
            create_deck(tree)
        
    bashCommand = f"ankdown -r {result_dir} -p {result_dir}.apkg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()