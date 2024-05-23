from tree import Tree, make_my_deck
import logging
import sys
MAXDEPTH = 8
import math
import random
import time
import tqdm

def create_game_tree1(current: Tree, depth: int, deck: list):
    """
    create_game_tree creates recursively a tree with each node being a card. (first method)
    inputs:
        current: the current node
        depth: the depth of the current node
        deck: the deck of cards
    output:
        the root of the tree
    """
    maxdepth = MAXDEPTH
    if depth == maxdepth:
        return current
    for card in deck:
        current.children.append(Tree(card, current.total, root=current.root))
    for child in current.children:
        # for each child, remove the card from the deck and create the tree
        try:
            deck.remove(child.val)
        except ValueError:
            logging.error(
                "card %s already removed (this should never happen)", child.val
            )
        create_game_tree1(child, depth + 1, deck)
        deck.append(child.val)
    return current



def create_game_tree2(current: Tree, depth: int, deck: list):
    """
    create_game_tree creates recursively a tree with each node being a card. (second method)
    inputs:
        current: the current node
        depth: the depth of the current node
        deck: the deck of cards
    output:
        the root of the tree
    """
    maxdepth = MAXDEPTH
    if depth == maxdepth:
        return current
    for card in deck:
        if current.total + card <= 21:
            current.children.append(Tree(card, current.total, root=current.root))
        else:
            # if total + card > 21 the game is lost so we don't create a child we just count it
            current.virtualchildrenscount += 1
    for child in current.children:
        # for each child, remove the card from the deck and create the tree
        try:
            deck.remove(child.val)
        except ValueError:
            logging.error(
                "card %s already removed (this should never happen)", child.val
            )
        create_game_tree2(child, depth + 1, deck)
        deck.append(child.val)
    return current

def create_game_tree3(current: Tree, depth: int, deck: list):
    """
    create_game_tree creates recursively a tree with each node being a card. (third method)
    inputs:
        current: the current node
        depth: the depth of the current node
        deck: the deck of cards
    output:
        the root of the tree
    """
    maxdepth = MAXDEPTH
    if depth == maxdepth:
        return current
    for card in deck:
        if current.total + card <= 21:
            # if a child with the same value does not exist, create it
            if current.navigate(card) == -1:
                current.children.append(Tree(card, current.total, root=current.root))
            else:  # else, increment the weight of the existing child
                current.navigate(card).weight += 1
        else:
            # if total + card > 21 the game is lost so we don't create a child we just count it
            current.virtualchildrenscount += 1
    for child in current.children:
        # for each child, remove the card from the deck and create the tree
        try:
            deck.remove(child.val)
        except ValueError:
            logging.error(
                "card %s already removed (this should never happen)", child.val
            )
        create_game_tree3(child, depth + 1, deck)
        deck.append(child.val)
    return current

def count(tree:Tree, counter:int):
    """Counts the nodes of a tree"""
    counter += 1
    for child in tree.children:
        counter = count(child, counter)
    return counter

def node_numer_m1(i,n):
    """ Returns the number of nodes in a tree of depth n"""
    if i==n:
        return 0
    else:
        return (52-i)*(1+node_numer_m1(i+1,n))

def node_number_m2(depth,it):
    if depth <= 2:
        return 0
    c = 0
    deck = make_my_deck()
    for _ in tqdm.tqdm(range(it)):
        a = random.sample(deck, depth)
        if sum(a) > 21:
            c += 1
    return c/it

def main():
    print(f"DEPTH={MAXDEPTH}\nMethod 1")
    m1m = node_numer_m1(0, MAXDEPTH)
    print(f"Total number of nodes (no optimisation)(math method) : {m1m}")
    print("Method 2")
    deck = make_my_deck()
    root = Tree(0, 0)
    tree = create_game_tree2(root, 0, deck)
    m2c = (count(tree, 0)-1)
    m2m = node_number_m2(MAXDEPTH, 10000000)
    print(f"Total number of node (using VC)(IT method) {m2c}")
    print(f"Proportion of nodes that are virtual children: {m1m-m2c}/{m1m}= {(m1m-m2c)/m1m}")
    print(f"Estimated proportion of nodes that are virtual children: {m2m}")
    print(f"Number of virtual children: {m1m-m2c}")
    print(f"Estimated number of virtual children: {(m2m*m1m)}")
    print(f"Total number of nodes (VC)(math method){m1m-(m2m*m1m)}")
    print(f"Optimisation ratio:w")
    print("Method 3")
    deck = make_my_deck()
    root = Tree(0, 0)
    tree = create_game_tree3(root, 0, deck)
    m3c = count(tree, 0)-1
    print(f"Total number of nodes (VC+Weigth)(IT method){m3c}")
    print("done")

main()