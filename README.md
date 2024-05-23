# tipe
## Presentation
This is the code of my TIPE (travail d'initiative personnelle encadré) on the subject :
>"Optimisation des chances de victoire au blackjack grâce à l’étude de systèmes décisionnels"

> [!WARNING]
> This code might not be neither the most efficient nor the most readable and might contain bugs. It was written in a short amount of time.

## Content

- `blackjack.py` : contains the code of the blackjack game
- `counting.py` : counts the reduction of the number of node in the decision tree to evaluate my optimisation
- `safeness_by_first_card.py` : evaluates the safeness of the player by the first card of the dealer
- `tab.py` : creates a graphical representation of the optimals decisions
- `theorical.png` : the graphical representation of the theorical optimal decisions
- `tree.py` : logic and algorithms to create the decision tree
- `valuetweak.py` : computes the best value of safeness from generated data
- `utlis folder` : visualisation and old data collection scripts
    - `max_depth.py` : was used to find the best depth for the decision tree
    - `run.sh` : was used to collect data for max_depth.py
    - `safeness_by_fc.py` : used to create a visual representation of the safeness by the first card of the dealer
    - `viz.py` : used to create a visual representation of winrate of each safeness
    - `xtractor.py` : used to simulate games and collect max depth data