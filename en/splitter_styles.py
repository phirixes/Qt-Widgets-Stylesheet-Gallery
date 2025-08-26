# -*- coding: utf-8 -*-

"""
QSplitter Style Sheet Examples
This file demonstrates how to customize various style effects for the QSplitter widget in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QSplitter,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QFrame,
    QTextEdit
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class SplitterStylesWindow(QMainWindow):
    """QSplitter Style Sheet Example Window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QSplitter Style Sheet Examples")
        self.resize(900, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QSplitter Style Sheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select splitter style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Splitter", 
            "Modern Splitter", 
            "Dashed Splitter",
            "Colored Splitter",
            "Hidden Splitter",
            "Round Splitter",
            "Gradient Splitter",
            "3D Splitter"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_splitter_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset Splitter")
        self.reset_button.clicked.connect(self.reset_splitter)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create splitter container
        self.splitter_container = QWidget()
        self.splitter_layout = QVBoxLayout(self.splitter_container)
        self.splitter_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.splitter_container)
        
        # Create splitters
        self.create_splitter()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic splitter by default
        self.update_splitter_style(0)
    
    def create_splitter(self):
        """Create splitter and content"""
        # Create main vertical splitter
        self.main_splitter = QSplitter(Qt.Vertical)
        
        # Create top horizontal splitter
        self.top_splitter = QSplitter(Qt.Horizontal)
        
        # Create left and right panels
        self.left_panel = self._create_panel("Left Panel")
        self.right_panel = self._create_panel("Right Panel")
        
        # Add to top horizontal splitter
        self.top_splitter.addWidget(self.left_panel)
        self.top_splitter.addWidget(self.right_panel)
        self.top_splitter.setSizes([300, 400])  # Set initial size ratio
        
        # Create bottom panel
        self.bottom_panel = self._create_panel("Bottom Panel")
        
        # Add to main vertical splitter
        self.main_splitter.addWidget(self.top_splitter)
        self.main_splitter.addWidget(self.bottom_panel)
        self.main_splitter.setSizes([400, 200])  # Set initial size ratio
        
        # Add main splitter to layout
        self.splitter_layout.addWidget(self.main_splitter)
    
    def _create_panel(self, title):
        """Create panel"""
        # Create panel frame
        panel = QFrame()
        panel.setFrameShape(QFrame.StyledPanel)
        panel.setMinimumSize(200, 100)  # Set minimum size
        
        # Create layout
        panel_layout = QVBoxLayout(panel)
        
        # Add title
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        panel_layout.addWidget(title_label)
        
        # Add content area
        content_text = QTextEdit()
        content_text.setReadOnly(True)
        content_text.setPlaceholderText(f"This is the content area for {title}")
        panel_layout.addWidget(content_text)
        
        return panel
    
    def update_splitter_style(self, index):
        """Update splitter style based on selection"""
        # Clear previous styles
        self.main_splitter.setStyleSheet("")
        self.top_splitter.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: #CCCCCC;
                }
                QSplitter::handle:vertical {
                    height: 10px;
                    background-color: #CCCCCC;
                }
                QSplitter::handle:horizontal {
                    width: 10px;
                    background-color: #CCCCCC;
                }
                QSplitter::handle:hover {
                    background-color: #BBBBBB;
                }
                QSplitter::handle:pressed {
                    background-color: #AAAAAA;
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("Basic Splitter Style: Simple gray splitter with different background colors on hover and click.")
        
        elif index == 1:
            # Modern splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: #E0E0E0;
                    border-radius: 2px;
                }
                QSplitter::handle:vertical {
                    height: 6px;
                    margin: 0 20%;
                }
                QSplitter::handle:horizontal {
                    width: 6px;
                    margin: 20% 0;
                }
                QSplitter::handle:hover {
                    background-color: #BDBDBD;
                }
                QSplitter::handle:pressed {
                    background-color: #9E9E9E;
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("Modern Splitter Style: Thinner splitter with rounded corners, only displayed in the middle part.")
        
        elif index == 2:
            # Dashed splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: transparent;
                    border: 1px dashed #9E9E9E;
                }
                QSplitter::handle:vertical {
                    height: 8px;
                }
                QSplitter::handle:horizontal {
                    width: 8px;
                }
                QSplitter::handle:hover {
                    border-color: #757575;
                    background-color: rgba(158, 158, 158, 0.1);
                }
                QSplitter::handle:pressed {
                    border-color: #616161;
                    background-color: rgba(158, 158, 158, 0.2);
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("Dashed Splitter Style: Uses dashed border instead of filled background color for a lighter visual effect.")
        
        elif index == 3:
            # Colored splitter style
            vertical_style = """
                QSplitter::handle:vertical {
                    height: 8px;
                    background-color: #4CAF50;
                    margin: 0 30%;
                    border-radius: 4px;
                }
                QSplitter::handle:vertical:hover {
                    background-color: #45A049;
                }
                QSplitter::handle:vertical:pressed {
                    background-color: #388E3C;
                }
            """
            
            horizontal_style = """
                QSplitter::handle:horizontal {
                    width: 8px;
                    background-color: #2196F3;
                    margin: 30% 0;
                    border-radius: 4px;
                }
                QSplitter::handle:horizontal:hover {
                    background-color: #0B7dda;
                }
                QSplitter::handle:horizontal:pressed {
                    background-color: #0d47a1;
                }
            """
            
            self.main_splitter.setStyleSheet(vertical_style)
            self.top_splitter.setStyleSheet(horizontal_style)
            self.info_label.setText("Colored Splitter Style: Sets different colors for vertical and horizontal splitters to make the interface more lively.")
        
        elif index == 4:
            # Hidden splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: transparent;
                }
                QSplitter::handle:vertical {
                    height: 16px;
                }
                QSplitter::handle:horizontal {
                    width: 16px;
                }
                QSplitter::handle:hover {
                    background-color: rgba(0, 0, 0, 0.1);
                }
                QSplitter::handle:pressed {
                    background-color: rgba(0, 0, 0, 0.2);
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("Hidden Splitter Style: Invisible by default, only appears when mouse hovers or drags.")
        
        elif index == 5:
            # Round splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: #9C27B0;
                    border-radius: 10px;
                }
                QSplitter::handle:vertical {
                    height: 20px;
                    width: 20px;
                    margin: 0 auto;
                }
                QSplitter::handle:horizontal {
                    width: 20px;
                    height: 20px;
                    margin: auto 0;
                }
                QSplitter::handle:hover {
                    background-color: #7B1FA2;
                }
                QSplitter::handle:pressed {
                    background-color: #6A1B9A;
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("Round Splitter Style: Uses round splitter handles that look like draggable buttons.")
        
        elif index == 6:
            # Gradient splitter style
            vertical_style = """
                QSplitter::handle:vertical {
                    height: 10px;
                    margin: 0 25%;
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF5722, stop:1 #E91E63);
                    border-radius: 5px;
                }
                QSplitter::handle:vertical:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF7043, stop:1 #F06292);
                }
                QSplitter::handle:vertical:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #E64A19, stop:1 #C2185B);
                }
            """
            
            horizontal_style = """
                QSplitter::handle:horizontal {
                    width: 10px;
                    margin: 25% 0;
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #2196F3, stop:1 #00BCD4);
                    border-radius: 5px;
                }
                QSplitter::handle:horizontal:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #42A5F5, stop:1 #26C6DA);
                }
                QSplitter::handle:horizontal:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1976D2, stop:1 #00ACC1);
                }
            """
            
            self.main_splitter.setStyleSheet(vertical_style)
            self.top_splitter.setStyleSheet(horizontal_style)
            self.info_label.setText("Gradient Splitter Style: Uses gradient effects to enhance the visual appeal of the splitter.")
        
        elif index == 7:
            # 3D splitter style
            splitter_style = """
                QSplitter::handle {
                    background-color: #E0E0E0;
                }
                QSplitter::handle:vertical {
                    height: 16px;
                    border-top: 1px solid #FFFFFF;
                    border-bottom: 1px solid #BDBDBD;
                }
                QSplitter::handle:horizontal {
                    width: 16px;
                    border-left: 1px solid #FFFFFF;
                    border-right: 1px solid #BDBDBD;
                }
                QSplitter::handle:hover {
                    background-color: #D5D5D5;
                }
                QSplitter::handle:pressed {
                    background-color: #CCCCCC;
                    border-top: 1px solid #BDBDBD;
                    border-bottom: 1px solid #FFFFFF;
                    border-left: 1px solid #BDBDBD;
                    border-right: 1px solid #FFFFFF;
                }
            """
            
            self.main_splitter.setStyleSheet(splitter_style)
            self.top_splitter.setStyleSheet(splitter_style)
            self.info_label.setText("3D Splitter Style: Uses border shadows to create a 3D effect, and the border effect is reversed when dragged.")
    
    def reset_splitter(self):
        """Reset splitter style and position"""
        # Reset splitter position
        self.top_splitter.setSizes([300, 400])
        self.main_splitter.setSizes([400, 200])
        
        # Restore default style
        self.update_splitter_style(self.style_combobox.currentIndex())

# Main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitterStylesWindow()
    window.show()
    sys.exit(app.exec())