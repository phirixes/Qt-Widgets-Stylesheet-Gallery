#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QRadioButton样式表示例
此文件展示了如何自定义Qt中QRadioButton控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QGroupBox
from PySide6.QtGui import QFont

class RadioButtonStylesWindow(QMainWindow):
    """QRadioButton样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QRadioButton样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QRadioButton样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择单选按钮样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本单选按钮", 
            "圆形填充", 
            "方形单选按钮", 
            "霓虹效果",
            "扁平风格",
            "彩色单选按钮",
            "自定义大小",
            "带图标的单选按钮"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_radiobutton_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置选择")
        self.reset_button.clicked.connect(self.reset_selection)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建单选按钮容器
        self.radiobutton_container = QWidget()
        self.radiobutton_layout = QVBoxLayout(self.radiobutton_container)
        self.main_layout.addWidget(self.radiobutton_container)
        
        # 创建各种单选按钮组
        self.create_radiobutton_groups()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本单选按钮
        self.update_radiobutton_style(0)
    
    def create_radiobutton_groups(self):
        """创建各种单选按钮组"""
        # 1. 基本单选按钮组
        basic_group = QGroupBox("1. 基本单选按钮")
        basic_layout = QVBoxLayout(basic_group)
        
        self.basic_radio1 = QRadioButton("选项 1")
        self.basic_radio2 = QRadioButton("选项 2")
        self.basic_radio3 = QRadioButton("选项 3")
        
        basic_layout.addWidget(self.basic_radio1)
        basic_layout.addWidget(self.basic_radio2)
        basic_layout.addWidget(self.basic_radio3)
        
        self.radiobutton_layout.addWidget(basic_group)
        
        # 2. 圆形填充单选按钮组
        filled_group = QGroupBox("2. 圆形填充单选按钮")
        filled_layout = QVBoxLayout(filled_group)
        
        self.filled_radio1 = QRadioButton("选项 A")
        self.filled_radio2 = QRadioButton("选项 B")
        self.filled_radio3 = QRadioButton("选项 C")
        
        filled_layout.addWidget(self.filled_radio1)
        filled_layout.addWidget(self.filled_radio2)
        filled_layout.addWidget(self.filled_radio3)
        
        self.radiobutton_layout.addWidget(filled_group)
        
        # 3. 方形单选按钮组
        square_group = QGroupBox("3. 方形单选按钮")
        square_layout = QVBoxLayout(square_group)
        
        self.square_radio1 = QRadioButton("选项 X")
        self.square_radio2 = QRadioButton("选项 Y")
        self.square_radio3 = QRadioButton("选项 Z")
        
        square_layout.addWidget(self.square_radio1)
        square_layout.addWidget(self.square_radio2)
        square_layout.addWidget(self.square_radio3)
        
        self.radiobutton_layout.addWidget(square_group)
        
        # 4. 霓虹效果单选按钮组
        neon_group = QGroupBox("4. 霓虹效果单选按钮")
        neon_layout = QVBoxLayout(neon_group)
        
        self.neon_radio1 = QRadioButton("选项 一")
        self.neon_radio2 = QRadioButton("选项 二")
        self.neon_radio3 = QRadioButton("选项 三")
        
        neon_layout.addWidget(self.neon_radio1)
        neon_layout.addWidget(self.neon_radio2)
        neon_layout.addWidget(self.neon_radio3)
        
        self.radiobutton_layout.addWidget(neon_group)
        
        # 5. 扁平风格单选按钮组
        flat_group = QGroupBox("5. 扁平风格单选按钮")
        flat_layout = QVBoxLayout(flat_group)
        
        self.flat_radio1 = QRadioButton("选项 α")
        self.flat_radio2 = QRadioButton("选项 β")
        self.flat_radio3 = QRadioButton("选项 γ")
        
        flat_layout.addWidget(self.flat_radio1)
        flat_layout.addWidget(self.flat_radio2)
        flat_layout.addWidget(self.flat_radio3)
        
        self.radiobutton_layout.addWidget(flat_group)
        
        # 6. 彩色单选按钮组
        color_group = QGroupBox("6. 彩色单选按钮")
        color_layout = QVBoxLayout(color_group)
        
        self.color_radio1 = QRadioButton("红色选项")
        self.color_radio2 = QRadioButton("绿色选项")
        self.color_radio3 = QRadioButton("蓝色选项")
        
        color_layout.addWidget(self.color_radio1)
        color_layout.addWidget(self.color_radio2)
        color_layout.addWidget(self.color_radio3)
        
        self.radiobutton_layout.addWidget(color_group)
        
        # 7. 自定义大小单选按钮组
        size_group = QGroupBox("7. 自定义大小单选按钮")
        size_layout = QVBoxLayout(size_group)
        
        self.size_radio1 = QRadioButton("小尺寸")
        self.size_radio2 = QRadioButton("标准尺寸")
        self.size_radio3 = QRadioButton("大尺寸")
        
        size_layout.addWidget(self.size_radio1)
        size_layout.addWidget(self.size_radio2)
        size_layout.addWidget(self.size_radio3)
        
        self.radiobutton_layout.addWidget(size_group)
        
        # 8. 带图标的单选按钮组
        icon_group = QGroupBox("8. 带图标的单选按钮")
        icon_layout = QVBoxLayout(icon_group)
        
        self.icon_radio1 = QRadioButton("图标选项 1")
        self.icon_radio2 = QRadioButton("图标选项 2")
        self.icon_radio3 = QRadioButton("图标选项 3")
        
        icon_layout.addWidget(self.icon_radio1)
        icon_layout.addWidget(self.icon_radio2)
        icon_layout.addWidget(self.icon_radio3)
        
        self.radiobutton_layout.addWidget(icon_group)
        
        # 应用样式
        self.apply_styles()
        
        # 默认隐藏所有单选按钮组
        for i in range(self.radiobutton_layout.count()):
            widget = self.radiobutton_layout.itemAt(i).widget()
            if widget:
                widget.hide()
    
    def apply_styles(self):
        """应用各种单选按钮样式"""
        # 1. 基本单选按钮样式
        basic_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 8px;
                height: 8px;
                border-radius: 4px;
                background-color: white;
                top: 4px;
                left: 4px;
            }
            QRadioButton:hover {
                color: #2196F3;
            }
            QRadioButton:hover::indicator {
                border-color: #2196F3;
            }
        """
        
        self.basic_radio1.setStyleSheet(basic_style)
        self.basic_radio2.setStyleSheet(basic_style)
        self.basic_radio3.setStyleSheet(basic_style)
        
        # 2. 圆形填充单选按钮样式
        filled_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #E0E0E0;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
            QRadioButton::indicator:checked::after {
                content: "✓";
                font-size: 12px;
                color: white;
                position: absolute;
                top: 1px;
                left: 4px;
            }
        """
        
        self.filled_radio1.setStyleSheet(filled_style)
        self.filled_radio2.setStyleSheet(filled_style)
        self.filled_radio3.setStyleSheet(filled_style)
        
        # 3. 方形单选按钮样式
        square_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #FF9800;
                border-radius: 2px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #FF9800;
            }
            QRadioButton::indicator:checked::after {
                content: "✓";
                font-size: 12px;
                color: white;
                position: absolute;
                top: 0px;
                left: 3px;
            }
        """
        
        self.square_radio1.setStyleSheet(square_style)
        self.square_radio2.setStyleSheet(square_style)
        self.square_radio3.setStyleSheet(square_style)
        
        # 4. 霓虹效果单选按钮样式
        neon_style = """
            QRadioButton {
                color: #00BCD4;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #00BCD4;
                border-radius: 10px;
                background-color: #1A1A1A;
            }
            QRadioButton::indicator:checked {
                background-color: #00BCD4;
                box-shadow: 0 0 10px #00BCD4, 0 0 20px #00BCD4;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 10px;
                height: 10px;
                border-radius: 5px;
                background-color: #1A1A1A;
                top: 5px;
                left: 5px;
            }
        """
        
        self.neon_radio1.setStyleSheet(neon_style)
        self.neon_radio2.setStyleSheet(neon_style)
        self.neon_radio3.setStyleSheet(neon_style)
        
        # 5. 扁平风格单选按钮样式
        flat_style = """
            QRadioButton {
                color: #607D8B;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #CFD8DC;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #26C6DA;
                border-color: #26C6DA;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 8px;
                height: 4px;
                background-color: white;
                top: 5px;
                left: 3px;
                border-left: 2px solid white;
                border-bottom: 2px solid white;
                transform: rotate(-45deg);
            }
        """
        
        self.flat_radio1.setStyleSheet(flat_style)
        self.flat_radio2.setStyleSheet(flat_style)
        self.flat_radio3.setStyleSheet(flat_style)
        
        # 6. 彩色单选按钮样式
        # 红色选项
        color_red_style = """
            QRadioButton {
                color: #F44336;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #FFCDD2;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #F44336;
                border-color: #F44336;
            }
        """
        
        # 绿色选项
        color_green_style = """
            QRadioButton {
                color: #4CAF50;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #C8E6C9;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
        """
        
        # 蓝色选项
        color_blue_style = """
            QRadioButton {
                color: #2196F3;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #BBDEFB;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
        """
        
        self.color_radio1.setStyleSheet(color_red_style)
        self.color_radio2.setStyleSheet(color_green_style)
        self.color_radio3.setStyleSheet(color_blue_style)
        
        # 7. 自定义大小单选按钮样式
        # 小尺寸
        small_style = """
            QRadioButton {
                color: #333333;
                font-size: 12px;
                spacing: 4px;
            }
            QRadioButton::indicator {
                width: 12px;
                height: 12px;
                border: 1px solid #CCCCCC;
                border-radius: 6px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
        """
        
        # 标准尺寸
        standard_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
        """
        
        # 大尺寸
        large_style = """
            QRadioButton {
                color: #333333;
                font-size: 16px;
                spacing: 6px;
            }
            QRadioButton::indicator {
                width: 24px;
                height: 24px;
                border: 2px solid #CCCCCC;
                border-radius: 12px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 12px;
                height: 12px;
                border-radius: 6px;
                background-color: white;
                top: 6px;
                left: 6px;
            }
        """
        
        self.size_radio1.setStyleSheet(small_style)
        self.size_radio2.setStyleSheet(standard_style)
        self.size_radio3.setStyleSheet(large_style)
        
        # 8. 带图标的单选按钮样式
        icon_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 8px;
                padding: 3px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #FFC107;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #FFC107;
                border-color: #FFC107;
            }
        """
        
        self.icon_radio1.setStyleSheet(icon_style)
        self.icon_radio2.setStyleSheet(icon_style)
        self.icon_radio3.setStyleSheet(icon_style)
        
        # 为了简化，这里没有实际添加图标，但在实际应用中可以使用以下代码：
        # icon = QIcon("path/to/icon.png")
        # self.icon_radio1.setIcon(icon)
        # self.icon_radio1.setIconSize(QSize(16, 16))
    
    def update_radiobutton_style(self, index):
        """根据选择更新显示的单选按钮组样式"""
        # 隐藏所有单选按钮组
        for i in range(self.radiobutton_layout.count()):
            widget = self.radiobutton_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # 显示选中的单选按钮组
        selected_group = self.radiobutton_layout.itemAt(index).widget()
        if selected_group:
            selected_group.show()
        
        # 更新说明信息
        descriptions = [
            "基本单选按钮使用标准的圆形设计，带有简单的边框和填充效果。",
            "圆形填充单选按钮在选中时显示一个完整的填充效果，并添加了对勾标记。",
            "方形单选按钮使用方形指示器，创造出不同的视觉效果。",
            "霓虹效果单选按钮使用发光效果，创造出科技感十足的界面。",
            "扁平风格单选按钮采用现代扁平设计，简洁清晰。",
            "彩色单选按钮为不同的选项设置不同的颜色，提高视觉区分度。",
            "自定义大小单选按钮展示了如何调整单选按钮的尺寸。",
            "带图标的单选按钮可以在文本前显示自定义图标。"
        ]
        self.info_label.setText(descriptions[index])
    
    def reset_selection(self):
        """重置所有单选按钮的选择状态"""
        # 重置所有单选按钮
        radiobuttons = [
            self.basic_radio1, self.basic_radio2, self.basic_radio3,
            self.filled_radio1, self.filled_radio2, self.filled_radio3,
            self.square_radio1, self.square_radio2, self.square_radio3,
            self.neon_radio1, self.neon_radio2, self.neon_radio3,
            self.flat_radio1, self.flat_radio2, self.flat_radio3,
            self.color_radio1, self.color_radio2, self.color_radio3,
            self.size_radio1, self.size_radio2, self.size_radio3,
            self.icon_radio1, self.icon_radio2, self.icon_radio3
        ]
        
        for radio in radiobuttons:
            radio.setAutoExclusive(False)
            radio.setChecked(False)
            radio.setAutoExclusive(True)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadioButtonStylesWindow()
    window.show()
    sys.exit(app.exec())