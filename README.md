# petstore-api-automation-python
A Python-based API automation framework for Swagger Petstore demonstrating best practices with Pytest, Requests, fixtures, and CI integration.

## Prerequisites

### Python 3.12.3 Installation

This project requires Python 3.12.3. We recommend using pyenv to manage Python versions.

#### Installing pyenv

**Windows:**
1. Install pyenv-win using Git Bash or PowerShell:
   ```bash
   git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv
   ```
2. Add pyenv to your PATH. You have two options:

   **Option A: Using PowerShell (Recommended)**
   Run these commands in PowerShell as Administrator:
   ```powershell
   [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
   [System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
   [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
   [System.Environment]::SetEnvironmentVariable('PATH',$env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + $env:PATH,"User")
   ```

   **Option B: Using System Properties (GUI)**
   1. Press `Win + R`, type `sysdm.cpl`, and press Enter
   2. Click "Environment Variables"
   3. Under "User variables", click "New" and add these variables:
      - Variable name: `PYENV`, Value: `%USERPROFILE%\.pyenv\pyenv-win\`
      - Variable name: `PYENV_ROOT`, Value: `%USERPROFILE%\.pyenv\pyenv-win\`
      - Variable name: `PYENV_HOME`, Value: `%USERPROFILE%\.pyenv\pyenv-win\`
   4. Find the `PATH` variable, click "Edit", and add these two paths:
      - `%USERPROFILE%\.pyenv\pyenv-win\bin`
      - `%USERPROFILE%\.pyenv\pyenv-win\shims`
3. Restart your terminal or run:
   ```bash
   refreshenv
   ```

**macOS:**
1. Install pyenv using Homebrew:
   ```bash
   brew install pyenv
   ```
2. Add pyenv to your shell profile (~/.zshrc or ~/.bash_profile):
   ```bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
3. Restart your terminal or run:
   ```bash
   source ~/.zshrc
   ```

#### Installing Python 3.12.3

After installing pyenv, install Python 3.12.3:

```bash
pyenv install 3.12.3
pyenv global 3.12.3
```

### Create virtual environment and name ".venv":

**Windows:**
```cmd
python -m venv .venv
```

**macOS:**
```bash
python3 -m venv .venv
```

### Activate your ".venv" virtual environment:

**Windows:**
```cmd
.venv\Scripts\activate
```

**macOS:**
```bash
source .venv/bin/activate
```

### Install needed python libraries:
```bash
pip install -r requirements.txt
```

### Create environment configuration file:

Create a `.env` file in the root directory with the following content:

```env
PETSTORE_API_BASEURL=https://petstore3.swagger.io/api
PETSTORE_API_VERSION=v3
```

**Note:** The `.env` file is required for the API client to function properly. Make sure to create this file before running tests.