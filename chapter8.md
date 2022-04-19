# Chapter 8: Graphical User Interface

GUI displays all information graphically to its users and allows them to manipulate it

GUI programs are event-driven: inactive until the user acts

Terminal-based programs: must reply to each prompt as it appears, no way to go back; to obtain different results, the entire program must be run again

GUI-based: includes a title bar, labels along the left side of the window, corresponding to entry fields along the right side; command button that calculates the result into the output field. The user can enter inputs in any order and change previous inputs, can run different data sets without re-entering all data

When the calculate button is pressed, a method call is triggered and retrieves all the values from the input fields for the calculation

Coding phase:
1. define a new class for the application window
2. instantiate the classes of window components
3. position the components in a window
4. register a method with each window component
5. define the methods to handle events
6. define a main function to instantiate the window class and launch the GUI

Use breezypythongui

class names are capitalized by convention in python

Method headers always include (self) as the first parameter

New classes that are subclasses of another class inherit attributes and behavior defined by parent and ancestor classes

## 8.3 Windows and Window Accessories

Window attributes:
* Title (empty string by default)
* Width and height (in pixels)
* resizability (true by default)
* Background color (white by default)

Components are laid out in a 2-D grid, (0, 0) in upper left
Components can be resized to span multiple rows or columns