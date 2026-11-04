
#  GitHub Actions – Exercises with Solutions & Execution Steps

## Exercise 1: Hello World Workflow

**Task:** Create a workflow that prints `Hello, GitHub Actions!` whenever code is pushed to the `main` branch.

**Steps to Execute:**

1. In your repo, create a folder `.github/workflows/`.
2. Create a file `hello.yml`.
3. Paste the workflow code below.
4. Commit and push to the `main` branch.
5. Go to **Actions tab** in GitHub → confirm workflow runs.

 **Solution:**

```yaml
name: Hello World

on:
  push:
    branches: [ main ]

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello, GitHub Actions!"
```

---

## Exercise 2: Checkout Repository

**Task:** Extend the Hello World workflow to also checkout the repository.

**Steps to Execute:**

1. Edit `hello.yml`.
2. Add a step using `actions/checkout@v4`.
3. Push changes to `main`.
4. Check Actions tab → logs should show "Hello, GitHub Actions!".

**Solution:**

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4
  - name: Print message
    run: echo "Hello, GitHub Actions!"
```

---

## Exercise 3: Run on Pull Requests

**Task:** Modify the workflow so it runs on **push to main** and **pull requests**.

**Steps to Execute:**

1. Edit workflow file.
2. Add `pull_request` trigger.
3. Open a pull request in GitHub.
4. Check Actions tab → workflow should run.

**Solution:**

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

---

## Exercise 4: Manual Trigger

**Task:** Add a manual trigger so the workflow can be run from the GitHub UI.

**Steps to Execute:**

1. Edit workflow file.
2. Add `workflow_dispatch`.
3. Push changes.
4. Go to **Actions → Select Workflow → Run workflow button**.

**Solution:**

```yaml
on:
  workflow_dispatch:
```

---

## Exercise 5: Multiple Jobs

**Task:** Create two jobs: `build` and `test`.

**Steps to Execute:**

1. Create a new file `multi-jobs.yml`.
2. Define both jobs.
3. Push to main.
4. Check Actions tab → both jobs run in parallel.

**Solution:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building project"

  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running tests"
```

---

## Exercise 6: Job Dependencies (`needs`)

**Task:** Make `test` run **only after** `build`.

**Steps to Execute:**

1. Edit `multi-jobs.yml`.
2. Add `needs: build` to `test`.
3. Push to main.
4. Check Actions → verify `build` runs first, then `test`.

**Solution:**

```yaml
test:
  runs-on: ubuntu-latest
  needs: build
  steps:
    - run: echo "Running tests after build"
```

---

## Exercise 7: Environment Variables

**Task:** Define `APP_ENV=development` at workflow level and print it.

**Steps to Execute:**

1. Create file `env-vars.yml`.
2. Add workflow-level `env`.
3. Push to main.
4. Logs should show: `App environment is development`.

**Solution:**

```yaml
env:
  APP_ENV: development

jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - run: echo "App environment is $APP_ENV"
```

---

## Exercise 8: Step-Level Variables

**Task:** Use a step-level variable `STAGE=test` and print it.

**Steps to Execute:**

1. Edit `env-vars.yml`.
2. Add `env` under a specific step.
3. Push to main.
4. Logs should show: `Stage = test`.

**Solution:**

```yaml
jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - name: Print stage variable
        run: echo "Stage = $STAGE"
        env:
          STAGE: test
```

---

## Exercise 9: Conditional Execution

**Task:** Add a deploy job that runs **only on main branch**.

**Steps to Execute:**

1. Create file `conditional.yml`.
2. Add `if: github.ref == 'refs/heads/main'`.
3. Push to main.
4. Check Actions tab → job runs only if push was to `main`.

**Solution:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Deploying to production"
```

---

## Exercise 10: Full Practical Workflow

**Task:** Create a pipeline with 3 jobs:

* `build` → echo "Building"
* `test` → runs after build → echo "Testing"
* `deploy` → runs after test, only if branch = main → echo "Deploying"

**Steps to Execute:**

1. Create `pipeline.yml`.
2. Define all 3 jobs with `needs` and `if`.
3. Push to main.
4. Actions tab → should show **Build → Test → Deploy** in sequence.

**Solution:**

```yaml
name: Practical Workflow

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building"

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - run: echo "Testing"

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Deploying"
```

---

<div style="text-align: left;">
  <a href="../../02_secrets_management/01_Secrets_Management.md"><b>Next Day Topic : Secrets Management</b></a>
</div>
