# -*- coding: utf-8 -*-

"""
QTableWidget Style Sheet Examples
This file demonstrates how to customize various style effects for the QTableWidget widget in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QGroupBox
)
from PySide6.QtGui import QFont, QBrush, QColor

class TableWidgetStylesWindow(QMainWindow):
    """QTableWidget Style Sheet Example Window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableWidget Style Sheet Examples")
        self.resize(900, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QTableWidget Style Sheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select table style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Table", 
            "Zebra Striped Table", 
            "Modern Style Table",
            "Dark Theme Table",
            "Cell Highlight Table",
            "Borderless Table",
            "Custom Grid Table",
            "Complex Style Table"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_table_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset Table")
        self.reset_button.clicked.connect(self.reset_table)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create table container
        self.table_container = QWidget()
        self.table_layout = QVBoxLayout(self.table_container)
        self.main_layout.addWidget(self.table_container)
        
        # Create table
        self.create_table()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic table by default
        self.update_table_style(0)
    
    def create_table(self):
        """Create table and populate with sample data"""
        # Create table widget
        self.table_widget = QTableWidget(5, 4)
        
        # Set header
        headers = ["Product Name", "Price", "Stock", "Status"]
        self.table_widget.setHorizontalHeaderLabels(headers)
        
        # Populate with sample data
        data = [
            ["Laptop", "¥6,999", "12", "In Stock"],
            ["Smartphone", "¥3,999", "50", "In Stock"],
            ["Tablet", "¥2,499", "0", "Out of Stock"],
            ["Smartwatch", "¥1,299", "28", "In Stock"],
            ["Wireless Headphones", "¥899", "45", "In Stock"]
        ]
        
        for row in range(5):
            for col in range(4):
                item = QTableWidgetItem(data[row][col])
                item.setTextAlignment(Qt.AlignCenter)
                
                # Set special style for stock status
                if col == 3:
                    if data[row][col] == "Out of Stock":
                        item.setForeground(QBrush(QColor(255, 0, 0)))
                    else:
                        item.setForeground(QBrush(QColor(0, 150, 0)))
                
                self.table_widget.setItem(row, col, item)
        
        # Auto adjust column widths
        self.table_widget.horizontalHeader().setSectionResizeMode(0, self.table_widget.horizontalHeader().Stretch)
        for i in range(1, 4):
            self.table_widget.horizontalHeader().setSectionResizeMode(i, self.table_widget.horizontalHeader().ResizeToContents)
        
        # Add table to layout
        self.table_layout.addWidget(self.table_widget)
    
    def update_table_style(self, index):
        """Update table style based on selection"""
        # Clear previous styles
        self.table_widget.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #DDDDDD;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #DDDDDD;
                }
                QHeaderView::section {
                    background-color: #F5F5F5;
                    padding: 8px;
                    border: 1px solid #DDDDDD;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Basic Table Style: Uses simple borders and background colors to provide clear visual hierarchy.")
        
        elif index == 1:
            # Zebra striped table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #E0E0E0;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTableWidget::item:selected {
                    background-color: #CCE8FF;
                    color: #000000;
                }
                QTableWidget::item:alternate {
                    background-color: #F9F9F9;
                }
                QHeaderView::section {
                    background-color: #4285F4;
                    color: white;
                    padding: 8px;
                    border: 1px solid #4285F4;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Zebra Striped Table Style: Uses alternate selector to create row alternating color effect, improving readability.")
        
        elif index == 2:
            # Modern style table
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #FFFFFF;
                    border: 1px solid #E0E0E0;
                    border-radius: 4px;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #F0F0F0;
                }
                QTableWidget::item:selected {
                    background-color: #2196F3;
                    color: white;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                }
                QHeaderView::section {
                    background-color: #F5F5F5;
                    color: #333333;
                    padding: 10px;
                    border: none;
                    border-bottom: 2px solid #E0E0E0;
                    font-weight: bold;
                    font-size: 15px;
                }
            """)
            self.info_label.setText("Modern Style Table: Uses rounded borders, simple bottom lines and hover effects to provide a modern UI experience.")
        
        elif index == 3:
            # Dark theme table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    gridline-color: #444444;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #444444;
                }
                QTableWidget::item:selected {
                    background-color: #3F51B5;
                    color: #FFFFFF;
                }
                QHeaderView::section {
                    background-color: #1A1A1A;
                    color: #FFFFFF;
                    padding: 8px;
                    border: 1px solid #444444;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Dark Theme Table: Uses dark background and high contrast text colors, suitable for night use.")
        
        elif index == 4:
            # Cell highlight table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #E0E0E0;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTableWidget::item:nth-child(4n+3) {
                    background-color: #FFF9C4;
                }
                QTableWidget::item:selected {
                    background-color: #FFCDD2;
                    color: #C62828;
                    font-weight: bold;
                }
                QHeaderView::section {
                    background-color: #81C784;
                    color: white;
                    padding: 8px;
                    border: 1px solid #66BB6A;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Cell Highlight Table Style: Uses nth-child selector to highlight specific rows and adds special style for selected items.")
        
        elif index == 5:
            # Borderless table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    border: none;
                    gridline-color: transparent;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 10px;
                    border: none;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                    border-radius: 4px;
                }
                QTableWidget::item:selected {
                    background-color: #E3F2FD;
                    border-radius: 4px;
                    color: #1565C0;
                }
                QHeaderView::section {
                    background-color: transparent;
                    color: #424242;
                    padding: 10px;
                    border: none;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("Borderless Table Style: Removes all borders, uses subtle hover effects and rounded selected states to create a clean appearance.")
        
        elif index == 6:
            # Custom grid table style
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #FAFAFA;
                    border: 2px solid #E0E0E0;
                    border-radius: 8px;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: none;
                    border-bottom: 1px dashed #E0E0E0;
                }
                QTableWidget::item:last-row {
                    border-bottom: none;
                }
                QTableWidget::item:selected {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
                QHeaderView::section {
                    background-color: #FAFAFA;
                    color: #333333;
                    padding: 10px;
                    border: none;
                    border-right: 1px solid #E0E0E0;
                    font-weight: bold;
                }
                QHeaderView::section:last-column {
                    border-right: none;
                }
            """)
            self.info_label.setText("Custom Grid Table Style: Uses dashed lines to separate rows, customizes header borders, creating a unique visual style.")
        
        elif index == 7:
            # Complex style table
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #EEEEEE;
                    font-size: 14px;
                    border-radius: 8px;
                    border: 1px solid #EEEEEE;
                }
                QTableWidget::item {
                    padding: 12px 8px;
                    border: 1px solid #EEEEEE;
                }
                QTableWidget::item:selected {
                    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                                  stop:0 #64B5F6, stop:1 #42A5F5);
                    color: white;
                    border: 1px solid #42A5F5;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                }
                QHeaderView::section {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                                  stop:0 #F5F5F5, stop:1 #EEEEEE);
                    color: #333333;
                    padding: 12px 8px;
                    border: 1px solid #EEEEEE;
                    font-weight: bold;
                }
                QHeaderView::section:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                                  stop:0 #EEEEEE, stop:1 #E0E0E0);
                }
                QTableCornerButton::section {
                    background-color: #F5F5F5;
                    border: 1px solid #EEEEEE;
                }
            """)
            self.info_label.setText("Complex Style Table: Uses gradients, hover effects and multiple border styles to create an exquisite visual experience.")
    
    def reset_table(self):
        """Reset table data and style"""
        # Recreate table
        while self.table_layout.count() > 0:
            item = self.table_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Recreate table
        self.create_table()
        
        # Reset style selector
        self.style_combobox.setCurrentIndex(0)
        self.update_table_style(0)

# Main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())