# GitHub Actions – Exercises 

## Exercise 1: Hello World Workflow

**Task:** Create a workflow that prints `Hello, GitHub Actions!` whenever code is pushed to the `main` branch.

---

## Exercise 2: Checkout Repository

**Task:** Extend the Hello World workflow to also checkout the repository.



---

## Exercise 3: Run on Pull Requests

**Task:** Modify the workflow so it runs on both `push` to `main` and on **pull requests** targeting `main`.

---

## Exercise 4: Manual Trigger

**Task:** Add a manual trigger so the workflow can be run from the GitHub UI.

---

## Exercise 5: Multiple Jobs

**Task:** Create two jobs:

1. `build` → prints "Building project".
2. `test` → prints "Running tests".
---

## Exercise 6: Job Dependencies (`needs`)

**Task:** Make the `test` job run **only after** the `build` job finishes.

---

## Exercise 7: Environment Variables

**Task:** Define an environment variable `APP_ENV=development` at the workflow level and print it in a job.

---

## Exercise 8: Step-Level Variables

**Task:** Use a job variable `STAGE=test` and print it only within a single step.

---

## Exercise 9: Conditional Execution

**Task:** Add a deploy job that only runs if the branch is `main`.

---

## Exercise 10: Full Practical Workflow

**Task:** Build a workflow with:

* `build` job → echo "Building"
* `test` job → runs after build → echo "Testing"
* `deploy` job → runs after test **only if branch is main** → echo "Deploying"

---

<div style="text-align: left;">
  <a href="../solution/01_Activity_Github_Actions_Solutions.md"><b> Day 1: Solutions</b></a>
</div>
