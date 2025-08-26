#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QComboBox样式表示例
此文件展示了Qt中QComboBox控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QComboBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class ComboBoxStylesWindow(QMainWindow):
    """QComboBox样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComboBox样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QComboBox样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和下拉框示例
        self.create_basic_style_example()
        self.create_editable_style_example()
        self.create_gradient_style_example()
        self.create_custom_arrow_style_example()
        self.create_dropdown_style_example()
        self.create_state_style_example()
        self.create_size_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 默认下拉框
        default_combobox = QComboBox()
        default_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        layout.addWidget(default_combobox)
        
        # 基本样式下拉框
        basic_combobox = QComboBox()
        basic_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        basic_combobox.setStyleSheet("""
            QComboBox {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
                border: 1px solid #388E3C;
                border-radius: 4px;
            }
        """)
        layout.addWidget(basic_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_editable_style_example(self):
        """可编辑下拉框样式表示例"""
        section_label = QLabel("可编辑下拉框样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 可编辑下拉框
        editable_combobox = QComboBox()
        editable_combobox.setEditable(True)
        editable_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        editable_combobox.setStyleSheet("""
            QComboBox {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: 1px solid #1976D2;
                border-radius: 4px;
            }
            QComboBox::edit {
                background-color: #FFFFFF;
                color: #000000;
                selection-background-color: #2196F3;
                selection-color: white;
            }
        """)
        layout.addWidget(editable_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 线性渐变下拉框
        gradient_combobox = QComboBox()
        gradient_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        gradient_combobox.setStyleSheet("""
            QComboBox {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 1, y2: 0,    /* 渐变结束点 */
                    stop: 0 #FF9800, /* 起始颜色 */
                    stop: 1 #E91E63  /* 结束颜色 */
                );
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(gradient_combobox)
        
        # 垂直线性渐变下拉框
        vertical_gradient_combobox = QComboBox()
        vertical_gradient_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        vertical_gradient_combobox.setStyleSheet("""
            QComboBox {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 0, y2: 1,    /* 渐变结束点 */
                    stop: 0 #9C27B0, /* 起始颜色 */
                    stop: 1 #673AB7  /* 结束颜色 */
                );
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(vertical_gradient_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_arrow_style_example(self):
        """自定义箭头样式表示例"""
        section_label = QLabel("自定义箭头样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 自定义箭头下拉框
        custom_arrow_combobox = QComboBox()
        custom_arrow_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        custom_arrow_combobox.setStyleSheet("""
            QComboBox {
                background-color: #FF5722;
                color: white;
                padding: 5px;
                padding-right: 25px;  /* 为箭头留出空间 */
                border: none;
                border-radius: 4px;
            }
            QComboBox::down-arrow {
                image: url(:/icons/down_arrow.png);  /* 实际项目中使用图像 */
                width: 12px;
                height: 12px;
                /* 由于没有实际图像，这里使用颜色模拟 */
                color: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: rgba(255, 255, 255, 0.3);
                border-left-style: solid;
            }
        """)
        layout.addWidget(custom_arrow_combobox)
        
        # 圆形下拉按钮
        round_arrow_combobox = QComboBox()
        round_arrow_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        round_arrow_combobox.setStyleSheet("""
            QComboBox {
                background-color: #009688;
                color: white;
                padding: 5px;
                padding-right: 30px;
                border: none;
                border-radius: 15px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.2);
            }
            QComboBox::down-arrow {
                image: url(:/icons/down_arrow.png);
                width: 10px;
                height: 10px;
                color: white;
            }
        """)
        layout.addWidget(round_arrow_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_dropdown_style_example(self):
        """下拉列表样式表示例"""
        section_label = QLabel("下拉列表样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 自定义下拉列表样式
        dropdown_combobox = QComboBox()
        dropdown_combobox.addItems(["选项 1", "选项 2", "选项 3", "选项 4", "选项 5"])
        dropdown_combobox.setStyleSheet("""
            QComboBox {
                background-color: #607D8B;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
            QComboBox::drop-down {
                border-left: 1px solid rgba(255, 255, 255, 0.3);
            }
            QComboBox::down-arrow {
                color: white;
            }
            QComboBox QAbstractItemView {
                background-color: #455A64;
                color: white;
                border: 1px solid #607D8B;
                selection-background-color: #607D8B;
                selection-color: white;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px 10px;
                height: 30px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #546E7A;
            }
        """)
        layout.addWidget(dropdown_combobox)
        
        # 另一种下拉列表样式
        alternate_dropdown_combobox = QComboBox()
        alternate_dropdown_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        alternate_dropdown_combobox.setStyleSheet("""
            QComboBox {
                background-color: #795548;
                color: white;
                padding: 5px;
                border: 1px solid #6D4C41;
                border-radius: 4px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
            }
            QComboBox QAbstractItemView {
                background-color: #8D6E63;
                color: white;
                border: 1px solid #6D4C41;
                selection-background-color: #5D4037;
            }
        """)
        layout.addWidget(alternate_dropdown_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """状态样式表示例"""
        section_label = QLabel("状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 悬停和选中状态样式
        state_combobox = QComboBox()
        state_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        state_combobox.setStyleSheet("""
            QComboBox {
                background-color: #3F51B5;
                color: white;
                padding: 5px;
                border: 2px solid transparent;
                border-radius: 4px;
            }
            QComboBox:hover {
                border-color: #7986CB;
                background-color: #5C6BC0;
            }
            QComboBox:focus {
                border-color: #2196F3;
                background-color: #3949AB;
            }
            QComboBox:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        layout.addWidget(state_combobox)
        
        # 禁用状态下拉框
        disabled_combobox = QComboBox()
        disabled_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        disabled_combobox.setEnabled(False)
        disabled_combobox.setStyleSheet("""
            QComboBox {
                background-color: #E0E0E0;
                color: #9E9E9E;
                padding: 5px;
                border: 1px solid #BDBDBD;
                border-radius: 4px;
            }
        """)
        layout.addWidget(disabled_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_size_style_example(self):
        """大小和间距样式表示例"""
        section_label = QLabel("大小和间距样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 小号下拉框
        small_combobox = QComboBox()
        small_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        small_combobox.setStyleSheet("""
            QComboBox {
                background-color: #F44336;
                color: white;
                padding: 3px;
                font-size: 12px;
                border: none;
                border-radius: 3px;
            }
        """)
        layout.addWidget(small_combobox)
        
        # 大号下拉框
        large_combobox = QComboBox()
        large_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        large_combobox.setStyleSheet("""
            QComboBox {
                background-color: #00BCD4;
                color: white;
                padding: 8px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
            }
        """)
        layout.addWidget(large_combobox)
        
        # 宽下拉框
        wide_combobox = QComboBox()
        wide_combobox.addItems(["选项 1", "选项 2", "选项 3"])
        wide_combobox.setMinimumWidth(200)
        wide_combobox.setStyleSheet("""
            QComboBox {
                background-color: #8BC34A;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(wide_combobox)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComboBoxStylesWindow()
    window.show()
    sys.exit(app.exec())