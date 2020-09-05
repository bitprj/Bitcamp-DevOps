# Using Community Actions

This is a "final," so to speak, but a relatively relaxed one. You won't be given much in the way of direction (unless you need hints!), so use your ingenuinity and Google skills to solve this one!

The task at hand: You have here a .md file ridden with spelling errors, and a python function and associated test file. You need to automate the testing process for these files, meaning on a pull request your .md file should be checked for spelling errors, and the python file should be tested by its test file.

__Requirements__

  - Find a way to test the .md file for spelling errors.
    - As it stands, this test should __fail__. Be careful, however, to make sure it fails because of the typos, and *not* because of the proper nouns (like "Horatio" and "Yorrick")
  - Find a way to implement python unit testing, given a test file and function to be tested.
    - This test should succeed.
    
These things should be accomplished via community actions! If you're stuck, I'll show the ones I used, but there's no requirement as to which one you use. Just make sure it has the functionalities you need, and make it work.

If you're stuck, here are some hints:

<details><summary> Hint #1!</summary>
Python actually has its testing as part of GitHub's official documentation. The spellchecker does not. Here are the two sources I used for my version:

https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions

https://github.com/marketplace/actions/run-pyspelling-as-a-github-action
</details>

<details><summary> Hint #2!</summary>
Your dictionary action should let you add a custom wordlist to filter out the words that aren't typos. Check out the documentation for your community action of choice - my one (linked above) had examples of how this worked in the linked repository. Yours might too.
</details>

<details><summary> Hint #3!</summary>
For the Python test, check the official documentation on how to make it work. The section of interest is probably "Testing with pytest and pytest-cov."
</details>
