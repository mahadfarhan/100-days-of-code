# Day 43 — Introduction to CSS

Day 43 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** continued the transition into web development by introducing **CSS (Cascading Style Sheets)**.

After using HTML to structure webpages, this day focused on using CSS to control their appearance and presentation.

## What This Day Covers

- CSS fundamentals
- Adding CSS to HTML
- Inline CSS
- Internal CSS
- External stylesheets
- CSS selectors
- Element selectors
- Class selectors
- ID selectors
- Attribute selectors
- Universal selectors
- CSS properties
- Styling text
- Changing colors
- Changing font weight
- Setting element dimensions
- Combining HTML and CSS

## Projects & Exercises

### 5.1 — Adding CSS

This exercise introduced the three main ways of adding CSS to an HTML document:

1. **Inline CSS**
2. **Internal CSS**
3. **External CSS**

The exercise includes separate HTML files demonstrating each method.

#### Inline CSS

CSS can be placed directly on an HTML element using the `style` attribute:

```html
<h1 style="color: blue;">Style Me in Blue!</h1>
```

This applies styling directly to that individual element. 

#### Internal CSS

CSS can be placed inside a `<style>` element within the HTML document's `<head>`:

```html
<style>
    h1 {
        color: red;
    }
</style>
```

The exercise demonstrates applying this approach to an HTML page. 

#### External CSS

CSS can be placed in a separate stylesheet and linked from the HTML document:

```html
<link rel="stylesheet" href="./style.css" />
```

The external stylesheet approach separates page structure from styling. 

## 5.3 — CSS Selectors

The CSS Selectors exercise introduced different ways of targeting HTML elements.

The exercise specifically practices:

- Element selectors
- Class selectors
- ID selectors
- Attribute selectors
- Universal selectors

The provided HTML includes tasks for changing paragraph color, styling elements with a particular class, targeting an element by ID, selecting an element based on an attribute value, and applying styling to all elements. 

The completed CSS uses these selector types:

```css
#id-selector-demo {
    color: green;
}

.note {
    font-size: 20px;
}

* {
    text-align: center;
}

p {
    color: red;
}

li[value="4"] {
    color: blue;
}
```

## 5.4 — Color Vocab Project

The main project for the day was the **Color Vocab Project**.

The webpage presents five Spanish color words:

- Rojo
- Azul
- Anaranjado
- Verde
- Amarillo

Each color heading has an ID that can be targeted from CSS, while the images are stored in an `assets/images` directory. 

The CSS solution uses the IDs to apply the corresponding colors:

```css
#orange {
    color: orange;
}

#green {
    color: green;
}

#red {
    color: red;
}

#blue {
    color: blue;
}

#yellow {
    color: yellow;
}
```

It also uses a class selector to change the font weight of the color headings and an element selector to set all images to `200px` by `200px`. 

The project instructions specifically required these changes to be made through CSS rather than modifying the HTML.

## Project Structure

```text
Day 43/
├── 5.4 Color Vocab Project/
│   ├── assets/
│   │   └── images/
│   │       ├── blue.png
│   │       ├── green.png
│   │       ├── orange.png
│   │       ├── red.png
│   │       └── yellow.png
│   ├── index.html
│   ├── style.css
│   └── solution/
│       ├── assets/
│       │   └── images/
│       ├── solution.html
│       └── style.css
│
└── exercises/
    ├── 5.1 Adding CSS/
    │   ├── external.html
    │   ├── index.html
    │   ├── inline.html
    │   ├── internal.html
    │   └── Solution/
    │       ├── external.html
    │       ├── inline.html
    │       ├── internal.html
    │       ├── solution.html
    │       └── style.css
    │
    └── 5.3 CSS Selectors/
        ├── goal.png
        ├── index.html
        ├── style.css
        └── solution/
```

## Concepts Practiced

- CSS syntax
- CSS rules
- Selectors
- Properties and values
- Inline styles
- Internal stylesheets
- External stylesheets
- Element selectors
- Class selectors
- ID selectors
- Attribute selectors
- Universal selectors
- `color`
- `font-weight`
- `width`
- `height`
- Linking CSS files to HTML
- Separating structure from presentation

## Development Notes

Day 43 builds directly on the HTML fundamentals from Days 41 and 42.

The progression is:

**HTML structure → HTML elements → CSS → HTML + CSS**

HTML provides the structure and content of the page, while CSS provides the styling and visual presentation.

The Color Vocab Project brings the selector concepts together by using IDs, classes, and element selectors to style different parts of the page.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
