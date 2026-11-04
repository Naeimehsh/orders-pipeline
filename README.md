
## Prerequisites

* An **AWS account** with the necessary permissions.
* A **Snowflake account** (for database integration later).
* A **GitHub account** (where we’ll store the Terraform code and enable CI/CD).

If you don’t already have a GitHub account, [create one here](https://github.com/join) before moving to the next steps.

---

## Step 1: Install GitHub CLI (`gh`)

The **GitHub CLI** makes it easy to create and manage repositories directly from your terminal.

**Linux (Debian/Ubuntu):**

```bash
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
  sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) \
signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
https://cli.github.com/packages stable main" | \
  sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

sudo apt update
sudo apt install gh -y
```

**macOS (with Homebrew):**

```bash
brew install gh
```

**Windows (with Winget):**

```powershell
winget install --id GitHub.cli
```

---

## Step 2: Authenticate with GitHub

```bash
gh auth login
```

* Choose **GitHub.com**
* Select **HTTPS** (or SSH if you’ve set up keys)
* Follow the browser login prompt

---

## Step 3: Initialize your local repo

```bash
cd project-example   # go to your project folder
git init
git add .
git commit -m "Initial commit"
```

---

## Step 4: Create GitHub repo + push in one shot

```bash
gh repo create project-example --private --source=. --remote=origin --push
```

---

Done!

* A new repository named **project-example** is created on GitHub.
* Your local code and workflows are pushed automatically.
* GitHub Actions (`.github/workflows/sample-ci.yml`) will start running.

---

<div style="text-align: left;">
  <a href="./01_intro_cicd.md"><b>Let's Begin : Introduction to CI/CD</b></a>
</div>

---



