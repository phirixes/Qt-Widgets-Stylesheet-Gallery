#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QCheckBox样式表示例
此文件展示了Qt中QCheckBox控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QCheckBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class CheckBoxStylesWindow(QMainWindow):
    """QCheckBox样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QCheckBox样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QCheckBox样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和复选框示例
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_custom_indicator_style_example()
        self.create_gradient_style_example()
        self.create_flat_style_example()
        self.create_radio_button_style_example()
        self.create_size_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 默认复选框
        default_checkbox = QCheckBox("默认复选框")
        layout.addWidget(default_checkbox)
        
        # 基本样式复选框
        basic_checkbox = QCheckBox("基本样式")
        basic_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #CCCCCC;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
        """)
        layout.addWidget(basic_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """状态样式表示例（正常、选中、悬停）"""
        section_label = QLabel("状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 状态样式复选框
        state_checkbox = QCheckBox("状态样式")
        state_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #CCCCCC;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:hover {
                border-color: #999999;
            }
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
            QCheckBox::indicator:checked:hover {
                background-color: #66BB6A;
            }
            QCheckBox::indicator:unchecked:disabled {
                background-color: #F5F5F5;
                border-color: #E0E0E0;
            }
            QCheckBox::indicator:checked:disabled {
                background-color: #E8F5E9;
                border-color: #C8E6C9;
            }
        """)
        layout.addWidget(state_checkbox)
        
        # 禁用状态复选框
        disabled_checkbox = QCheckBox("禁用状态")
        disabled_checkbox.setEnabled(False)
        disabled_checkbox.setChecked(True)
        disabled_checkbox.setStyleSheet("""
            QCheckBox {
                color: #9E9E9E;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #E0E0E0;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked:disabled {
                background-color: #E8F5E9;
                border-color: #C8E6C9;
            }
        """)
        layout.addWidget(disabled_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_indicator_style_example(self):
        """自定义指示器样式表示例"""
        section_label = QLabel("自定义指示器样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 圆形指示器复选框
        circle_checkbox = QCheckBox("圆形指示器")
        circle_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 22px;
                height: 22px;
                border: 2px solid #F44336;
                border-radius: 11px;  /* 宽度的一半 */
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #F44336;
            }
        """)
        layout.addWidget(circle_checkbox)
        
        # 带勾选标记的复选框
        checkmark_checkbox = QCheckBox("自定义勾选标记")
        checkmark_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #2196F3;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
            }
            /* Qt样式表不直接支持自定义勾选标记的形状 */
            /* 实际项目中需要通过子类化QCheckBox或使用图像实现 */
        """)
        layout.addWidget(checkmark_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 渐变背景复选框
        gradient_checkbox = QCheckBox("渐变背景")
        gradient_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #9C27B0;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 1, y2: 1,    /* 渐变结束点 */
                    stop: 0 #9C27B0, /* 起始颜色 */
                    stop: 1 #673AB7  /* 结束颜色 */
                );
            }
        """)
        layout.addWidget(gradient_checkbox)
        
        # 发光效果复选框
        glow_checkbox = QCheckBox("发光效果")
        glow_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #FF9800;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #FF9800;
                /* Qt样式表不直接支持box-shadow，但可以通过自定义绘制实现 */
            }
        """)
        layout.addWidget(glow_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_flat_style_example(self):
        """扁平风格样式表示例"""
        section_label = QLabel("扁平风格样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 扁平风格复选框
        flat_checkbox = QCheckBox("扁平风格")
        flat_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #607D8B;
                border-radius: 2px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #607D8B;
            }
        """)
        layout.addWidget(flat_checkbox)
        
        # 极简风格复选框
        minimal_checkbox = QCheckBox("极简风格")
        minimal_checkbox.setStyleSheet("""
            QCheckBox {
                color: #212121;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #757575;
                border-radius: 0;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #212121;
            }
        """)
        layout.addWidget(minimal_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_radio_button_style_example(self):
        """单选按钮风格的复选框"""
        section_label = QLabel("单选按钮风格")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 圆形单选按钮风格复选框
        radio_style_checkbox = QCheckBox("单选按钮风格")
        radio_style_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #00BCD4;
                border-radius: 10px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #00BCD4;
                /* 在实际项目中，可以添加自定义绘制的圆点 */
            }
        """)
        layout.addWidget(radio_style_checkbox)
        
        # 带圆点的单选风格复选框
        dot_radio_checkbox = QCheckBox("带圆点的单选风格")
        dot_radio_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: white;
                border-color: #4CAF50;
                /* Qt样式表不直接支持在指示器内绘制圆点 */
                /* 实际项目中需要通过子类化QCheckBox实现 */
            }
        """)
        layout.addWidget(dot_radio_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_size_style_example(self):
        """大小和间距样式表示例"""
        section_label = QLabel("大小和间距样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 小号复选框
        small_checkbox = QCheckBox("小号复选框")
        small_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 12px;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
                border: 1px solid #CCCCCC;
                border-radius: 2px;
            }
            QCheckBox::indicator:checked {
                background-color: #9E9E9E;
            }
        """)
        layout.addWidget(small_checkbox)
        
        # 大号复选框
        large_checkbox = QCheckBox("大号复选框")
        large_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 18px;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                border: 2px solid #FF5722;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background-color: #FF5722;
            }
        """)
        layout.addWidget(large_checkbox)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxStylesWindow()
    window.show()
    sys.exit(app.exec())