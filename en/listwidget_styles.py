#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
QListWidget Style Sheet Example
This file demonstrates how to customize various style effects for the QListWidget widget in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QGroupBox
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class ListWidgetStylesWindow(QMainWindow):
    """QListWidget stylesheet example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QListWidget Style Sheet Example")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QListWidget Style Sheet Example")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select list style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic List", 
            "Card List", 
            "Horizontal List",
            "Icon List",
            "Colored Items List",
            "Dark Theme List",
            "Checkbox List",
            "Custom Separator List"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_list_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset List")
        self.reset_button.clicked.connect(self.reset_list)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create list container
        self.list_container = QWidget()
        self.list_layout = QVBoxLayout(self.list_container)
        self.main_layout.addWidget(self.list_container)
        
        # Create list widget
        self.create_listwidget()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic list by default
        self.update_list_style(0)
    
    def create_listwidget(self):
        """Create list widget and add items"""
        # Create list widget
        self.list_widget = QListWidget()
        
        # Add list items
        items = [
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
            "Item 6",
            "Item 7",
            "Item 8",
            "Item 9",
            "Item 10"
        ]
        
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setTextAlignment(Qt.AlignVCenter)
            self.list_widget.addItem(item)
        
        # Add list widget to layout
        self.list_layout.addWidget(self.list_widget)
    
    def update_list_style(self, index):
        """Update list style based on selection"""
        # Clear previous styles
        self.list_widget.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic list style
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 8px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #CCE8FF;
                    color: #000000;
                }
                QListWidget::item:hover {
                    background-color: #F5F5F5;
                }
            """)
            self.info_label.setText("Basic list style: Uses simple borders and background colors, providing clear visual hierarchy.")
        
        elif index == 1:
            # Card list style
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #F5F5F5;
                    border: none;
                    font-size: 14px;
                }
                QListWidget::item {
                    background-color: white;
                    padding: 12px;
                    margin: 8px;
                    border-radius: 8px;
                    border: 1px solid #E0E0E0;
                }
                QListWidget::item:selected {
                    background-color: #E3F2FD;
                    border-color: #2196F3;
                    color: #2196F3;
                    font-weight: bold;
                }
                QListWidget::item:hover {
                    border-color: #90CAF9;
                }
            """)
            self.info_label.setText("Card list style: Each item is an independent card with rounded corners and shadow effects.")
        
        elif index == 2:
            # Horizontal list style
            # Set list to horizontal scrolling
            self.list_widget.setFlow(QListWidget.LeftToRight)
            self.list_widget.setWrapping(True)
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #FAFAFA;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    background-color: white;
                    padding: 10px 20px;
                    margin: 8px;
                    border-radius: 20px;
                    border: 1px solid #E0E0E0;
                    min-width: 100px;
                    height: 40px;
                    text-align: center;
                }
                QListWidget::item:selected {
                    background-color: #4CAF50;
                    color: white;
                    border-color: #4CAF50;
                }
                QListWidget::item:hover {
                    border-color: #4CAF50;
                }
            """)
            self.info_label.setText("Horizontal list style: List items are arranged horizontally with circular button styles, suitable for category tags.")
        
        elif index == 3:
            # Icon list style
            # Reset list to vertical scrolling
            self.list_widget.setFlow(QListWidget.TopToBottom)
            self.list_widget.setWrapping(False)
            
            # Recreate list items with icons
            self.reset_list()
            
            # Add icons to each item
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                # Use different colored squares as icons (can be replaced with real icons in actual use)
                colors = ["#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", 
                          "#2196F3", "#03A9F4", "#00BCD4", "#009688", "#4CAF50"]
                color = colors[i % len(colors)]
                # Create simple icon style
                item.setText(f"<span style='color:{color}; font-weight:bold'>●</span> {item.text()}")
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px 16px;
                    border-bottom: 1px solid #F5F5F5;
                }
                QListWidget::item:selected {
                    background-color: #F5F5F5;
                    color: #2196F3;
                }
                QListWidget::item:hover {
                    background-color: #FAFAFA;
                }
            """)
            self.info_label.setText("Icon list style: Each list item has an icon to enhance visual recognition.")
        
        elif index == 4:
            # Colored items list style
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #FFFFFF;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 12px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #E0E0E0;
                    color: #000000;
                }
                QListWidget::item:nth-child(even) {
                    background-color: #F9F9F9;
                }
                QListWidget::item:nth-child(3n) {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
            """)
            self.info_label.setText("Colored items list style: Uses nth-child selectors to set different background colors for different rows.")
        
        elif index == 5:
            # Dark theme list style
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    border: 1px solid #444444;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #444444;
                }
                QListWidget::item:selected {
                    background-color: #3F51B5;
                    color: #FFFFFF;
                }
                QListWidget::item:hover {
                    background-color: #3C3C3C;
                }
            """)
            self.info_label.setText("Dark theme list style: Uses dark background and high-contrast text colors, suitable for night use.")
        
        elif index == 6:
            # Checkbox list style
            # Recreate list and add checkboxes
            self.reset_list()
            
            # Add checkbox styles to each item
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                # Add checkbox symbol
                item.setText(f"□ {item.text()}")
            
            # Connect signal to toggle checkbox state when clicked
            self.list_widget.itemClicked.connect(self.toggle_checkbox)
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #F5F5F5;
                    color: #000000;
                }
            """)
            self.info_label.setText("Checkbox list style: Each list item has a checkable checkbox, suitable for multiple selection operations.")
        
        elif index == 7:
            # Custom separator list style
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #E0E0E0;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 12px 16px;
                    border-bottom: 2px dotted #E0E0E0;
                }
                QListWidget::item:selected {
                    background-color: #FFF8E1;
                    color: #FFA000;
                    font-weight: bold;
                }
                QListWidget::item:hover {
                    background-color: #FAFAFA;
                }
            """)
            self.info_label.setText("Custom separator list style: Uses dotted lines to separate rows, creating a unique visual style.")
    
    def toggle_checkbox(self, item):
        """Toggle checkbox state"""
        text = item.text()
        if text.startswith("□"):
            # Checked state
            item.setText(text.replace("□", "☑"))
        else:
            # Unchecked state
            item.setText(text.replace("☑", "□"))
    
    def reset_list(self):
        """Reset list data and style"""
        # Clear the list
        self.list_widget.clear()
        
        # Re-add items
        items = [
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
            "Item 6",
            "Item 7",
            "Item 8",
            "Item 9",
            "Item 10"
        ]
        
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setTextAlignment(Qt.AlignVCenter)
            self.list_widget.addItem(item)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())