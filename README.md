# SimpleDockerManager


This script creates a GUI application using tkinter to install and manage Medusa and Lidarr Docker containers. The application consists of three tabs: General, Medusa, and Lidarr. Users can select which application they want to install using checkboxes on the General tab. After making their selections, users can click the "Install Selected" button to install the chosen applications.

The script defines several functions for managing Medusa and Lidarr containers, such as install, start, stop, delete, and update. These functions use the subprocess module to run Docker commands that manage the containers.

The Application class creates the main GUI window, the tabs, and their contents. The create_widgets method sets up the user interface for each tab. For example, it creates checkboxes for installing Medusa and Lidarr on the General tab, and it creates labels for the Medusa and Lidarr tabs. The code also defines the install_selected method for the Application class, which is called when the "Install Selected" button is clicked. However, the method is not yet implemented.

To make the script functional, you need to add the widgets for Medusa and Lidarr settings, and implement the install_selected method by calling the respective install_medusa and install_lidarr functions with the required parameters.

Also, notice that the install_selected function is defined twice, once as a standalone function and then as a method in the Application class. You should remove the standalone function and keep the method in the Application class.

When the application is complete, users will be able to install and manage Medusa and Lidarr Docker containers easily through the GUI.
