# Turtle Crossing Game

A Turtle graphics game built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

The player controls a turtle trying to cross a road filled with moving cars. Each successful crossing increases the level and makes the traffic move faster.

## Features

- Keyboard-controlled player movement
- Random car generation
- Continuous traffic movement
- Increasing difficulty after each successful crossing
- Collision detection between the player and cars
- Level tracking
- Game-over display
- Automatic player reset after reaching the finish line
- Cleanup of cars that leave the screen
- Multi-file object-oriented structure
- Custom car sprite support

## Controls

| Key | Action |
|---|---|
| `↑` | Move forward |

## Project Structure

```text
turtle-crossing/
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
├── car.gif
└── README.md
```

### `main.py`

Controls the main game loop and coordinates interactions between the player, car manager, and scoreboard.

It is responsible for:

- Creating the game screen
- Listening for keyboard input
- Creating and moving cars
- Checking whether the player reaches the finish line
- Increasing the level and car speed
- Detecting collisions
- Ending the game when the player is hit

### `player.py`

Contains the `Player` class, which manages:

- Player creation
- Forward movement
- Starting position
- Finish-line detection
- Resetting the player after completing a level

### `car_manager.py`

Contains the `CarManager` class, which manages:

- Random car generation
- Car movement
- Current traffic speed
- Speed increases between levels
- Removing cars that leave the screen
- Clearing all cars after a completed level
- Registering and using the custom car sprite

### `scoreboard.py`

Contains the `Scoreboard` class, which:

- Tracks the current level
- Updates the level display
- Displays a game-over message

## How It Works

1. The player begins at the bottom of the screen.
2. Pressing the Up Arrow moves the turtle forward.
3. Cars are generated randomly on the right side of the screen.
4. Each car travels horizontally across the road.
5. When the player reaches the finish line:
   - The player returns to the starting position.
   - The level increases.
   - Traffic speed increases.
   - Existing cars are cleared.
6. Cars that travel off-screen are removed from the active car list.
7. If the player's bounding area overlaps with a car's bounding area, the game ends.

## Collision Detection

Collision detection is handled using explicit coordinate overlap checks rather than only measuring distance between object centers.

The game compares the horizontal and vertical bounds of the player and each car to determine whether their rectangular areas overlap.

## Concepts Practiced

- Object-oriented programming
- Classes and inheritance
- Multiple Python modules
- Event listeners
- Game loops
- Randomization
- Lists of objects
- Coordinate systems
- Collision detection
- Object state
- Constants
- Difficulty scaling
- Safe list modification
- Custom Turtle shapes
- Separation of responsibilities

## Implementation Notes

The car manager maintains a list of active cars and uses a copied snapshot of that list when removing cars that have left the screen. This avoids modifying the same list while iterating over it.

Difficulty increases by raising the distance each car moves per game-loop iteration after the player completes a level.

The game also uses a custom `car.gif` sprite instead of the default Turtle shapes.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored in this project was written independently by me.**
