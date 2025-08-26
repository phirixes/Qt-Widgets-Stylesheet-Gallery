#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QLineEdit样式表示例
此文件展示了Qt中QLineEdit控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLineEdit, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class LineEditStylesWindow(QMainWindow):
    """QLineEdit样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLineEdit样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QLineEdit样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和输入框示例
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_placeholder_style_example()
        self.create_password_style_example()
        self.create_gradient_style_example()
        self.create_custom_cursor_style_example()
        self.create_icon_style_example()
        self.create_readonly_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 默认输入框
        default_lineedit = QLineEdit()
        default_lineedit.setPlaceholderText("默认输入框")
        layout.addWidget(default_lineedit)
        
        # 基本样式输入框
        basic_lineedit = QLineEdit()
        basic_lineedit.setPlaceholderText("基本样式")
        basic_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        layout.addWidget(basic_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """状态样式表示例（正常、悬停、聚焦）"""
        section_label = QLabel("状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 悬停和聚焦状态样式
        state_lineedit = QLineEdit()
        state_lineedit.setPlaceholderText("悬停和聚焦效果")
        state_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                transition: border-color 0.3s ease;
            }
            QLineEdit:hover {
                border-color: #999999;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                background-color: #F5F5F5;
                outline: none;  /* 移除默认的聚焦轮廓 */
            }
        """)
        layout.addWidget(state_lineedit)
        
        # 不同颜色主题的输入框
        blue_lineedit = QLineEdit()
        blue_lineedit.setPlaceholderText("蓝色主题")
        blue_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #E3F2FD;
                color: #1565C0;
                border: 2px solid #90CAF9;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #1976D2;
                background-color: #BBDEFB;
            }
        """)
        layout.addWidget(blue_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_placeholder_style_example(self):
        """占位符文本样式表示例"""
        section_label = QLabel("占位符文本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 自定义占位符文本样式
        placeholder_lineedit = QLineEdit()
        placeholder_lineedit.setPlaceholderText("自定义占位符样式")
        placeholder_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #999999;
                font-style: italic;
            }
        """)
        layout.addWidget(placeholder_lineedit)
        
        # 彩色占位符
        color_placeholder_lineedit = QLineEdit()
        color_placeholder_lineedit.setPlaceholderText("彩色占位符")
        color_placeholder_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #FF9800;
                font-weight: bold;
            }
        """)
        layout.addWidget(color_placeholder_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_password_style_example(self):
        """密码框样式表示例"""
        section_label = QLabel("密码框样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 普通密码框
        password_lineedit = QLineEdit()
        password_lineedit.setEchoMode(QLineEdit.Password)
        password_lineedit.setPlaceholderText("密码")
        password_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        layout.addWidget(password_lineedit)
        
        # 自定义密码符号
        custom_password_lineedit = QLineEdit()
        custom_password_lineedit.setEchoMode(QLineEdit.Password)
        custom_password_lineedit.setPlaceholderText("自定义密码样式")
        custom_password_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFF3E0;
                border: 2px solid #FFCC80;
                border-radius: 4px;
                padding: 5px;
                color: #E65100;
            }
            /* 注意：Qt样式表不直接支持自定义密码符号 */
            /* 实际项目中需要通过子类化QLineEdit实现 */
        """)
        layout.addWidget(custom_password_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 线性渐变输入框
        gradient_lineedit = QLineEdit()
        gradient_lineedit.setPlaceholderText("渐变背景")
        gradient_lineedit.setStyleSheet("""
            QLineEdit {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 0,
                    stop: 0 #E1BEE7,
                    stop: 1 #D1C4E9
                );
                color: #4A148C;
                border: 2px solid #9575CD;
                border-radius: 4px;
                padding: 5px;
                font-weight: bold;
            }
        """)
        layout.addWidget(gradient_lineedit)
        
        # 发光效果输入框
        glow_lineedit = QLineEdit()
        glow_lineedit.setPlaceholderText("发光效果")
        glow_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #4CAF50;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #8BC34A;
                /* Qt样式表不直接支持box-shadow，但可以通过自定义绘制实现 */
                /* 这里使用边框颜色变化模拟发光效果 */
            }
        """)
        layout.addWidget(glow_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_cursor_style_example(self):
        """自定义光标样式表示例"""
        section_label = QLabel("自定义光标样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 自定义光标颜色
        cursor_lineedit = QLineEdit()
        cursor_lineedit.setPlaceholderText("自定义光标颜色")
        cursor_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                /* 通过设置caret-color来自定义光标颜色 */
                caret-color: #F44336;
            }
        """)
        layout.addWidget(cursor_lineedit)
        
        # 大光标输入框
        big_cursor_lineedit = QLineEdit()
        big_cursor_lineedit.setPlaceholderText("大光标")
        big_cursor_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 8px;
                font-size: 16px;
                caret-color: #2196F3;
            }
            /* 注意：Qt样式表不直接支持设置光标宽度 */
            /* 实际项目中需要通过子类化QLineEdit并重写paintEvent实现 */
        """)
        layout.addWidget(big_cursor_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_icon_style_example(self):
        """带图标输入框样式表示例"""
        section_label = QLabel("带图标输入框样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 带左侧图标的输入框
        left_icon_lineedit = QLineEdit()
        left_icon_lineedit.setPlaceholderText("搜索...")
        left_icon_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                padding-left: 30px;  /* 为左侧图标留出空间 */
                background-image: url(:/icons/search.png);  /* 实际项目中使用图标 */
                background-repeat: no-repeat;
                background-position: left center;
                background-origin: content;
            }
            /* 由于没有实际图标文件，这里使用Unicode符号模拟 */
        """)
        # 实际项目中可以使用QAction添加图标
        # action = QAction(self)
        # action.setIcon(QIcon("search.png"))
        # left_icon_lineedit.addAction(action, QLineEdit.LeadingPosition)
        layout.addWidget(left_icon_lineedit)
        
        # 带右侧图标的输入框
        right_icon_lineedit = QLineEdit()
        right_icon_lineedit.setPlaceholderText("带右侧图标")
        right_icon_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                padding-right: 30px;  /* 为右侧图标留出空间 */
            }
        """)
        layout.addWidget(right_icon_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_readonly_style_example(self):
        """只读状态样式表示例"""
        section_label = QLabel("只读状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 只读输入框
        readonly_lineedit = QLineEdit()
        readonly_lineedit.setText("这是只读文本")
        readonly_lineedit.setReadOnly(True)
        readonly_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #F5F5F5;
                color: #757575;
                border: 2px solid #E0E0E0;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:read-only {
                background-color: #F5F5F5;
                color: #9E9E9E;
            }
        """)
        layout.addWidget(readonly_lineedit)
        
        # 禁用输入框
        disabled_lineedit = QLineEdit()
        disabled_lineedit.setText("这是禁用文本")
        disabled_lineedit.setEnabled(False)
        disabled_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FAFAFA;
                color: #BDBDBD;
                border: 2px solid #EEEEEE;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:disabled {
                background-color: #FAFAFA;
                color: #BDBDBD;
            }
        """)
        layout.addWidget(disabled_lineedit)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineEditStylesWindow()
    window.show()
    sys.exit(app.exec())