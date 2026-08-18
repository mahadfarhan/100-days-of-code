# Day 22 — Pong

A two-player recreation of **Pong** built with Python's Turtle module as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project was built as a multi-file object-oriented game, with separate classes for the ball, paddles, scoreboard, and center divider.

## Features

- Two-player keyboard controls
- Continuous ball movement
- Paddle collision detection
- Top and bottom wall bouncing
- Variable vertical ball movement after paddle collisions
- Score tracking for both players
- Automatic round reset after a point is scored
- Paddle reset after each point
- Short pause between rounds
- Center divider
- Multi-file object-oriented project structure

## Controls

| Player | Key | Action |
|---|---|---|
| Left Paddle | `W` | Move up |
| Left Paddle | `S` | Move down |
| Right Paddle | `↑` | Move up |
| Right Paddle | `↓` | Move down |

## Project Structure

```text
Day 22/
├── main.py
├── ball.py
├── paddle.py
├── scoreboard.py
├── divider.py
└── README.md
```

### `main.py`

Controls the overall game flow.

It is responsible for:

- Creating the screen
- Creating both paddles
- Creating the ball
- Creating both scoreboards
- Creating the divider
- Registering keyboard controls
- Running the game loop
- Detecting paddle collisions
- Detecting wall collisions
- Detecting scoring
- Resetting the round after a point

### `ball.py`

Contains the `Ball` class, which manages:

- Horizontal movement
- Vertical movement
- Randomized starting vertical direction
- Horizontal bouncing
- Vertical bouncing
- Changing vertical direction based on paddle contact
- Returning to the center after a point

### `paddle.py`

Contains the `Paddle` class, which manages:

- Paddle creation
- Up and down movement
- Screen-boundary limits
- Resetting to the starting position after a point

### `scoreboard.py`

Contains the `Scoreboard` class, which:

- Stores each player's score
- Displays the score
- Updates the display when a player scores

### `divider.py`

Creates the dashed vertical divider in the center of the screen.

## How It Works

1. The game creates two paddles on opposite sides of the screen.
2. The ball begins moving continuously across the play area.
3. Each player controls their paddle independently using the keyboard.
4. When the ball reaches the top or bottom boundary, its vertical direction is reversed.
5. When the ball reaches a paddle:
   - Its horizontal direction is reversed.
   - Its vertical movement is adjusted depending on whether it hit above or below the paddle's center.
6. If the ball passes beyond a paddle:
   - The opposing player's score increases.
   - The ball returns to the center.
   - Both paddles reset to their starting positions.
   - The game pauses briefly before the next round.
7. The game continues indefinitely.

## Concepts Practiced

- Object-oriented programming
- Classes and inheritance
- Multiple Python modules
- Event listeners
- Keyboard controls
- Game loops
- Collision detection
- Coordinate systems
- Randomization
- State management
- Constants
- Refactoring
- Separation of responsibilities
- Real-time graphical programs

## Implementation Notes

The ball's horizontal and vertical movement are handled independently.

Horizontal bouncing is done by reversing the sign of the horizontal movement amount, while wall collisions reverse the vertical movement.

Paddle collisions also modify the ball's vertical movement so that the return angle can vary rather than remaining identical after every hit.

Game timing is controlled from the main game loop rather than from inside the `Ball` class, keeping movement logic and frame timing separate.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
