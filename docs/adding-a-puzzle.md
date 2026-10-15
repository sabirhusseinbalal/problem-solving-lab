# How to add a puzzle

Keep it simple: one folder for the question, a separate folder for answers.

## 1. You find a problem

You can use practice problems from [W3Resource's Python puzzles](https://www.w3resource.com/python-exercises/puzzles/), [Exercism](https://exercism.org/), or [MDN's web development challenges](https://developer.mozilla.org/en-US/docs/Learn_web_development). Practise and learn with these.

For example, the exercise called **“Length of Strings in List”** appears on W3Resource: https://w3resource.com/python-exercises/puzzles/python-programming-puzzles-14.php.

Before adapting an exercise from another source, check its license and reuse terms. Include the source and follow any attribution requirements. If permission to reuse or adapt the exercise is unclear, don't copy its wording or examples into this repository.

## 2. Propose it first

Open an issue with:

- What the problem asks
- Which skill it practises
- A small example and expected answer
- Where the idea came from, if it was inspired by something

Wait until the maintainer gives approval and assigns a number to it.

## 3. Add the problem statement

For an approved puzzle, create:

```text
puzzles/
└── 010-length-of-strings/
    └── README.md
```

Use the file template in [puzzle-template.md](puzzle-template.md). The puzzle README should include examples and edge cases along with the title and task and the answer should not be included.

## 4. Add a solution separately

A solution goes in a language folder:

```text
solutions/
└── 010-length-of-strings/
    └── python/
        └── your-github-username.py
```

Use the prefix `javascript/` for JavaScript, and a `.js` file extension. If you are making a small browser project, you should use the following directory: web/your-github-username/ and add only index.html, style.css and script.js as necessary.

## 5. Check it

Test all examples, test unusual examples, and ensure the written answer is correct. Utilize simple features for simple puzzles; modules/external libraries not to be used unless specified in the challenge.
