
# =====================================================
# PROJECT: EASY IMAGE EDITOR
# =====================================================
# OBJECTIVE:
# Create a simple image editor using PyQt5.
#
# INSTRUCTIONS:
# Read each instruction and hint carefully.
# Complete the missing code in every section.
# Do not skip any section!
# =====================================================


# PART 1: IMPORT LIBRARIES
# -----------------------------------------------------
# INSTRUCTION:
# Import the os module to work with files and folders.
# Import the necessary widgets from PyQt5.QtWidgets.
#
# HINT:
# You will need:
# QApplication, QWidget, QFileDialog, QLabel,
# QPushButton, QListWidget, QHBoxLayout, QVBoxLayout.


# YOUR CODE HERE:
import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout, QComboBox
)
from PyQt5.QtCore import Qt # needs a Qt.KeepAspectRatio constant to resize while maintaining proportions
from PyQt5.QtGui import QPixmap # screen-optimised

from PIL import Image
from PIL import ImageQt # to import the graphics from Pillow to Qt 
from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)
# PART 2: CREATE THE APPLICATION WINDOW
# -----------------------------------------------------
# INSTRUCTION:
# 1. Create the QApplication object.
# 2. Create the main window using QWidget().
# 3. Set the window size to 700 x 500.
# 4. Set the window title to "Easy Editor".
#
# HINT:
# Use:
# QApplication([])
# QWidget()
# resize(width, height)
# setWindowTitle("title")


# YOUR CODE HERE:
app = QApplication([])
wit = QWidget()
wit.setWindowTitle("Easy Editor")
wit.resize(1100, 750)




# PART 3: CREATE THE WIDGETS
# -----------------------------------------------------
# INSTRUCTION:
# Create all the widgets needed for the application.
#
# HINT:
# 1. Create a QLabel with the text "Image".
# 2. Create a button with the text "Folder".
# 3. Create a QListWidget for displaying filenames.
# 4. Create five editing buttons:
#    - Left
#    - Right
#    - Mirror
#    - Sharpness
#    - B/W
#
# Use QLabel(), QPushButton(), and QListWidget().


# YOUR CODE HERE:
mag = QLabel("Image")
files = QListWidget()
fold = QPushButton("Folder")
edit_menu = QComboBox()
edit_menu.addItem("Choose Edit")
edit_menu.addItem("Left")
edit_menu.addItem("Right")
edit_menu.addItem("Mirror")
edit_menu.addItem("Sharpness")
edit_menu.addItem("B/W")
edit_menu.addItem("Blur")
edit_menu.addItem("Contour")
edit_menu.addItem("Detail")
edit_menu.addItem("Edge_Enhance")
edit_menu.addItem("Edge_Enhance_More")
edit_menu.addItem("Emboss")
edit_menu.addItem("Find_Edges")
edit_menu.addItem("Smooth")
edit_menu.addItem("Smooth_More")


# PART 4: CREATE THE LAYOUTS
# -----------------------------------------------------
# INSTRUCTION:
# Organize the widgets into two columns.
#
# HINT:
# 1. Create one main horizontal layout.
# 2. Create two vertical layouts for the columns.
# 3. Add the Folder button and file list to column 1.
# 4. Add the image label to column 2.
# 5. Create another horizontal layout for editing buttons.
# 6. Add all five editing buttons to this layout.
# 7. Add the editing button layout to column 2.
# 8. Add both columns to the main layout.
# 9. Set the main layout to the window.
#
# USE:
# QHBoxLayout()
# QVBoxLayout()
# addWidget()
# addLayout()
# setLayout()
#
# HINT:
# Use addLayout() when adding one layout inside another.
# Use addWidget() when adding a widget to a layout.


# YOUR CODE HERE:
lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
ver1 = QVBoxLayout()
ver2 = QVBoxLayout()
ver1.addWidget(fold)
ver1.addWidget(files)
ver2.addWidget(mag, 1)
mag.setMinimumSize(500, 500)
mag.setAlignment(Qt.AlignCenter)
lay2.addWidget(edit_menu)
ver2.addLayout(lay2)
lay1.addLayout(ver1)
lay1.addLayout(ver2)


# PART 5: CREATE THE WORKING DIRECTORY VARIABLE
# -----------------------------------------------------
# INSTRUCTION:
# Create a global variable called workdir.
#
# HINT:
# Initialize it as an empty string.


# YOUR CODE HERE:
workdir = ' '


# PART 6: CREATE THE FILTER FUNCTION
# -----------------------------------------------------
# INSTRUCTION:
# Write a function called filter().
# The function must find files with the correct extensions.
#
# SUPPORTED IMAGE EXTENSIONS:
# .jpg, .jpeg, .png, .gif, .bmp
#
# HINT:
# 1. Create an empty list called result.
# 2. Use a for loop to check every filename.
# 3. Use another for loop to check every extension.
# 4. Use endswith() to check the file extension.
# 5. Use append() to add matching filenames.
# 6. Return the result list.
#
# REMEMBER:
# The function receives two parameters:
# files and extensions.


# YOUR CODE HERE:
def filter(files, extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result


# PART 7: CREATE THE CHOOSE WORKING DIRECTORY FUNCTION
# -----------------------------------------------------
# INSTRUCTION:
# Write a function called chooseWorkdir().
# This function allows the user to select a folder.
#
# HINT:
# 1. Use the global keyword to access workdir.
# 2. Use QFileDialog.getExistingDirectory().
# 3. Save the selected folder path in workdir.
#
# REMEMBER:
# You do not need to create a new window.
# QFileDialog will open the folder selection dialog.


# YOUR CODE HERE:
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


# PART 8: DISPLAY THE FILENAMES
# -----------------------------------------------------
# INSTRUCTION:
# Write a function called showFilenamesList().
# This function displays all image filenames
# from the selected folder.
#
# HINT:
# Follow these steps:
#
# 1. Create a list of supported image extensions.
# 2. Call chooseWorkdir() to select a folder.
# 3. Use os.listdir() to get filenames from the folder.
# 4. Use your filter() function to find image files.
# 5. Clear the old filenames from the list widget.
# 6. Use a for loop to display each filename.
# 7. Use lw_files.addItem() to add each filename.
#
# REMEMBER:
# os.listdir(workdir) returns the files and folders
# inside the selected directory.
#
# lw_files.clear() removes old items.
# lw_files.addItem(filename) adds a new item.


# YOUR CODE HERE:
def showFilenamesList():
    extens = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filename = filter(os.listdir(workdir), extens)
    files.clear()
    for file in filename:
        files.addItem(file)
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    def loadImage(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir,filename)
        self.image = Image.open(fullname)
    def showImage(self, path):
        mag.hide()
        pixmapimage = QPixmap(path)
        w, h = mag.width(), mag.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        mag.setPixmap(pixmapimage)
        mag.show()
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
    def do_BW(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_sharp(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_contour(self):
        self.image = self.image.filter(CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_detail(self):
        self.image = self.image.filter(DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_ee(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_eem(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_emboss(self):
        self.image = self.image.filter(EMBOSS)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_fe(self):
        self.image = self.image.filter(FIND_EDGES)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_s(self):
        self.image = self.image.filter(SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_sm(self):
        self.image = self.image.filter(SMOOTH_MORE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
def showChosenImage():
    if files.currentRow() >= 0:
        filename = files.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(os.path.join(workdir, workimage.filename))
def applyEdit(index):
    if index == 1:
        workimage.do_left()
    elif index == 2:
        workimage.do_right()
    elif index == 3:
        workimage.do_mirror()
    elif index == 4:
        workimage.do_sharp()
    elif index == 5:
        workimage.do_BW()
    elif index == 6:
        workimage.do_blur()
    elif index == 7:
        workimage.do_contour()
    elif index == 8:
        workimage.do_detail()
    elif index == 9:
        workimage.do_ee()
    elif index == 10:
        workimage.do_eem()
    elif index == 11:
        workimage.do_emboss()
    elif index == 12:
        workimage.do_fe()
    elif index == 13:
        workimage.do_s()
    elif index == 14:
        workimage.do_sm()
    edit_menu.setCurrentIndex(0)
workimage = ImageProcessor()
files.currentRowChanged.connect(showChosenImage)
# DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
#    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE

# PART 9: CONNECT THE FOLDER BUTTON
# -----------------------------------------------------
# INSTRUCTION:
# Make the Folder button work.
#
# HINT:
# Use the clicked.connect() method.
#
# Connect the Folder button to the function
# showFilenamesList().
#
# REMEMBER:
# Do not write parentheses after the function name
# when connecting a button signal.


# YOUR CODE HERE:
fold.clicked.connect(showFilenamesList)
edit_menu.currentIndexChanged.connect(applyEdit)

# PART 10: SHOW THE WINDOW AND START THE APPLICATION
# -----------------------------------------------------
# INSTRUCTION:
# 1. Display the main window.
# 2. Start the PyQt5 application.
#
# HINT:
# Use:
# win.show()
# app.exec()


# YOUR CODE HERE:
wit.setLayout(lay1)
wit.show()
app.exec_()


# =====================================================
# CHALLENGE: TEST YOUR PROGRAM!
# =====================================================
# 1. Does the window appear correctly?
# 2. Can you click the Folder button?
# 3. Can you select a folder?
# 4. Are image filenames displayed?
# 5. What happens if the folder contains PDF or TXT files?
#
# BONUS CHALLENGE:
# Modify the program so that filenames are displayed
# in alphabetical order.
#
# EXTRA HINT:
# Research the Python sorted() function.
# =====================================================
