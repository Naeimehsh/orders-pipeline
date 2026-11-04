## A pipeline with several jobs

So far one job does everything. Real pipelines have stages. Here is the picture written as a workflow: **build, then test, then deploy.** You do this in the **playground**, with plain text, so you can focus on the structure.
 
In **`actions-playground`** repository, create a file `.github/workflows/multijob.yml` and save the following in it and before committing it, read through it and then commit it:

```yaml
# A small example of a pipeline: build a package, test, then deploy it.
name: Build, Test, Deploy

# These events start the workflow:
# - push to main: run after a change is pushed to main
# - pull_request targeting main: run while a change is proposed for main
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    # Each job gets its own runner (machine).
    runs-on: ubuntu-24.04
    steps:
      - name: Create a demo package
        # This is a stand-in for a real build. It creates a file we can pass
        # to later jobs so participants can see the artifact move through the pipeline.
        run: |
          mkdir -p package
          echo "demo package, built by run ${{ github.run_number }}" > package/version.txt

      - name: Keep the package for later jobs
        # Upload the folder as an artifact: a file produced by this run
        # that another job can download. Jobs do not share their runner's files automatically.
        uses: actions/upload-artifact@v7
        with:
          name: demo-package
          path: package/

  test:
    runs-on: ubuntu-24.04
    # This job starts only after build succeeds.
    # It runs on a separate runner, so it cannot simply read build's package/ folder.
    needs: build
    steps:
      - run: echo "Testing (a real test job would check out the code and run pytest)"

  deploy:
    runs-on: ubuntu-24.04
    # Deployment waits for tests to succeed.
    needs: test

    # Only deploy from a push to main—not from a pull request.
    # Pull requests can run the build and test jobs without deploying.
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'

    # Associates this job with the GitHub environment named "production".
    # Environment protection rules (if configured) can require approval before it starts.
    environment: production

    # Sets an environment variable for commands in this job.
    env:
      APP_ENV: production

    steps:
      - name: Fetch the package built earlier
        # Download the artifact uploaded by the build job into this job's workspace.
        uses: actions/download-artifact@v8
        with:
          name: demo-package
          path: dist

      - name: Look at what we are about to ship
        # Show the downloaded files and the version marker inside the package.
        run: |
          ls -l dist
          cat dist/version.txt

      - name: Deploy (placeholder_for_actual_project)
        # This only prints a message; it does not deploy anything.
        # A real deployment step would publish the downloaded package to a target system.
        run: echo "A real deployment would go here. Pretending to deploy dist/ to $APP_ENV"
```


**Three details to notice.**

1. **The `build` job makes a "package" and keeps it as an artifact.** This is the idea: build once, keep the artifact, and deploy *that*. Here the package is a text file with the run number in it, so you can see exactly which build you shipped.
2. **The `deploy` job downloads the artifact to `dist` and looks at it** before "deploying". "Check what you ship" is a habit worth naming.
3. **The deploy step is a placeholder.** It only prints a message, to show the *structure* of a pipeline. It is not a real deployment. In real work the artifact is a package or a container image **that includes its dependencies** (which is where Docker and Kubernetes come in), and this step would update a function, publish an image or deploy a DAG. The later topics replace it.

**Predict.**

1. Without `needs`, in what order would the three jobs run?
2. `test` fails. Does `deploy` run?
3. You open a pull request. Does `deploy` run?

<details>
<summary><b>Check yourself</b></summary>

1. At the same time. Jobs run <b>in parallel by default</b>.
2. No. If a job it needs fails, it is <b>skipped</b>.
3. No, it is <b>skipped</b>, because the <code>if</code> requires a <i>push</i> to <code>main</code>. You will see the deploy job shown as skipped (grey) on the pull request.
</details>

**On the `if`.** Many tutorials put `if: github.ref == 'refs/heads/main'` in a workflow that only ever runs on pushes to `main`.  Here the workflow also runs on pull requests check the `on:` at the start of the yaml, where the reference is a pull-request reference rather than `refs/heads/main`, so the `if` visibly **skips** the deploy. That is what makes it testable.

### 1.1 Each job is a separate machine

The `build` job created `package/version.txt`. Can the `deploy` job simply read that file?

<details>
<summary><b>Check yourself</b></summary>
No. Every job gets a <b>fresh machine</b>, so files do not carry over. A real <code>test</code> job would need its <b>own</b> <code>checkout</code> and its own Python setup.
</details>

To pass a file from one job to another you **upload it as an artifact** and **download it** later. This also solves part of P4 and P6: you build the package **once** and deploy **that exact package**, rather than rebuilding it differently at deploy time. "Build once, deploy that" is a core delivery habit. In this demo the "package" is just a text file. In real projects it is a package or a container image that includes its dependencies: that is where Docker and Kubernetes come in.

### 1.2 Environment variables at three levels

```yaml
name: Variables at three levels

on: push

env:
  APP_ENV: development          # workflow level: every job sees it

jobs:
  example:
    runs-on: ubuntu-24.04
    env:
      STAGE: test               # job level: every step in this job sees it
    steps:
      - name: Show them
        env:
          STEP_ONLY: "only this step"   # step level: only this step sees it
        run: echo "$APP_ENV / $STAGE / $STEP_ONLY"
      - name: Next step
        run: echo "STEP_ONLY here is '$STEP_ONLY' (empty)"
```

The innermost level wins when names clash. And note the two syntaxes: `$VAR` is read by the **shell** when the step runs, while `${{ ... }}` is replaced by **GitHub** before the step runs.

### 1.3 Environments: a preview of approvals

Notice `environment: production` on the deploy job. An **environment** is a named place you deploy to. You can attach rules to it, for example **required reviewers**, so the job pauses until a human approves. That is the "continuous delivery" approval step from the discussion. Environments can also hold their own **secrets**, so the production key is only visible to production jobs. The next topics use exactly this.
