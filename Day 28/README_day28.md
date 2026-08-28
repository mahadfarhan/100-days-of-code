# Day 28 — Pomodoro Timer

Day 28 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on building a **Pomodoro productivity timer** with Tkinter.

This project was completed as a guided course project. A substantial portion of the structure and implementation was written while following along with the instructor. Some sections differ from the course solution because of challenge prompts, independent problem-solving, debugging, and personal implementation choices.

## What This Day Covers

- Tkinter GUI development
- Canvas widgets
- Images in Tkinter
- Event-driven programming
- Scheduled callbacks with `after()`
- Cancelling callbacks with `after_cancel()`
- Managing application state
- Timer logic
- Work and break cycles
- Reset behavior
- Dynamic UI updates
- Preventing duplicate timer execution

## Project Structure

```text
Day 28/
├── main.py
├── tomato.png
└── README.md
```

## Pomodoro Timer

The application implements the Pomodoro technique using alternating work and break sessions.

### Default Timing

- Work session: 25 minutes
- Short break: 5 minutes
- Long break: 20 minutes

## Features

- Start button to begin the timer
- Alternating work and break sessions
- Long break after multiple work sessions
- Countdown display
- Dynamic title changes for work and break periods
- Checkmarks showing completed sessions
- Reset button
- Cancellation of an active scheduled timer
- Start button disabled while a timer is running
- Automatic transition between timer stages
- Tomato image displayed through a Tkinter `Canvas`

## How It Works

The application tracks the current Pomodoro cycle using a repetition counter.

Depending on the current repetition:

1. Odd-numbered repetitions begin a work session.
2. Even-numbered repetitions begin a short break.
3. The eighth repetition begins a long break.
4. Completed break cycles add a checkmark to the interface.
5. After the full cycle completes, the timer resets.

The countdown is driven by Tkinter's `after()` method rather than blocking the GUI with a sleep loop. This allows the application to remain responsive while the timer is running.

## Timer Scheduling

Each countdown step schedules the next update using:

```python
window.after(...)
```

The returned callback identifier is stored so the active timer can later be cancelled with:

```python
window.after_cancel(...)
```

This allows the Reset button to stop the current countdown cleanly.

## Reset Behavior

Resetting the timer:

- Cancels any active callback
- Clears the checkmarks
- Restores the timer display to `00:00`
- Restores the title to `Timer`
- Resets the repetition counter
- Re-enables the Start button
- Clears the stored timer reference

## Duplicate Timer Prevention

The Start button is disabled once a timer begins.

This prevents multiple independent `after()` callback chains from being started at the same time, which would otherwise cause overlapping countdowns.

## Concepts Practiced

- Tkinter
- GUI state
- Canvas
- `PhotoImage`
- Callback functions
- `after()`
- `after_cancel()`
- Global state
- Conditional logic
- Modulo operations
- Dynamic widget configuration
- Lists
- Timer formatting
- Application reset logic
- Event-driven programming

## Development Notes

Unlike several earlier projects in this repository that were built mostly or entirely independently from a project brief, Day 28 was primarily a **follow-along project**.

The overall project design, much of the starter structure, and portions of the implementation come directly from the course instruction. During challenge sections, debugging, and implementation steps, I also wrote or modified parts of the solution independently, which means my final code may differ from the instructor's version in some areas.

This repository keeps the project as part of my learning progression rather than presenting it as an entirely original implementation.

## Course Attribution

The project concept, UI design, project structure, instructional implementation, and challenge prompts originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance.

**The code in this project is not entirely my own. A significant portion was written while following along with Dr. Angela Yu's course. Some portions were independently implemented or modified by me during challenge exercises, debugging, and experimentation.**
