# Bug-Run
Practice Game Made using Pygame

Summary:
Bug-Run is a basic game designed to allow users to easily create their own levels with minimal hassle or programming knowledge.

# Gameplay:
Blocks fall from the top of the screen. The player needs to dodge them all in order to survive. Certain blocks can be tagged a power up which enables the user to absorb one hit.

# Running the game:
Ensure python is installed and you can run python scripts.

Clone this repo locally, then enter _python bug-run.py_ and install requirements as needed. (The only extra library to install should be pygame).

# Custom levels: 
Can easily be created by making a json file with appropriate entries. A level consists of a list of lists.

The outer list holds every block collection in the level.
An inner list consists of the blocks which will all drop at one point in time. (When the prior blocks reach the bottom of the screen).

The inner lists are populated by blocks with the following attributes:

**id:** Two options: 1, which indicates a block to be dodged, or 2, which indicates an invulnerability powerup.

**x:** The X coordinate where the block drops in from.

**y:** The Y coordinate where it starts at. Traditionally set to -600.

**w:** The width of the block.

**h:** The height of the block.

**s:** The speed of the block.

**color:** List of RGB values. e.g. [0,255,0] results in a green block.


