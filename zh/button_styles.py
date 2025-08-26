#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QPushButton样式表示例
此文件展示了Qt中QPushButton控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class ButtonStylesWindow(QMainWindow):
    """QPushButton样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPushButton样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QPushButton样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和按钮示例
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_gradient_style_example()
        self.create_bordered_style_example()
        self.create_icon_style_example()
        self.create_custom_shapes_example()
        self.create_disabled_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 基本按钮样式
        basic_button = QPushButton("基本样式")
        basic_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  # 背景颜色
                color: white;              # 文本颜色
                padding: 10px 20px;        # 内边距（上下 左右）
                font-size: 14px;           # 字体大小
                font-weight: normal;       # 字体粗细
            }
        """)
        layout.addWidget(basic_button)
        
        # 不同颜色按钮
        red_button = QPushButton("红色按钮")
        red_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;  # 红色背景
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(red_button)
        
        blue_button = QPushButton("蓝色按钮")
        blue_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;  # 蓝色背景
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(blue_button)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """按钮状态样式表示例（正常、悬停、按下）"""
        section_label = QLabel("按钮状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 带状态的按钮
        state_button = QPushButton("悬停和按下效果")
        state_button.setStyleSheet("""
            QPushButton {               /* 正常状态 */
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;            /* 无边框 */
                font-size: 14px;
            }
            QPushButton:hover {         /* 悬停状态 */
                background-color: #5CBF60;
                font-weight: bold;       /* 悬停时加粗 */
            }
            QPushButton:pressed {       /* 按下状态 */
                background-color: #3D8B40;
                padding-left: 12px;      /* 按下时轻微位移 */
                padding-top: 12px;
            }
        """)
        layout.addWidget(state_button)
        
        # 带有边框状态变化的按钮
        border_state_button = QPushButton("边框状态变化")
        border_state_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border: 2px solid #1976D2;  /* 正常边框 */
            }
            QPushButton:hover {
                border-color: #BBDEFB;      /* 悬停时边框颜色变化 */
                border-width: 3px;          /* 悬停时边框变宽 */
            }
            QPushButton:pressed {
                border-color: #0D47A1;      /* 按下时边框颜色变化 */
            }
        """)
        layout.addWidget(border_state_button)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 线性渐变按钮
        linear_gradient_button = QPushButton("线性渐变")
        linear_gradient_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* 渐变起始点 */
                    x2: 1, y2: 0,    /* 渐变结束点 */
                    stop: 0 #4CAF50, /* 起始颜色 */
                    stop: 1 #8BC34A  /* 结束颜色 */
                );
                color: white;
                padding: 10px 20px;
                border: none;
            }
        """)
        layout.addWidget(linear_gradient_button)
        
        # 辐射渐变按钮
        radial_gradient_button = QPushButton("辐射渐变")
        radial_gradient_button.setStyleSheet("""
            QPushButton {
                background: qradialgradient(
                    cx: 0.5, cy: 0.5,    /* 中心点 */
                    radius: 0.5,         /* 半径 */
                    fx: 0.5, fy: 0.5,    /* 焦点 */
                    stop: 0 #FF5722,     /* 中心颜色 */
                    stop: 1 #E64A19      /* 边缘颜色 */
                );
                color: white;
                padding: 10px 20px;
                border: none;
            }
        """)
        layout.addWidget(radial_gradient_button)
        
        self.main_layout.addLayout(layout)
    
    def create_bordered_style_example(self):
        """边框样式表示例"""
        section_label = QLabel("边框样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 圆角按钮
        rounded_button = QPushButton("圆角按钮")
        rounded_button.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                padding: 10px 20px;
                border-radius: 15px;     /* 圆角半径 */
                border: 2px solid #7B1FA2;
            }
        """)
        layout.addWidget(rounded_button)
        
        # 虚线边框按钮
        dashed_button = QPushButton("虚线边框")
        dashed_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                border: 2px dashed #E65100;  /* 虚线边框 */
            }
        """)
        layout.addWidget(dashed_button)
        
        # 双线边框按钮
        double_border_button = QPushButton("双线边框")
        double_border_button.setStyleSheet("""
            QPushButton {
                background-color: #00BCD4;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                border: 2px solid #006064;
                /* 用伪元素实现双线边框效果 */
                border-style: outset;
            }
        """)
        layout.addWidget(double_border_button)
        
        self.main_layout.addLayout(layout)
    
    def create_icon_style_example(self):
        """图标按钮样式表示例"""
        section_label = QLabel("图标按钮样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 带图标的按钮（这里使用Unicode符号代替实际图标）
        icon_button = QPushButton("🔍 搜索")
        icon_button.setStyleSheet("""
            QPushButton {
                background-color: #607D8B;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: left;         /* 文本左对齐 */
                padding-left: 30px;       /* 左侧留出图标空间 */
            }
            /* 注意：实际项目中，建议使用QIcon设置图标，而不是依赖Unicode符号 */
        """)
        layout.addWidget(icon_button)
        
        # 图标和文本分离的按钮
        split_button = QPushButton("详细信息 ⋯")
        split_button.setStyleSheet("""
            QPushButton {
                background-color: #3F51B5;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: left;         /* 文本左对齐 */
            }
        """)
        layout.addWidget(split_button)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_shapes_example(self):
        """自定义形状按钮样式表示例"""
        section_label = QLabel("自定义形状")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 圆形按钮
        circle_button = QPushButton("+")
        circle_button.setFixedSize(50, 50)  # 设置固定大小使按钮成为圆形
        circle_button.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 25px;      /* 半径为宽度的一半 */
                border: none;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
            QPushButton:pressed {
                background-color: #B71C1C;
            }
        """)
        layout.addWidget(circle_button)
        
        # 胶囊形状按钮
        capsule_button = QPushButton("胶囊形状")
        capsule_button.setStyleSheet("""
            QPushButton {
                background-color: #009688;
                color: white;
                padding: 8px 25px;
                border-radius: 20px;      /* 较大的圆角 */
                border: none;
            }
        """)
        layout.addWidget(capsule_button)
        
        self.main_layout.addLayout(layout)
    
    def create_disabled_style_example(self):
        """禁用状态样式表示例"""
        section_label = QLabel("禁用状态样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 正常按钮和禁用按钮对比
        enabled_button = QPushButton("可用按钮")
        enabled_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(enabled_button)
        
        disabled_button = QPushButton("禁用按钮")
        disabled_button.setEnabled(False)  # 设置为禁用状态
        disabled_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;  /* 禁用时背景色 */
                color: #757575;             /* 禁用时文字颜色 */
                opacity: 0.6;               /* 透明度 */
            }
        """)
        layout.addWidget(disabled_button)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonStylesWindow()
    window.show()
    sys.exit(app.exec())