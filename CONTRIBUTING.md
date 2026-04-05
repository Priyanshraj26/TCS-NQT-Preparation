# Contributing to TCS NQT Preparation

Thank you for your interest in improving this repository!

## How to Contribute

### Adding Questions
1. Create a new `.md` file in the appropriate topic folder under `02-Coding/DSA-Questions/`
2. Follow the existing question format (see any existing file for reference)
3. Include: problem statement, input/output format, constraints, examples, hints, tags

### Adding Solutions
1. Create matching solution file in `02-Coding/Solutions-CPP/`
2. Include both brute force and optimized approaches
3. All C++ code must compile with `g++ -std=c++17 -Wall`
4. Include `main()` with test cases

### Fixing Errors
- Fix typos, incorrect answers, or compilation errors
- Update complexity analysis if incorrect
- Improve explanations for clarity

### Updating PDFs
1. Edit the relevant script in `scripts/`
2. Run the script to regenerate the PDF
3. Verify the PDF opens correctly

## Guidelines
- Keep formatting consistent with existing files
- Test all code before submitting
- One change per pull request when possible
- Describe what and why in your commit message

## Code Style (C++)
- Use `#include <bits/stdc++.h>` or specific headers
- Use `using namespace std;`
- Class-based solutions preferred
- 4-space indentation
- Meaningful variable names
