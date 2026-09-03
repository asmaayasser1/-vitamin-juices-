# Vitamin Juices — Python Tkinter GUI

## Project Overview

Vitamin Juices is an academic Python desktop application that demonstrates foundational event-driven GUI programming with Tkinter.

The project presents a simple custom juice-order interface where users can enter a juice base, supplement, and drink size. It demonstrates window management, form input, validation, button callbacks, message-box feedback, and local image handling.

## Application Workflow

The primary application is designed around two windows:

1. The main window displays a logo, welcome message, and navigation buttons.
2. Selecting **Create Your Juice** hides the main window and opens the order window.
3. The user enters a juice base.
4. The user enters a supplement.
5. The user enters a drink size.
6. Selecting **Submit Order** verifies that none of the three fields is empty.
7. Valid entries are displayed in a confirmation dialog.
8. The user can clear the fields or return to the main menu.

The **View Previous Orders** button is currently a placeholder. It displays a message stating that no previous orders are available, and submitted orders are not stored.

## GUI Features

- Tkinter root window
- Secondary `Toplevel` window
- Frames and labels
- Free-form entry fields
- Buttons with callback functions
- `StringVar` input state
- `messagebox` error and confirmation feedback
- Clear/reset actions
- Window navigation with `withdraw()` and `deiconify()`
- Local image loading with `PhotoImage`
- Class-based application structure
- Standard `__main__` entry point

## Technology Stack

- Python 3
- Tkinter
- Python standard library

No third-party Python packages are used by the current source code.

## Project Structure

```text
.
├── AliAsmaaFinalProject.py
├── vitamin_juices extended .py
├── Juice..jpg
├── juiceHealthydrink.jpg
├── logo Juice.png
└── README.md
```

### `AliAsmaaFinalProject.py`

This is the primary application. It contains the complete Tkinter class, both application windows, widget definitions, navigation callbacks, input handling, message boxes, and application event loop.

### `vitamin_juices extended .py`

This file contains a small experimental or alternate `submit_order()` method. It adds numeric size validation and clears selections after a successful submission.

The file is not integrated into the primary application and cannot run independently because it does not contain the surrounding class, imports, widgets, or event loop.

### Image Assets

- `logo Juice.png` is referenced by the primary application and assigned to the visible logo label.
- `Juice..jpg` and `juiceHealthydrink.jpg` are exact duplicate image files.
- The two JPEG files are not referenced by the current Python code.
- `fruit.png` is referenced by the primary application but is missing from the repository.
- The loaded `fruit.png` image is not assigned to a visible widget in the current implementation.

## Getting Started

### Prerequisites

You will need:

- Python 3 with Tkinter support
- A graphical desktop environment

Tkinter is included with many standard Python installations, although its availability can vary by operating system and Python distribution.

### Clone the Repository

```bash
git clone https://github.com/asmaayasser1/-vitamin-juices-.git
cd ./-vitamin-juices-
```

### Run the Application

```bash
python AliAsmaaFinalProject.py
```

### Current Missing-Asset Limitation

The committed application references:

```text
fruit.png
```

That file is not currently included in the repository. Because Tkinter attempts to load it during application initialization, the clean-clone version may fail before the GUI fully starts.

This documentation describes the repository as it currently exists; the missing image reference has not been changed or replaced.

## Data and Storage

User entries exist only in memory while the application is running.

The current project does not use:

- A database
- File-based order storage
- Persistent order history
- Network communication
- External APIs

Submitting an order displays the entered values in a message box but does not save them. The **View Previous Orders** action therefore remains a placeholder.

## Input Handling

The primary application checks whether the juice base, supplement, and size fields contain values. If any field is empty, it displays an error message.

The primary application does not currently validate:

- Whether the size is numeric
- Whether the entered juice or supplement is an available product
- Quantities
- Prices
- Order totals

The separate experimental Python file contains numeric size validation, but that method is not integrated into the primary application.

## Current Limitations

- `fruit.png` is referenced but missing
- The clean-clone application may fail during image initialization
- Submitted orders are not persisted
- **View Previous Orders** is a placeholder
- Juice base, supplement, and size are free-form text inputs
- No predefined product catalog is included
- No quantities, prices, or totals are calculated
- The secondary Python method is not integrated
- Two unused JPEG files are exact duplicates
- No automated tests are included
- No packaging or deployment configuration is provided

## Team / Academic Context

The primary source file identifies this repository as an academic Module 08 final project and preserves its original author attribution.

This portfolio documentation describes the verified repository behavior without making broader claims about contribution scope or production readiness.

## Project Status

Academic Tkinter GUI project being refined for professional portfolio presentation.
