# CS 1440 Project 1: Tic-Tac-Toe - Instructions

Since you are still new to using Git, refer to the **Using Git** section of the lecture notes when you need help remembering which command to use to push your work to the server.

Previous Semester Statistics     | Fall 2023 | Spring 2024 | Fall 2024
--------------------------------:|:---------:|:-----------:|:---------:
Average Hours Spent              | 7.225     | 7.34        | 5.523
Standard Deviation Hours         | 3.753     | 4.013       | 3.263
% students thought this was Easy | 21.2%     | 13.4%       | 12.9%
... Medium                       | 40.4%     | 43.8%       | 30.6%
... Hard                         | 26.0%     | 33.3%       | 38.8%
... Too Hard/Did not complete    | 12.5%     | 9.4%        | 17.6%



*   [AI Tools / External Resources Policy](#ai-tools-external-resources-policy)
*   [How to Do This Project](#how-to-do-this-project)
    *   [Phase 0: Requirements Analysis](#phase-0-requirements-analysis)
    *   [Phase 1: Design](#phase-1-design)
    *   [Phase 2: Implementation](#phase-2-implementation)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging)
    *   [Phase 4: Deployment](#phase-4-deployment)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [Hints](#hints)
*   [What We Look for When Grading](#what-we-look-for-when-grading)



## AI Tools / External Resources Policy

I will not accept code or documentation that is not 100% your own creation.

You may use AI and external resources in ways that assist your understanding without replacing your effort or responsibility to learn.

Acceptable uses include:

*   Analyzing project instructions.
*   Understanding why and how starter code works.
*   Brainstorming ideas for a prototype.
*   Researching and explaining error messages.
*   Proofreading your documentation.

Unacceptable uses include:

*   Generating code, including unit tests.
*   Debugging your code or suggesting fixes.
*   Writing parts of your software plan or any other deliverable.

If you're stuck, ask for help before resorting to shortcuts or risking a violation.


## How to Do This Project


This project is larger than the homework assignments in CS 1400 and CS 1410.  Do not try to complete it in one sitting.  The theme of this project is "it gets worse before it gets better."  Start early because you should expect to get stuck a few times before you finish.

The problem is that the AI can lose.  It is your job to find out why.  You will uncover the causes as you study the documentation and code.  Apart from the intentional AI bug, this program works as intended.  If you see anything else which looks wrong, **just leave it alone**.  I will make a public announcement if another serious issue is discovered.


### Phase 0: Requirements Analysis
*(20% of your effort)*

0.  Read the [Project Requirements](./Project_Requirements.md) to understand what the project is about.
1.  Study the *Software Development Plans* written by the previous teams.
    *   [AI team's SDP](./AI_Team_Plan.md)
    *   [Game Engine team's SDP](./Engine_Team_Plan.md)
    *   You should understand these documents well enough to find your way around the source code.
    *   Use an AI chat bot (i.e. ChatGPT, Gemini, Claude, Mistral) to help you understand these documents.
    *   Pay special attention to the test cases the previous teams wrote.  After you fix the bug, use these tests to verify your solution.
2.  Run the program several times to learn what it does.
    *   Use the debugger to identify which functions perform what actions.
3.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the project is due
4.  Reorganize the program into **five** modules.  Look out for issues in the code, but **DO NOT DELETE ANY CODE IN THIS PHASE.**
    1.  `ttt.py` - the main entry point of the program.
        *   No functions are defined in this module (i.e. the `def` keyword does not appear in this file).
        *   This file should be short! (my solution is only two dozen lines.)
    2.  `interface.py` - contains functions that take input from the user and create colorful output.
        *   This is the *only* file where the `input()` function is directly called.
        *   Many (but not all) functions that use `print()` belong in this module.
        *   Functions that return *terminal escape sequences* belong here, as do functions that deal with colors.
        *   This module *does not* import any other modules to prevent *circular import* errors.
    3.  `lut.py` - contains the *Look Up Table* (LUT) which the strategy functions refer to.
        *   Take care when moving this code; there are no bugs in the LUT.
        *   Moving this giant hunk of code into its own module makes the rest of the program easier to navigate.
        *   This module *does not* import any other modules to prevent *circular import* errors.
    4.  `ai.py` - the strategy functions which power the CPU opponent are defined here.
        *   The strategy functions have names beginning with `strategy_`.
        *   Functions that examine or manipulate the game board are not defined here.  They are imported from another module.
        *   Import the LUT from the `lut` module.
    5.  `engine.py` - is home to functions that drive the main game loop, deal with the game board, or don't belong anywhere else.
        *   There are four different game loops, one for each mode
            1.  CPU vs. CPU
            2.  human vs. CPU
            3.  CPU vs. human
            4.  human vs. human
        *   Code in this module *may* print messages with the help of functions imported from `interface.py`.
        *   Functions that call `input()` do not belong in this module.
        *   Some functions belonging to this module will need to be modified if the format of the game board changes.
    *   Consider every function on its own merits.  Don't keep functions together simply because they were neighbors in the original program.
5.  The program won't work after you remodel it.  As the saying goes, *you can't make an omelette without breaking eggs*.  You will tackle the new problems you created in the next phase.  Here is a preview of the errors you will find:
    *   Moving functions into different modules will result in error messages like this:
        ```
        NameError: name 'logo' is not defined
        ```
        It will be necessary to add `import` statements to restore the program to functionality.
        *   Take care to avoid *circular imports*, which lead to error messages like this:
            ```
            ImportError: cannot import name 'show' from partially initialized module 'interface' (most likely due to a circular import)
            ```
            Circular imports happen when a module ends up importing itself.  For example, a circular import occurs when interface.py imports `engine`, and engine.py imports `interface`.
        *   Circular imports are resolved by breaking the cycle by creating a module that does not import anything else.
6.  Track your time in Signature.md.
7.  Add new files to Git with `git add`.  Run `git status` to identify such files and check that they are ready to commit.


### Phase 1: Design
*(30% of your effort)*

By now you have seen all of the code and have a better understanding of how and why it works.

0.  Resolve the `NameError`s so the program runs again.
1.  Turn back to the *duplicated* functions you discovered and ponder these questions:
    *   *Why were there two versions of these functions?*
    *   *What does this tell you about each team's conception of the game?*
    *   *How can you untangle the mess they created?*
        *   There are two obvious ways to fix this program:
            1.  Rewrite the functions that have faulty assumptions about how the game board is tracked.  Identify the smallest subset of functions that are affected to avoid rewriting the entire program.
            2.  Design one or two *adapter* functions to translate the game board representation as needed.
2.  Consider what new test cases could ensure the new program will perform correctly.
3.  You should be able to get 100% on the **Starter Code Quiz** by now.
4.  Track your time in Signature.md.
5.  Commit your changes to Git (use `git status` to identify files that have changed).


### Phase 2: Implementation
*(15% of your effort)*

0.  Now you may delete useless functions.  Carefully choose which functions are kept and removed.
1.  Apply the other changes you designed to the source code.
    *   Be patient and take your time.
    *   Update comments that are made obsolete by your changes.
    *   It is normal to introduce new bugs as you go.  Here are some hints:
        *   Rename variables and functions to improve the readability of the program.  Good names make it easy to spot bugs.
        *   When testing the CPU player, set `CPU_DELAY` to a smaller value to speed things up.  Remember to restore it to the original value before you turn in the project.
        *   It is very likely that you will encounter *off-by-one* errors.  Think hard and run lots of tests before you try to fix these.
        *   If you make a change but don't see the result, take another look for duplicated functions.
        *   If you rename a function or add a new function, update your `import` statements.
        *   Ask for help before you get overwhelmed!
        *   Frequently commit your work to Git.  It makes it easier for us when you come for help.
2.  If you feel that you just made things worse, go back to **Phase 1** and design a new approach.  Ask the instructor and TAs for help with Git if you want to undo some of your changes.
3.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes regularly!
4.  Track your time in Signature.md and commit your changes to Git.


### Phase 3: Testing and Debugging
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

0.  Run through the test cases documented by the previous teams in their software plans.
1.  Run through any new test cases that you devised.
2.  If you found bugs in this phase, explain what was wrong and how you fixed it.
3.  Track your time in Signature.md and commit your changes to Git.


### Phase 4: Deployment
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Project](./How_To_Submit.md) and make sure that your submission is correct.
1.  Push your code to GitLab, then check that all files and commits are there.
2.  Clone your project into a *different directory* on your computer and re-run your test cases.


### Phase 5: Maintenance

**Before The Due Date**

0.  Review Signature.md one last time.
1.  Make one final commit and push your **completed** Signature.md to GitLab.
2.  Make sure that you are happy with your **Starter Code Quiz** score.
3.  Respond to the **Project Reflection Survey** on Canvas.



## Hints

Here are some tips for when you think you've found the bug in Tic-Tac-Toe but are unsure of the next steps.

*   The bug is **not** in the LUT.
*   Read both of the software plans (from the AI and Engine teams) before debugging the program.
    *   After you find the bug, take another look at those documents.  What assumptions does each team make about the game board?
*   Consider how you can use the REPL and print statement debugging to answer the question "why does this happen?"
*   When you re-arrange functions into separate modules, **do not delete anything**.
    *   Instead of deleting unused functions, rename them to make it clear that they are useless:
        *   ```python
            def full(board):
            ```
        *   becomes...
        *   ```python
            def UNUSED_full(board):
            ```
    *   Only delete the `UNUSED_` functions after you are positive that the program works without them.
*   In the past students have lost important pieces of the puzzle when re-arranging the code into modules.  While it is possible to recover the missing code with Git, at this point you haven't been taught all of the necessary commands.
    *   If have lost an important bit of code, you can find it by looking at the original version of ttt.py in my repository: https://gitlab.cs.usu.edu/duckiecorp/cs1440-falor-erik-proj1/-/blob/master/src/ttt.py



## What We Look for When Grading

**Total points: 90**

*   Repository Structure (10 points)
    *   `.gitignore` is correct and no forbidden files or directories are present
    *   The repository is a clone of the starter code
    *   The repository's GitLab URL follows the naming convention
    *   All required files and directories are in their expected locations
    *   There is at least one Git commit per phase of the project.
*   Time management (5 points)
    *   Signature.md contains accurate information about the time you spent on this project
        *   The time reported on the **TOTAL** entry is the sum of the daily entries
    *   The *TODO* message and the placeholder entries have been removed
*   Code quality (35 points)
    *   Functions are organized into the correct modules
    *   No useless variables or constants remain
    *   No useless or redundant functions remain; each function is present in only one module
        *   Exceptions
            *   Unused strategy functions *may* be kept for testing
            *   Unused color functions *may* be kept for future development
    *   Doc strings and comments match the code they describe
    *   Import statements are reasonable
        *   No useless import statements are present
        *   Program *does not* import any modules **except**:
            *   `random`
            *   `time`
            *   `typing`
            *   modules you wrote yourself
        *   No import statement fails due to misspelling or incorrect capitalization
            *   **Windows users** make sure that the capitalization of file names on GitLab match your `import` statements!
        *   No imports involve the `src.` package; this is the result of a PyCharm misconfiguration
*   Program behavior (40 points)
    *   Be sure to test your program from the command line, not just in PyCharm
        *   Testing only in PyCharm is not sufficient
    *   AI opponent is unbeatable
        *   CPU vs. CPU matches always end in a draw
        *   Human vs. CPU matches end either in a draw or CPU victory
    *   Existing good behavior of program is preserved
        *   The user interface and appearance is unchanged from the starter code
        *   The Easter Egg is still accessible just as it was in the original program
    *   No new bugs
        *   Program doesn't crash
        *   Illegal user input is detected by the program and an appropriate error message is displayed
    *   All test cases work as expected
