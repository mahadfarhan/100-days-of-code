# Snake Game

A recreation of the classic **Snake** game built with Python's Turtle module as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project was developed across two course days, so some intermediate versions of the code are also available in the Day 21 folder. The complete version of the game is available in the Day 22 folder.

## Features

- Keyboard-controlled snake movement
- Continuous movement using a game loop
- Snake growth after eating food
- Random food placement
- Score tracking
- Wall collision detection
- Tail collision detection
- Game-over display
- Prevention of immediate 180-degree turns
- Multi-file object-oriented project structure

## Controls

| Key | Action |
|---|---|
| `↑` | Move up |
| `↓` | Move down |
| `←` | Move left |
| `→` | Move right |

## Project Structure

The complete game is separated into multiple modules:

```text
snake-game/
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
└── README.md
```

### `main.py`

Creates the game screen, initializes the game objects, handles keyboard controls, runs the main game loop, and detects collisions with food, walls, and the snake's tail.

### `snake.py`

Contains the `Snake` class, which is responsible for:

- Creating the initial snake
- Moving the snake
- Adding new body segments
- Tracking the head
- Handling directional input
- Preventing the snake from immediately reversing into itself

### `food.py`

Contains the `Food` class.

The food is represented by a small Turtle object and is moved to a new random position whenever the snake eats it.

### `scoreboard.py`

Contains the `Scoreboard` class, which:

- Tracks the player's score
- Updates the displayed score
- Displays a game-over message when the player loses

## How It Works

1. The snake begins with three body segments.
2. Each segment follows the position of the segment directly in front of it.
3. The head moves forward continuously.
4. Arrow-key input changes the direction of the snake's head.
5. When the snake reaches the food:
   - A new body segment is added.
   - The food moves to a new random location.
   - The score increases.
6. If the snake hits a wall, the game ends.
7. If the snake's head collides with one of its own body segments, the game ends.

## Concepts Practiced

- Object-oriented programming
- Classes and inheritance
- Multiple Python modules
- Lists of objects
- Event listeners
- Game loops
- Coordinate systems
- Collision detection
- Object state
- Constants
- Slicing
- Turtle graphics
- Refactoring code into separate responsibilities

## Development Notes

This project was built across two course days rather than as a single exercise.

Because of that, earlier or intermediate versions of the code may also appear in the Day 21 folder. The complete implementation is stored in the Day 22 folder, while this README is intended to document the full Snake project from the master project folder.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
