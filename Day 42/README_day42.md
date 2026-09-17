# Day 42 — HTML Lists, Nesting, Links & Images

Day 42 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** continued the introduction to HTML by expanding beyond basic headings and paragraphs into lists, nested elements, hyperlinks, and images.

The day also included a **Birthday Invite Project**, combining the HTML elements learned throughout the lesson into a single webpage.

## What This Day Covers

- HTML lists
- Ordered lists
- Unordered lists
- Nested lists
- HTML indentation
- Anchor elements
- Hyperlinks
- Image elements
- Image `src` attributes
- Image `alt` attributes
- Combining multiple HTML elements
- Building a simple webpage from multiple HTML components

## Projects & Exercises

### 3.0 List Elements

This exercise introduced HTML lists.

Unordered lists use:

```html
<ul>
    <li>Item</li>
</ul>
```

while ordered lists use:

```html
<ol>
    <li>Item</li>
</ol>
```

The exercise provided practice with creating lists and individual list items.

### 3.1 Nesting and Indentation

This exercise introduced placing HTML elements inside other elements.

For example, lists can be nested inside other lists:

```html
<ul>
    <li>A</li>
    <li>B
        <ol>
            <li>B1</li>
            <li>B2</li>
        </ol>
    </li>
</ul>
```

The exercise also emphasized indentation as a way of making nested HTML easier to read and understand.

### 3.2 Anchor Elements

The anchor element was introduced for creating hyperlinks:

```html
<a href="https://example.com">Visit the website</a>
```

The `href` attribute specifies the destination of the link.

The exercise created an ordered list of favourite websites, with each item containing a clickable link.

### 3.3 Image Elements

This exercise introduced the HTML `<img>` element for displaying images.

A basic image element uses:

```html
<img src="image.png" alt="Description of image">
```

The `src` attribute identifies the image resource, while the `alt` attribute provides alternative text describing the image.

The exercise included multiple image examples and demonstrated how images can be incorporated into an HTML document.

## Birthday Invite Project

The main project for Day 42 was a simple birthday invitation webpage.

The page includes:

- A main heading announcing the birthday
- A date
- A birthday-cake image
- A list of things to bring
- A location section
- A Google Maps link

The completed project combines several of the HTML elements introduced during the day.

For example, the page uses:

```html
<h1>It's My Birthday!</h1>
<h2>On 11th September</h2>
```

an image:

```html
<img src="..." alt="Birthday cake">
```

an unordered list for the items guests should bring, and an anchor element for the location link.

## Project Structure

```text
Day 42/
├── 3.4 Birthday Invite Project/
│   ├── goal.png
│   ├── index.html
│   └── solution.html
│
└── exercises/
    ├── 3.0 List Elements/
    │   ├── goal.png
    │   ├── index.html
    │   └── solution.html
    │
    ├── 3.1 Nesting and Indentation/
    │   ├── goal.png
    │   ├── index.html
    │   └── solution.html
    │
    ├── 3.2 Anchor Elements/
    │   ├── goal.png
    │   ├── index.html
    │   └── solution.html
    │
    └── 3.3 Image Elements/
        ├── goal1.png
        ├── goal2.png
        ├── index.html
        ├── solution1.html
        └── solution2.html
```

## Concepts Practiced

- `<ul>`
- `<ol>`
- `<li>`
- Nested HTML elements
- HTML indentation
- `<a>`
- `href`
- `<img>`
- `src`
- `alt`
- Combining HTML elements
- Structuring webpage content
- Creating hyperlinks
- Embedding images

## Development Notes

Day 42 builds directly on the basic HTML structure introduced on Day 41.

The progression is:

**Headings & paragraphs → lists → nested elements → links → images → complete webpage**

The Birthday Invite Project brings these concepts together into a small but complete HTML page, providing practice with structuring content and connecting different HTML elements.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
