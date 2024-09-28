# Perforce Python Blueprint Node Plugin for Unreal Engine

## Overview

This free plugin provides a foundation for integrating Perforce version control functionality into Unreal Engine projects using Blueprint nodes. It's designed as a starting point for developers to build custom Perforce tools within the Unreal Engine environment.

## Features

- Automatic installation of the p4python library
- Exposed Python source code for customization
- Blueprint node for executing P4 commands
- Functions for syncing and tracking file modifications
- Integration with Unreal Engine's built-in Revision Control system

## Technical Details

- For in-editor use only
- Requires P4 CLI (included with P4V on Windows, separate download for Mac/Linux)

## Installation

### Automatic Installation

1. Install the plugin through the Unreal Engine Marketplace.
2. Enable the plugin in your project's plugin settings.

### Manual Installation

1. Create a directory called `Plugins` inside your UE project directory if it doesn't already exist.
2. Copy the `PerforcePython` folder into the `Plugins` directory.
3. Start Unreal Engine and open your project.
4. Go to Edit > Plugins in the editor.
5. Find the "Perforce Python Blueprint Node" plugin and enable it.

## Usage

To use the pre-made Editor Utility Widgets, navigate to them in the Plugins folder, right click, and choose Run Editor Utility Widget. You can then dock the widget in your editor for easy access.

The plugin allows developers to:

1. Run Perforce commands directly from Blueprints
2. Retrieve information about modified files
3. Sync changes without navigating through the content browser
4. Extend functionality by modifying the provided Python source code

## Documentation

For more information on available commands and usage, refer to:

- [P4 Command Line Reference](https://www.perforce.com/manuals/cmdref/Content/CmdRef/Home-cmdref.html)
- [P4Python Developer Guide](https://www.perforce.com/manuals/p4python/Content/P4Python/Home-p4python.html)

## Support

This plugin is provided as-is and is not officially supported. The developer will do their best to respond to requests, answer questions, and keep it updated. Users are encouraged to modify and extend the plugin to suit their specific needs.

## License

MIT License
