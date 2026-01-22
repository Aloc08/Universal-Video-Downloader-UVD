## Adding the UVD to PATH

### Why it's recommended to do so?

Adding the program to your system PATH allows you to run it from any terminal by simply typing `uvd`, without specifying its full path.

### Windows

1. Move the executable to a permanent folder (e.g.: `C:\Program Files\uvd`).
2. Open **Start** and search for **“Environment Variables”**.
3. Click **“Edit the system environment variables”**.
4. In the **Advanced** tab, click **“Environment Variables”**.
5. Under **User variables** or **System variables**, select **`Path`** and click **Edit**.
6. Click **New** and add the folder that contains the executable.
7. Click **OK** to save and restart any open command prompt.

You're set!

### Linux & macOS

1. Move the executable to a directory of your choice (for example: `~/bin` or `/usr/local/bin`).
2. Make sure the file is executable:

   ```bash
   chmod +x uvd
   ```
3. If the directory is not already in your PATH, add it by editing your shell configuration file:

   * **bash**: `~/.bashrc` or `~/.bash_profile`
   * **zsh (default on macOS)**: `~/.zshrc`

   Add the following line:

   ```bash
   export PATH="$PATH:/path/to/your/directory"
   ```
4. Reload the configuration file:

   ```bash
   source ~/.bashrc   # or source ~/.zshrc
   ```



**After completing these steps, you can run the program from any terminal by typing `uvd`.**
