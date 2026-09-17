# Day 44 — CSS Properties & The Box Model

Day 44 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** continued the CSS section by moving beyond basic selectors and introducing commonly used CSS properties, fonts, colors, and the CSS box model.

The day concluded with a **Motivation Meme Project**, combining the CSS concepts into a complete styled webpage.

## What This Day Covers

- CSS colors
- Named colors
- Hexadecimal colors
- Font families
- Generic font families
- Font sizes
- `px`
- `pt`
- `em`
- `rem`
- Font weight
- Text alignment
- Google Fonts
- CSS properties
- The CSS box model
- Width and height
- Padding
- Borders
- Margins
- Combining multiple CSS properties
- Styling a complete webpage

## Projects & Exercises

### 6.0 — CSS Colors

This exercise introduced CSS color properties and different ways of specifying colors.

The exercise covers:

- Named CSS colors
- Hexadecimal color values
- `color`
- `background-color`

The completed work applies these properties to the page elements to reproduce the target design.

### 6.1 — Font Properties

This section introduced CSS font properties and different units for controlling text.

#### Font Family

The `font-family.html` file is an instructional example provided as part of the course material to demonstrate different font-family options. It was used as a learning reference rather than being authored independently.

The example demonstrates font families including:

- Helvetica
- Arial
- Serif
- Sans Serif
- Cursive
- Monospace
- Fantasy

#### Font Size

Similarly, `font-size.html` is an instructional example provided for learning the different CSS font-size units.

It demonstrates:

- `px`
- `pt`
- `em`
- `rem`

It also demonstrates changing the root HTML font size and using relative units based on the parent or root element.

#### CSS Properties Exercise

The main `index.html` exercise is the part of this section implemented independently.

It combines several CSS properties:

- `color`
- `font-size`
- `font-weight`
- `font-family`
- `text-align`

It also uses the Google Font **Caveat** and changes the root HTML font size.

## 6.3 — CSS Box Model

This exercise introduced the CSS box model through three `<div>` elements.

Each box uses:

```css
width: 200px;
height: 200px;
```

The exercise then applies padding, borders, and margins to control the dimensions and positioning of the boxes.

The first box uses:

```css
padding: 20px;
border: 10px solid black;
```

The second uses different horizontal and vertical border widths, while the third uses a standard `10px` border.

Margins are used to position the boxes so that their corners touch.

The practical model is:

```text
Content
   ↓
Padding
   ↓
Border
   ↓
Margin
```

The Day 44 box-model work is a mix of course-provided structure and independently implemented styling, with the completed solution reflecting the concepts practiced during the exercise.

## 6.4 — Motivation Meme Project

The main project for Day 44 was a **Motivation Meme Project**.

The project combines HTML and CSS into a single styled webpage.

The requirements included:

- Using the **Regular Libre Baskerville** Google Font for the main `<h1>`
- White text
- Black background
- A custom image
- A `5px` white image border
- Center-aligned text
- A `<div>` containing the heading, paragraph, and image
- Centering the `<div>` using a `50%` width and `25%` left margin
- Making the image fill the width of the container
- Using `text-transform` to make the heading uppercase

The project was implemented using the HTML/CSS concepts introduced throughout the day, with the course providing the task and project structure.

## Project Structure

```text
Day 44/
├── 6.4 Motivation Meme Project/
│   ├── assets/
│   │   └── images/
│   │       └── daenerys.jpeg
│   ├── solution/
│   ├── goal.png
│   ├── index.html
│   └── style.css
│
└── exercises/
    ├── 6.0 CSS Colors/
    │   ├── goal.png
    │   ├── index.html
    │   └── solution.html
    │
    ├── 6.1 Font Properties/
    │   ├── font-family.html
    │   ├── font-size.html
    │   ├── goal.png
    │   ├── index.html
    │   └── solution.html
    │
    └── 6.3 CSS Box Model/
        ├── goal.png
        ├── index.html
        └── solution.html
```

## Concepts Practiced

- CSS colors
- Named colors
- Hex colors
- `color`
- `background-color`
- `font-family`
- `font-size`
- `font-weight`
- `text-align`
- `text-transform`
- Google Fonts
- `px`
- `pt`
- `em`
- `rem`
- Width and height
- Padding
- Borders
- Margins
- CSS box model
- Combining HTML and CSS
- External stylesheets

## Development Notes

Day 44 builds directly on the CSS selectors and styling concepts introduced previously.

The progression is:

**CSS selectors → CSS properties → fonts & colors → box model → complete styled webpage**

The day contains a mixture of instructional course material and independently implemented work. In particular, the `font-family.html` and `font-size.html` files in the 6.1 exercise are course-provided instructional examples, while the `index.html` exercise and much of the styling work throughout the day were implemented independently.

The Motivation Meme Project brings these concepts together into a complete styled webpage.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
