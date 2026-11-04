# Understanding the YAML Structure in GitHub Actions

Every GitHub Actions workflow is written in **YAML** (YAML Ain’t Markup Language).
YAML is a simple, human-readable way to define configuration.

---

##  Core Workflow Structure

```yaml
name: Workflow Name

on: 
  push:
    branches: [ main ]

jobs:
  job_id:
    runs-on: ubuntu-latest
    steps:
      - name: Step name
        run: command OR
        uses: action-name
```

---

##  Breakdown of Each Section

### 1. `name`

* Optional, for readability.
* Appears in the **GitHub Actions tab**.

```yaml
name: CI Pipeline
```

---

### 2. `on` (Triggers)

* Defines **when** a workflow runs.

Examples:

```yaml
on:
  push:
    branches: [ main ]
```

```yaml
on:
  pull_request:
    branches: [ main ]
```

```yaml
on: workflow_dispatch  # manual trigger
```

---

### 3. `jobs`

* A workflow consists of **jobs**.
* Each job runs in its own **isolated virtual machine (runner)**.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

---

### 4. `runs-on` (Runner Environment)

* Defines the **OS environment** for the job.
* Common options:

  * `ubuntu-latest`
  * `windows-latest`
  * `macos-latest`

---

### 5. `steps`

* A job has **steps**, which run sequentially.
* Steps can either:

  * Run shell commands (`run`)
  * Use pre-built actions (`uses`)

Example:

```yaml
steps:
  - name: Checkout repository
    uses: actions/checkout@v4

  - name: Print a message
    run: echo "Hello from YAML!"
```

---

##  Practical Enhancements in YAML

### 1. Multiple Jobs in One Workflow

Workflows can define multiple jobs that run in **parallel by default**.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building the app"

  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running tests"
```

---

### 2. Job Dependencies (`needs`)

Jobs can be run **in sequence** using `needs`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building app"

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - run: echo "Running tests after build"
```

---

### 3. Environment Variables (`env`)

You can define variables at different levels:

* **Workflow-level** (shared across all jobs)
* **Job-level**
* **Step-level**

```yaml
env:
  APP_ENV: development

jobs:
  example:
    runs-on: ubuntu-latest
    env:
      JOB_VAR: "job scope"
    steps:
      - name: Print environment variables
        run: echo "Env = $APP_ENV, Job = $JOB_VAR"
```

---

### 4. Conditionals (`if`)

Run steps only when conditions are met.

```yaml
steps:
  - name: Deploy only on main
    if: github.ref == 'refs/heads/main'
    run: echo "Deploying to production"
```

---

##  Example: Practical Workflow

```yaml
name: CI Workflow

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Build
        run: echo "Building project"

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Run tests
        run: echo "Running tests"

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy
        run: echo "Deploying app..."
```

---

## Key Takeaways

* **Core Concepts** → `name`, `on`, `jobs`, `runs-on`, `steps`
* **Practical Enhancements** → Multiple jobs, job dependencies, environment variables, conditionals

---

<div style="text-align: left;">
  <a href="./excerise/01_Activity_Github_Actions.md"><b> Day 1: Exercises</b></a>
</div>
