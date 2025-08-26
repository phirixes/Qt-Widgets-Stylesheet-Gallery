#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QSlider样式表示例
此文件展示了Qt中QSlider控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QSlider, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QGridLayout
)
from PySide6.QtGui import QFont, QColor

class SliderStylesWindow(QMainWindow):
    """QSlider样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QSlider样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QSlider样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和滑块示例
        self.create_basic_style_example()
        self.create_orientation_style_example()
        self.create_gradient_style_example()
        self.create_round_handle_style_example()
        self.create_flat_style_example()
        self.create_groove_style_example()
        self.create_tick_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 默认滑块
        default_slider = QSlider(Qt.Horizontal)
        default_slider.setRange(0, 100)
        default_slider.setValue(50)
        layout.addWidget(default_slider)
        
        # 基本样式滑块
        basic_slider = QSlider(Qt.Horizontal)
        basic_slider.setRange(0, 100)
        basic_slider.setValue(50)
        basic_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #CCCCCC;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #2196F3;
                width: 16px;
                height: 16px;
                margin: -4px 0;
                border-radius: 8px;
            }
        """)
        layout.addWidget(basic_slider)
        
        self.main_layout.addLayout(layout)
    
    def create_orientation_style_example(self):
        """不同方向样式表示例"""
        section_label = QLabel("方向样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QGridLayout()
        
        # 水平滑块
        horizontal_slider = QSlider(Qt.Horizontal)
        horizontal_slider.setRange(0, 100)
        horizontal_slider.setValue(50)
        horizontal_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #E0E0E0;
                height: 10px;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                width: 20px;
                height: 20px;
                margin: -5px 0;
                border-radius: 10px;
            }
        """)
        layout.addWidget(horizontal_slider, 0, 0)
        
        # 垂直滑块
        vertical_slider = QSlider(Qt.Vertical)
        vertical_slider.setRange(0, 100)
        vertical_slider.setValue(50)
        vertical_slider.setStyleSheet("""
            QSlider::groove:vertical {
                background: #E0E0E0;
                width: 10px;
                border-radius: 5px;
            }
            QSlider::handle:vertical {
                background: #F44336;
                width: 20px;
                height: 20px;
                margin: 0 -5px;
                border-radius: 10px;
            }
        """)
        layout.addWidget(vertical_slider, 0, 1)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 线性渐变滑块
        gradient_slider = QSlider(Qt.Horizontal)
        gradient_slider.setRange(0, 100)
        gradient_slider.setValue(50)
        gradient_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 1, y2: 0,    /* 渐变结束点 */
                    stop: 0 #FF9800, /* 起始颜色 */
                    stop: 1 #F44336  /* 结束颜色 */
                );
                height: 10px;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background: white;
                width: 20px;
                height: 20px;
                margin: -5px 0;
                border-radius: 10px;
                border: 2px solid #FF5722;
            }
        """)
        layout.addWidget(gradient_slider)
        
        # 另一种渐变样式
        alternate_gradient_slider = QSlider(Qt.Horizontal)
        alternate_gradient_slider.setRange(0, 100)
        alternate_gradient_slider.setValue(50)
        alternate_gradient_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 0, y2: 1,    /* 渐变结束点 */
                    stop: 0 #9C27B0, /* 起始颜色 */
                    stop: 1 #673AB7  /* 结束颜色 */
                );
                height: 15px;
                border-radius: 7px;
            }
            QSlider::handle:horizontal {
                background: qradialgradient(
                    cx: 0.5, cy: 0.5,    /* 中心点 */
                    radius: 0.5,         /* 半径 */
                    fx: 0.5, fy: 0.5,    /* 焦点 */
                    stop: 0 #FFFFFF,     /* 中心颜色 */
                    stop: 1 #E1BEE7      /* 边缘颜色 */
                );
                width: 25px;
                height: 25px;
                margin: -5px 0;
                border-radius: 12px;
                border: 1px solid #9575CD;
            }
        """)
        layout.addWidget(alternate_gradient_slider)
        
        self.main_layout.addLayout(layout)
    
    def create_round_handle_style_example(self):
        """圆形手柄样式表示例"""
        section_label = QLabel("圆形手柄样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 简单圆形手柄
        simple_round_slider = QSlider(Qt.Horizontal)
        simple_round_slider.setRange(0, 100)
        simple_round_slider.setValue(50)
        simple_round_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #E0E0E0;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #00BCD4;
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
        """)
        layout.addWidget(simple_round_slider)
        
        # 带边框的圆形手柄
        bordered_round_slider = QSlider(Qt.Horizontal)
        bordered_round_slider.setRange(0, 100)
        bordered_round_slider.setValue(50)
        bordered_round_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #E0E0E0;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: white;
                width: 20px;
                height: 20px;
                margin: -7px 0;
                border-radius: 10px;
                border: 2px solid #FF9800;
            }
            QSlider::handle:horizontal:hover {
                border-color: #FF5722;
                background: #FFF3E0;
            }
        """)
        layout.addWidget(bordered_round_slider)
        
        self.main_layout.addLayout(layout)
    
    def create_flat_style_example(self):
        """扁平风格样式表示例"""
        section_label = QLabel("扁平风格样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 扁平风格滑块
        flat_slider = QSlider(Qt.Horizontal)
        flat_slider.setRange(0, 100)
        flat_slider.setValue(50)
        flat_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #ECEFF1;
                height: 4px;
            }
            QSlider::handle:horizontal {
                background: #3F51B5;
                width: 24px;
                height: 24px;
                margin: -10px 0;
                border-radius: 12px;
            }
            QSlider::handle:horizontal:hover {
                background: #5C6BC0;
            }
            QSlider::handle:horizontal:pressed {
                background: #303F9F;
            }
        """)
        layout.addWidget(flat_slider)
        
        # 极简风格滑块
        minimal_slider = QSlider(Qt.Horizontal)
        minimal_slider.setRange(0, 100)
        minimal_slider.setValue(50)
        minimal_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #BDBDBD;
                height: 2px;
            }
            QSlider::handle:horizontal {
                background: #212121;
                width: 16px;
                height: 16px;
                margin: -7px 0;
                border-radius: 8px;
            }
        """)
        layout.addWidget(minimal_slider)
        
        self.main_layout.addLayout(layout)
    
    def create_groove_style_example(self):
        """轨道样式表示例"""
        section_label = QLabel("轨道样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 凹陷轨道滑块
        sunken_groove_slider = QSlider(Qt.Horizontal)
        sunken_groove_slider.setRange(0, 100)
        sunken_groove_slider.setValue(50)
        sunken_groove_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #BDBDBD,
                    stop: 1 #FFFFFF
                );
                height: 12px;
                border: 1px solid #9E9E9E;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #FFFFFF,
                    stop: 1 #E0E0E0
                );
                width: 20px;
                height: 20px;
                margin: -4px 0;
                border: 1px solid #BDBDBD;
                border-radius: 10px;
            }
        """)
        layout.addWidget(sunken_groove_slider)
        
        # 带进度的轨道滑块
        progress_groove_slider = QSlider(Qt.Horizontal)
        progress_groove_slider.setRange(0, 100)
        progress_groove_slider.setValue(50)
        progress_groove_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #E0E0E0;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::sub-page:horizontal {
                background: #4CAF50;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: white;
                width: 18px;
                height: 18px;
                margin: -5px 0;
                border-radius: 9px;
                border: 2px solid #4CAF50;
            }
        """)
        layout.addWidget(progress_groove_slider)
        
        self.main_layout.addLayout(layout)
    
    def create_tick_style_example(self):
        """刻度样式表示例"""
        section_label = QLabel("刻度样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QVBoxLayout()
        
        # 带刻度的滑块
        tick_slider = QSlider(Qt.Horizontal)
        tick_slider.setRange(0, 100)
        tick_slider.setValue(50)
        tick_slider.setTickPosition(QSlider.TicksBelow)
        tick_slider.setTickInterval(20)
        tick_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #E0E0E0;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #2196F3;
                width: 18px;
                height: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QSlider::tick-mark:horizontal {
                background: #9E9E9E;
                width: 2px;
                height: 8px;
            }
        """)
        layout.addWidget(tick_slider)
        
        # 垂直带刻度的滑块
        vertical_tick_slider = QSlider(Qt.Vertical)
        vertical_tick_slider.setRange(0, 100)
        vertical_tick_slider.setValue(50)
        vertical_tick_slider.setTickPosition(QSlider.TicksRight)
        vertical_tick_slider.setTickInterval(20)
        vertical_tick_slider.setStyleSheet("""
            QSlider::groove:vertical {
                background: #E0E0E0;
                width: 8px;
                border-radius: 4px;
            }
            QSlider::handle:vertical {
                background: #F44336;
                width: 18px;
                height: 18px;
                margin: 0 -5px;
                border-radius: 9px;
            }
            QSlider::tick-mark:vertical {
                background: #9E9E9E;
                width: 8px;
                height: 2px;
            }
        """)
        
        # 添加垂直滑块到水平布局中
        vertical_layout = QHBoxLayout()
        vertical_layout.addWidget(vertical_tick_slider)
        vertical_layout.addStretch()
        layout.addLayout(vertical_layout)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderStylesWindow()
    window.show()
    sys.exit(app.exec())