This repository contains a Conky configuration that integrates with the `gcalendar` pip package, allowing you to display upcoming Google Calendar events on your desktop using Conky. 

Follow the steps below to set up and customize this configuration for your system.

## Prerequisites

Before installing and using this Conky configuration, make sure you have the following prerequisites installed on your system:

1. [pipx](https://pipx.pypa.io/stable/installation/) - A tool to install and run Python applications in isolated environments.

## Installation

1.**Install pipx:**

You can visit the pix link above if your system is not debian based.

   ```bash
   sudo apt-get install pipx
   ```

2.**Install gcalendar:**

   ```bash
   pipx install gcalendar
   ```

3.**Ensure pipx is in your PATH:**

   ```bash
   pipx ensurepath
   ```

4.**Enable pipx command completions:**

   ```bash
   pipx completions
   ```

5.**Verify pipx installation:**

   ```bash
   pipx
   ```

## Configuration

1. **Authenticate with Google Calendar:**

   Run the following command in the terminal:

   ```bash
   gcalendar
   ```

   This will open a browser window where you can authenticate and grant access to your Google Calendar.

2. **Copy Conky Configuration:**

   Copy the `gcalendar-conky-config` file to your Conky configuration path. For example, if your Conky configuration is stored in `~/.config/conky/`:

   ```bash
   cp gcalendar-conky-config/* ~/.config/conky/
   ```

3. **Edit Conky Configuration:**

   Modify the `~/.config/conky/gcalendar-conky-config` file to suit your preferences. You may customize the appearance, colors, and update intervals according to your liking.

4. **Start Conky:**

   Run Conky with the chosen configuration:

   ```bash
   conky -c ~/.config/conky/gcalendar-conky-config
   ```

   The Conky widget should now display your upcoming Google Calendar events on your desktop.

## Notes

- Ensure that Conky is properly configured and running on your system.
- Make sure to run Conky with the specified configuration file path.

Feel free to explore and modify the Conky configuration to match your desktop environment and personal preferences. Enjoy having your Google Calendar events conveniently displayed on your desktop.
