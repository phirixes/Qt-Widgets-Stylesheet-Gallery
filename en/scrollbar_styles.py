#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QScrollBar Styles Example
This file demonstrates how to customize various styles for QScrollBar widgets in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QFrame
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class ScrollBarStylesWindow(QMainWindow):
    """QScrollBar styles example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QScrollBar Styles Example")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QScrollBar Styles Example")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select Scrollbar Style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Scrollbar", 
            "Modern Scrollbar", 
            "Ultra-Thin Scrollbar",
            "Round Scrollbar",
            "Colorful Scrollbar",
            "Dark Theme Scrollbar",
            "Hidden Scrollbar",
            "Gradient Scrollbar"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_scrollbar_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset Scrollbar")
        self.reset_button.clicked.connect(self.reset_scrollbar)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create scroll area
        self.create_scroll_area()
        
        # Add description
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic scrollbar by default
        self.update_scrollbar_style(0)
    
    def create_scroll_area(self):
        """Create scroll area and content"""
        # Create scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        # Create scroll area content
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        
        # Add enough content to activate scrollbars
        for i in range(20):
            # Create a frame as content item
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setMinimumHeight(80)
            frame.setMaximumWidth(700)
            
            # Set label content
            label = QLabel(f"Scroll Content Example #{i+1}")
            label.setStyleSheet("font-size: 16px; margin: 20px;")
            label.setAlignment(Qt.AlignCenter)
            
            # Add to frame
            frame_layout = QVBoxLayout(frame)
            frame_layout.addWidget(label)
            
            # Add to content layout
            self.content_layout.addWidget(frame)
        
        # Create horizontal content
        horizontal_content = QWidget()
        horizontal_layout = QHBoxLayout(horizontal_content)
        horizontal_layout.setContentsMargins(20, 20, 20, 20)
        
        for i in range(15):
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setMinimumWidth(100)
            frame.setMinimumHeight(100)
            
            label = QLabel(f"{i+1}")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 16px;")
            
            frame_layout = QVBoxLayout(frame)
            frame_layout.addWidget(label)
            
            horizontal_layout.addWidget(frame)
        
        self.content_layout.addWidget(horizontal_content)
        
        # Set scroll area content
        self.scroll_area.setWidget(content_widget)
        
        # Add scroll area to main layout
        self.main_layout.addWidget(self.scroll_area)
    
    def update_scrollbar_style(self, index):
        """Update scrollbar style based on selection"""
        # Clear previous style
        self.scroll_area.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #CCCCCC;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: #F5F5F5;
                    width: 12px;
                    margin: 0;
                }
                QScrollBar::handle:vertical {
                    background: #CCCCCC;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #BBBBBB;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #AAAAAA;
                }
                QScrollBar::sub-line:vertical {
                    background: none;
                }
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: #F5F5F5;
                    height: 12px;
                    margin: 0;
                }
                QScrollBar::handle:horizontal {
                    background: #CCCCCC;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #BBBBBB;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #AAAAAA;
                }
                QScrollBar::sub-line:horizontal {
                    background: none;
                }
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("Basic Scrollbar Style: Simple gray scrollbar without arrow buttons, providing basic scrolling functionality.")
        
        elif index == 1:
            # Modern scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: white;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: #FAFAFA;
                    width: 8px;
                    margin: 2px;
                    border-radius: 4px;
                }
                QScrollBar::handle:vertical {
                    background: #CCCCCC;
                    border-radius: 4px;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #AAAAAA;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: #FAFAFA;
                    height: 8px;
                    margin: 2px;
                    border-radius: 4px;
                }
                QScrollBar::handle:horizontal {
                    background: #CCCCCC;
                    border-radius: 4px;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #AAAAAA;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("Modern Scrollbar Style: Narrower scrollbar with rounded corners, different background colors on hover and click.")
        
        elif index == 2:
            # Ultra-thin scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: none;
                    background-color: white;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: transparent;
                    width: 4px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical {
                    background: #BBBBBB;
                    border-radius: 2px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #888888;
                    width: 6px;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #555555;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 4px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal {
                    background: #BBBBBB;
                    border-radius: 2px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #888888;
                    height: 6px;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #555555;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("Ultra-Thin Scrollbar Style: Very thin scrollbar that becomes thicker on hover, almost invisible, suitable for minimalist interfaces.")
        
        elif index == 3:
            # Round scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: #FAFAFA;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: transparent;
                    width: 20px;
                    margin: 5px;
                }
                QScrollBar::handle:vertical {
                    background: #4CAF50;
                    border-radius: 10px;
                    min-height: 40px;
                    width: 16px;
                    margin: 2px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #45A049;
                    width: 18px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #388E3C;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: #4CAF50;
                    width: 16px;
                    height: 16px;
                    margin: 2px;
                    border-radius: 8px;
                }
                QScrollBar::sub-line:vertical:hover,
                QScrollBar::add-line:vertical:hover {
                    background: #45A049;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: transparent;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 20px;
                    margin: 5px;
                }
                QScrollBar::handle:horizontal {
                    background: #2196F3;
                    border-radius: 10px;
                    min-width: 40px;
                    height: 16px;
                    margin: 2px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #0B7dda;
                    height: 18px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #0d47a1;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: #2196F3;
                    width: 16px;
                    height: 16px;
                    margin: 2px;
                    border-radius: 8px;
                }
                QScrollBar::sub-line:horizontal:hover,
                QScrollBar::add-line:horizontal:hover {
                    background: #0B7dda;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: transparent;
                }
            """)
            self.info_label.setText("Round Scrollbar Style: Uses round scrollbars and buttons for a friendly visual effect.")
        
        elif index == 4:
            # Colorful scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: white;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: #F9F9F9;
                    width: 14px;
                    margin: 2px;
                    border-radius: 7px;
                }
                QScrollBar::handle:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF5722, stop:1 #E91E63);
                    border-radius: 7px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF7043, stop:1 #F06292);
                }
                QScrollBar::handle:vertical:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #E64A19, stop:1 #C2185B);
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: #F9F9F9;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow.png);
                }
                QScrollBar::sub-page:vertical {
                    background: #FFF3E0;
                    border-radius: 7px;
                }
                QScrollBar::add-page:vertical {
                    background: #F3E5F5;
                    border-radius: 7px;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: #F9F9F9;
                    height: 14px;
                    margin: 2px;
                    border-radius: 7px;
                }
                QScrollBar::handle:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #2196F3, stop:1 #00BCD4);
                    border-radius: 7px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #42A5F5, stop:1 #26C6DA);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1976D2, stop:1 #00ACC1);
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: #F9F9F9;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow.png);
                }
                QScrollBar::sub-page:horizontal {
                    background: #E0F7FA;
                    border-radius: 7px;
                }
                QScrollBar::add-page:horizontal {
                    background: #E8F5E9;
                    border-radius: 7px;
                }
            """)
            self.info_label.setText("Colorful Scrollbar Style: Uses gradient backgrounds and colored areas to make scrollbars more eye-catching.")
        
        elif index == 5:
            # Dark theme scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #444444;
                    background-color: #2C2C2C;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: #3C3C3C;
                    width: 14px;
                    margin: 2px;
                }
                QScrollBar::handle:vertical {
                    background: #666666;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #777777;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:vertical {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::add-line:vertical {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow-white.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow-white.png);
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: #333333;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: #3C3C3C;
                    height: 14px;
                    margin: 2px;
                }
                QScrollBar::handle:horizontal {
                    background: #666666;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #777777;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:horizontal {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::add-line:horizontal {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow-white.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow-white.png);
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: #333333;
                }
            """)
            self.info_label.setText("Dark Theme Scrollbar Style: Uses dark backgrounds, suitable for dark-themed interfaces.")
        
        elif index == 6:
            # Hidden scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: none;
                    background-color: white;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: transparent;
                    width: 8px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical {
                    background: transparent;
                    border-radius: 4px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: rgba(100, 100, 100, 0.3);
                }
                QScrollBar::handle:vertical:pressed {
                    background: rgba(100, 100, 100, 0.5);
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 8px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal {
                    background: transparent;
                    border-radius: 4px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: rgba(100, 100, 100, 0.3);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: rgba(100, 100, 100, 0.5);
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("Hidden Scrollbar Style: Hidden by default, only visible on mouse hover, providing a clean visual effect.")
        
        elif index == 7:
            # Gradient scrollbar style
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #E0E0E0;
                    background-color: #F5F5F5;
                }
                
                /* Vertical scrollbar */
                QScrollBar:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #EEEEEE, stop:1 #E0E0E0);
                    width: 16px;
                    margin: 0;
                    border-left: 1px solid #CCCCCC;
                }
                QScrollBar::handle:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #1A237E, stop:1 #283593);
                    min-height: 40px;
                    border-radius: 8px;
                    margin: 3px;
                }
                QScrollBar::handle:vertical:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #303F9F, stop:1 #3949AB);
                }
                QScrollBar::handle:vertical:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #1A237E, stop:1 #0D47A1);
                }
                QScrollBar::sub-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    height: 24px;
                    border-bottom: 1px solid #CCCCCC;
                }
                QScrollBar::add-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    height: 24px;
                    border-top: 1px solid #CCCCCC;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow-white.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow-white.png);
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* Horizontal scrollbar */
                QScrollBar:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #EEEEEE, stop:1 #E0E0E0);
                    height: 16px;
                    margin: 0;
                    border-top: 1px solid #CCCCCC;
                }
                QScrollBar::handle:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1A237E, stop:1 #283593);
                    min-width: 40px;
                    border-radius: 8px;
                    margin: 3px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #303F9F, stop:1 #3949AB);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1A237E, stop:1 #0D47A1);
                }
                QScrollBar::sub-line:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    width: 24px;
                    border-right: 1px solid #CCCCCC;
                }
                QScrollBar::add-line:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    width: 24px;
                    border-left: 1px solid #CCCCCC;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow-white.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow-white.png);
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("Gradient Scrollbar Style: Uses gradient effects to enhance the visual appeal of scrollbars.")
    
    def reset_scrollbar(self):
        """Reset scrollbar style"""
        # Reset scrollbar position
        self.scroll_area.verticalScrollBar().setValue(0)
        self.scroll_area.horizontalScrollBar().setValue(0)
        
        # Restore default style
        self.update_scrollbar_style(self.style_combobox.currentIndex())

# Launch function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollBarStylesWindow()
    window.show()
    sys.exit(app.exec())