# -*- coding: utf-8 -*-

"""
QTabWidget Style Examples
This file demonstrates how to customize various style effects of the QTabWidget control in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QTextEdit,
    QGroupBox
)
from PySide6.QtGui import QFont, QIcon

class TabWidgetStylesWindow(QMainWindow):
    """QTabWidget style example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTabWidget Style Examples")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QTabWidget Style Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select Tab Style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Tabs", 
            "Modern Style Tabs", 
            "Rounded Tabs",
            "Underlined Tabs",
            "Colored Tabs",
            "Dark Theme Tabs",
            "Vertical Tabs",
            "Custom Tabs"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_tab_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset Tabs")
        self.reset_button.clicked.connect(self.reset_tab)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create tab container
        self.tab_container = QWidget()
        self.tab_layout = QVBoxLayout(self.tab_container)
        self.main_layout.addWidget(self.tab_container)
        
        # Create tab widget
        self.create_tabwidget()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic tabs by default
        self.update_tab_style(0)
    
    def create_tabwidget(self):
        """Create tab widget and add tab pages"""
        # Create tab widget
        self.tab_widget = QTabWidget()
        
        # Create multiple tab pages
        self.create_tab("Basic Info", "This is the content of the Basic Info tab.")
        self.create_tab("Detailed Settings", "This is the content of the Detailed Settings tab.")
        self.create_tab("Advanced Options", "This is the content of the Advanced Options tab.")
        self.create_tab("Help Documentation", "This is the content of the Help Documentation tab.")
        
        # Add tab widget to layout
        self.tab_layout.addWidget(self.tab_widget)
    
    def create_tab(self, title, content_text):
        """Create a single tab page"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Add content text box
        content = QTextEdit()
        content.setPlainText(content_text)
        content.setReadOnly(True)
        content.setStyleSheet("background-color: #F8F9FA; border: none; padding: 10px;")
        
        # Add some controls as examples
        group = QGroupBox("Example Controls")
        group_layout = QVBoxLayout(group)
        
        label1 = QLabel("This is a label example")
        label2 = QLabel("Another label example")
        
        group_layout.addWidget(label1)
        group_layout.addWidget(label2)
        
        # Add controls to tab page layout
        layout.addWidget(content)
        layout.addWidget(group)
        
        # Add tab page to tab widget
        self.tab_widget.addTab(tab, title)
    
    def update_tab_style(self, index):
        """Update tab style based on selection"""
        # Clear previous styles
        self.tab_widget.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #CCCCCC;
                    background-color: white;
                }
                QTabBar::tab {
                    background-color: #F0F0F0;
                    color: #333333;
                    padding: 8px 16px;
                    border: 1px solid #CCCCCC;
                    border-bottom: none;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Basic Tab Style: Uses simple borders and background colors to provide clear visual hierarchy.")
        
        elif index == 1:
            # Modern style tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 4px;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 10px 20px;
                    margin-right: 2px;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    color: #2196F3;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Modern Style Tabs: Uses rounded corners and larger padding for a more modern appearance.")
        
        elif index == 2:
            # Rounded tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 8px;
                    margin-top: 4px;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 10px 20px;
                    margin-right: 4px;
                    border-radius: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: #4CAF50;
                    color: white;
                    border-color: #4CAF50;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Rounded Tabs: All tabs use rounded corners design, and selected tabs are highlighted with contrasting colors.")
        
        elif index == 3:
            # Underlined tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: none;
                    background-color: white;
                    border-bottom: 1px solid #E0E0E0;
                }
                QTabBar::tab {
                    background-color: transparent;
                    color: #666666;
                    padding: 12px 20px;
                    margin-right: 4px;
                }
                QTabBar::tab:hover {
                    color: #2196F3;
                }
                QTabBar::tab:selected {
                    color: #2196F3;
                    font-weight: bold;
                }
                QTabBar::tab:selected::after {
                    content: '';
                    background-color: #2196F3;
                    height: 3px;
                    width: 100%;
                    position: absolute;
                    bottom: 0;
                    left: 0;
                }
            """)
            self.info_label.setText("Underlined Tabs: Uses simple underlines to identify selected tabs, providing a minimalist design.")
        
        elif index == 4:
            # Colored tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 4px;
                }
                QTabBar::tab {
                    color: white;
                    padding: 10px 20px;
                    margin-right: 4px;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                }
                QTabBar::tab:nth-child(1) {
                    background-color: #F44336;
                }
                QTabBar::tab:nth-child(2) {
                    background-color: #2196F3;
                }
                QTabBar::tab:nth-child(3) {
                    background-color: #4CAF50;
                }
                QTabBar::tab:nth-child(4) {
                    background-color: #FF9800;
                }
                QTabBar::tab:hover {
                    opacity: 0.8;
                }
                QTabBar::tab:selected {
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Colored Tabs: Each tab uses a different color, creating a colorful interface effect.")
        
        elif index == 5:
            # Dark theme tab style
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #444444;
                    background-color: #2C2C2C;
                    color: white;
                }
                QTabBar::tab {
                    background-color: #3C3C3C;
                    color: #BBBBBB;
                    padding: 10px 20px;
                    margin-right: 2px;
                    border: 1px solid #444444;
                    border-bottom: none;
                }
                QTabBar::tab:hover {
                    background-color: #444444;
                    color: #FFFFFF;
                }
                QTabBar::tab:selected {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Dark Theme Tabs: Uses dark background and high-contrast text colors, suitable for night use.")
        
        elif index == 6:
            # Vertical tab style
            # Set tab position to left
            self.tab_widget.setTabPosition(QTabWidget.West)
            
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 12px 16px;
                    margin-bottom: 2px;
                    min-width: 80px;
                    height: 60px;
                    border-right: 1px solid #E0E0E0;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    color: #2196F3;
                    border-right: none;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Vertical Tabs: Tabs arranged on the left, suitable for tab names with longer content.")
        
        elif index == 7:
            # Custom tab style
            # Restore tab position to top
            self.tab_widget.setTabPosition(QTabWidget.North)
            
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 2px solid #9C27B0;
                    background-color: #F5F5F5;
                    border-radius: 8px;
                    margin-top: 4px;
                }
                QTabBar::tab {
                    background-color: white;
                    color: #9C27B0;
                    padding: 10px 20px;
                    margin-right: 8px;
                    border-radius: 20px;
                    border: 2px solid #9C27B0;
                }
                QTabBar::tab:hover {
                    background-color: #F3E5F5;
                }
                QTabBar::tab:selected {
                    background-color: #9C27B0;
                    color: white;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Custom Tabs: Uses unique circular design and color combinations to create personalized tab styles.")
    
    def reset_tab(self):
        """Reset tab style"""
        # Recreate tab widget
        while self.tab_layout.count() > 0:
            item = self.tab_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Recreate tab widget
        self.create_tabwidget()
        
        # Reset style selector
        self.style_combobox.setCurrentIndex(0)
        self.update_tab_style(0)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())