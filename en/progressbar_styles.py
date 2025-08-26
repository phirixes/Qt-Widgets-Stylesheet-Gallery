# -*- coding: utf-8 -*-

"""
QProgressBar Stylesheet Examples
This file demonstrates how to customize various style effects for the QProgressBar widget in Qt.
"""

import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QProgressBar, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox
from PySide6.QtGui import QColor

class ProgressBarStylesWindow(QMainWindow):
    """QProgressBar stylesheet example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QProgressBar Stylesheet Examples")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QProgressBar Stylesheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select progress bar style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Progress Bar", 
            "Gradient Progress Bar", 
            "Circular Progress Bar", 
            "Segmented Progress Bar",
            "Glassmorphism Effect",
            "Neon Effect",
            "3D Effect",
            "Custom Text Display"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_progress_bar_style)
        
        # Control buttons
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_progress)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_progress)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.start_button)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create progress bar container
        self.progress_container = QWidget()
        self.progress_layout = QVBoxLayout(self.progress_container)
        self.main_layout.addWidget(self.progress_container)
        
        # Create various progress bars
        self.create_progress_bars()
        
        # Set up timer for updating progress
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        
        # Default to showing basic progress bar
        self.update_progress_bar_style(0)
    
    def create_progress_bars(self):
        """Create various progress bars"""
        # Basic progress bar
        self.basic_progress = QProgressBar()
        self.basic_progress.setValue(0)
        self.basic_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("1. Basic Progress Bar"))
        self.progress_layout.addWidget(self.basic_progress)
        
        # Gradient progress bar
        self.gradient_progress = QProgressBar()
        self.gradient_progress.setValue(0)
        self.gradient_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("2. Gradient Progress Bar"))
        self.progress_layout.addWidget(self.gradient_progress)
        
        # Circular progress bar
        self.circular_progress = QProgressBar()
        self.circular_progress.setValue(0)
        self.circular_progress.setMinimumSize(150, 150)
        self.progress_layout.addWidget(QLabel("3. Circular Progress Bar"))
        self.progress_layout.addWidget(self.circular_progress, alignment=Qt.AlignCenter)
        
        # Segmented progress bar
        self.segmented_progress = QProgressBar()
        self.segmented_progress.setValue(0)
        self.segmented_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("4. Segmented Progress Bar"))
        self.progress_layout.addWidget(self.segmented_progress)
        
        # Glassmorphism effect progress bar
        self.glass_progress = QProgressBar()
        self.glass_progress.setValue(0)
        self.glass_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("5. Glassmorphism Effect"))
        self.progress_layout.addWidget(self.glass_progress)
        
        # Neon effect progress bar
        self.neon_progress = QProgressBar()
        self.neon_progress.setValue(0)
        self.neon_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("6. Neon Effect"))
        self.progress_layout.addWidget(self.neon_progress)
        
        # 3D effect progress bar
        self.three_d_progress = QProgressBar()
        self.three_d_progress.setValue(0)
        self.three_d_progress.setMinimumHeight(40)
        self.progress_layout.addWidget(QLabel("7. 3D Effect"))
        self.progress_layout.addWidget(self.three_d_progress)
        
        # Custom text display progress bar
        self.custom_text_progress = QProgressBar()
        self.custom_text_progress.setValue(0)
        self.custom_text_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("8. Custom Text Display"))
        self.progress_layout.addWidget(self.custom_text_progress)
        
        # Add description
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.progress_layout.addWidget(self.info_label)
        
        # Apply styles
        self.apply_styles()
        
        # Hide all progress bars by default
        for i in range(1, self.progress_layout.count()):
            widget = self.progress_layout.itemAt(i).widget()
            if widget and widget != self.info_label:
                widget.hide()
    
    def apply_styles(self):
        """Apply various progress bar styles"""
        # 1. Basic progress bar style
        self.basic_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #333;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                border-radius: 10px;
            }
        """)
        
        # 2. Gradient progress bar style
        self.gradient_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-weight: bold;
                border: 1px solid #BDBDBD;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                          stop:0 #4CAF50, stop:1 #2196F3);
                border-radius: 15px;
                border: 1px solid #4CAF50;
            }
        """)
        
        # 3. Circular progress bar style
        self.circular_progress.setStyleSheet("""
            QProgressBar {
                background-color: #F5F5F5;
                border-radius: 75px;
                text-align: center;
                color: #2196F3;
                font-weight: bold;
                font-size: 18px;
                border: 8px solid #E0E0E0;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                border-radius: 75px;
                border: 8px solid #1976D2;
            }
        """)
        
        # 4. Segmented progress bar style
        self.segmented_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #333;
                font-weight: bold;
                border: 1px solid #BDBDBD;
            }
            QProgressBar::chunk {
                background-color: #FF9800;
                width: 20px;
                margin: 1px;
                border-radius: 3px;
            }
        """)
        
        # 5. Glassmorphism effect progress bar style
        self.glass_progress.setStyleSheet("""
            QProgressBar {
                background-color: rgba(224, 224, 224, 150);
                border-radius: 15px;
                text-align: center;
                color: #333;
                font-weight: bold;
                border: 1px solid rgba(189, 189, 189, 150);
                backdrop-filter: blur(5px);
            }
            QProgressBar::chunk {
                background-color: rgba(33, 150, 243, 200);
                border-radius: 15px;
                border: 1px solid rgba(25, 118, 210, 200);
            }
        """)
        
        # 6. Neon effect progress bar style
        self.neon_progress.setStyleSheet("""
            QProgressBar {
                background-color: #1A1A1A;
                border-radius: 15px;
                text-align: center;
                color: #00BCD4;
                font-weight: bold;
                border: 1px solid #00BCD4;
                padding: 2px;
            }
            QProgressBar::chunk {
                background-color: #00BCD4;
                border-radius: 13px;
                box-shadow: 0 0 10px #00BCD4, 0 0 20px #00BCD4;
            }
        """)
        
        # 7. 3D effect progress bar style
        self.three_d_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 20px;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border: 1px solid #BDBDBD;
                box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #4CAF50, stop:1 #388E3C);
                border-radius: 20px;
                border: 1px solid #4CAF50;
                box-shadow: inset 0 2px 4px rgba(255, 255, 255, 0.3);
            }
        """)
        
        # 8. Custom text display progress bar style
        self.custom_text_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #F44336;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QProgressBar::chunk {
                background-color: #F44336;
                border-radius: 10px;
            }
        """)
        
        # Set custom text display
        self.custom_text_progress.setFormat("%v%% Completed")
    
    def update_progress_bar_style(self, index):
        """Update displayed progress bar style based on selection"""
        # Hide all progress bars
        for i in range(1, self.progress_layout.count()):
            widget = self.progress_layout.itemAt(i).widget()
            if widget and widget != self.info_label:
                widget.hide()
        
        # Show selected progress bar
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        # Show corresponding label and progress bar
        self.progress_layout.itemAt(index * 2).widget().show()  # Show label
        progress_bars[index].show()  # Show progress bar
        
        # Update description
        descriptions = [
            "Basic progress bar uses simple rounded rectangle design, suitable for most application scenarios.",
            "Gradient progress bar uses linear gradient effect to create smooth color transitions.",
            "Circular progress bar adopts circular design, suitable for displaying percentage completion.",
            "Segmented progress bar displays progress as discrete blocks, providing a different visual experience.",
            "Glassmorphism effect creates a modern interface through semi-transparency and blur effects.",
            "Neon effect creates a futuristic visual effect using glow and shadows.",
            "3D effect creates a three-dimensional visual experience through multiple shadows and gradients.",
            "Custom text display allows you to modify the format and style of text displayed on the progress bar."
        ]
        self.info_label.setText(descriptions[index])
    
    def start_progress(self):
        """Start updating progress"""
        if not self.timer.isActive():
            self.timer.start(50)  # Update every 50 milliseconds
            self.start_button.setText("Pause")
        else:
            self.timer.stop()
            self.start_button.setText("Continue")
    
    def reset_progress(self):
        """Reset progress"""
        self.timer.stop()
        self.progress_value = 0
        
        # Reset all progress bars
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        for progress_bar in progress_bars:
            progress_bar.setValue(0)
        
        self.start_button.setText("Start")
    
    def update_progress(self):
        """Update progress value"""
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        
        # Update all progress bars
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        for progress_bar in progress_bars:
            progress_bar.setValue(self.progress_value)

# Launch function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBarStylesWindow()
    window.show()
    sys.exit(app.exec())