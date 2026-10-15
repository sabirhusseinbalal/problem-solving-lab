# Contributing

Thanks for helping! Limit contributions to simplicity, clarity and testing.

## What can I add?

- Any solution of an existing puzzle in another language.
- Correction or clarification.
- A brand new and original puzzle.

Use simple features of the language, and no external modules/libraries (unless the puzzle states otherwise) for beginner solutions. Do not use a pre-made helper if the puzzle clearly states that it is not to be used. Use functions when they make the solution clearer.

## Where files go to?

**Puzzle statement:** `puzzles/001-missing-number/README.md`

**Python solution:** `solutions/001-missing-number/python/YOUR-GITHUB-USERNAME.py`

**JavaScript solution:** `solutions/001-missing-number/javascript/YOUR-GITHUB-USERNAME.js`

**Small web solution:** `solutions/PUZZLE-ID/web/YOUR-GITHUB-USERNAME/` Include `index.html`. Add `style.css` and `script.js` if needed. An optional `README.md` can explain how to run the project.

Do not overwrite another contributor's solution. Add your solution as a separate file using your GitHub username in the filename.

## Adding a new puzzle

1. create a GitHub issue; present your idea first.
2. Wait until the maintainer says the number of the puzzle and folder name.
3. Create a problem statement to file as `puzzles/NUMBER-short-name/README.md`.
4. Present clear rules, examples, and outcomes. Check every example.
5. Do not put an answer in the puzzle statement, put solutions in `solutions/`.

New puzzle statements must be written and checked by a person. Do not submit AI-generated puzzle statements.

If you adapt an exercise from another source, credit the source and check its license or reuse terms. A link alone does not give permission to copy or adapt its content.

AI and documentation may be used for learning, grammar checks, and code feedback. Disclose meaningful AI assistance in a pull request.

Learn from AI or documentation, check grammar or review your own code. Be honest when it comes to meaningful AI assistance in pull request.

## How to fork and send a pull request

1. Open this repo on GitHub and click **Fork**. This creates your own copy.
2. Open a terminal and clone **your fork**. Replace `YOUR-USERNAME` with your GitHub username:

   ```bash
   git clone https://github.com/YOUR-USERNAME/problem-solving-lab.git
   cd problem-solving-lab
   git switch -c add-solution-001
   ```

3. Add your file in the correct folder shown above.
4. Save and test your code. Then run:

   ```bash
   git add .
   git commit -m "Add Python solution for puzzle 001"
   git push -u origin add-solution-001
   ```

5. Open your fork on GitHub and click **Compare & pull request**. Make sure the base repository is the original `problem-solving-lab`, not your fork.
6. Explain what you added and how you tested it. Then submit the pull request.

For a new puzzle, replace `add-solution-001` with a branch name such as `add-puzzle-010` and use the puzzle folder approved by the maintainer.

## Before you submit

- [ ] I have the correct folder and file name.
- [ ] I checked the following examples and edge cases:
- [ ] I can explain my solution.
- [ ] I did not take another person's file.
- [ ] Quoted and cited sources if necessary.
- [ ]  I didn't enter passwords, API keys or any private information.

When you submit a contribution you certify that it can be shared under this repository's license (MIT). Do NOT submit work that you don't have the right to share.

All Pull Requests are checked. The maintainer might request changes prior to merging. Any helpful comment will be attributed to the GitHub user.
