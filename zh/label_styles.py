#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QLabel样式表示例
此文件展示了Qt中QLabel控件的各种样式表用法，每种样式都有详细注释说明。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QGridLayout
)
from PySide6.QtGui import QFont, QColor

class LabelStylesWindow(QMainWindow):
    """QLabel样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLabel样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QLabel样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建样式表说明和标签示例
        self.create_basic_style_example()
        self.create_font_style_example()
        self.create_background_style_example()
        self.create_border_style_example()
        self.create_shadow_style_example()
        self.create_gradient_style_example()
        self.create_html_style_example()
        self.create_image_style_example()
    
    def create_basic_style_example(self):
        """基本样式表示例"""
        section_label = QLabel("基本样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 默认标签
        default_label = QLabel("默认标签")
        layout.addWidget(default_label)
        
        # 文本颜色标签
        color_label = QLabel("红色文本")
        color_label.setStyleSheet("color: #f44336;")
        layout.addWidget(color_label)
        
        # 背景颜色标签
        bg_color_label = QLabel("蓝色背景")
        bg_color_label.setStyleSheet("background-color: #2196F3; color: white;")
        layout.addWidget(bg_color_label)
        
        self.main_layout.addLayout(layout)
    
    def create_font_style_example(self):
        """字体样式表示例"""
        section_label = QLabel("字体样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QGridLayout()
        
        # 不同字体大小
        small_font_label = QLabel("小字体")
        small_font_label.setStyleSheet("font-size: 10px;")
        layout.addWidget(small_font_label, 0, 0)
        
        medium_font_label = QLabel("中字体")
        medium_font_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(medium_font_label, 0, 1)
        
        large_font_label = QLabel("大字体")
        large_font_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(large_font_label, 0, 2)
        
        # 不同字体粗细
        normal_label = QLabel("正常粗细")
        layout.addWidget(normal_label, 1, 0)
        
        bold_label = QLabel("粗体")
        bold_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(bold_label, 1, 1)
        
        italic_label = QLabel("斜体")
        italic_label.setStyleSheet("font-style: italic;")
        layout.addWidget(italic_label, 1, 2)
        
        # 不同字体系列
        serif_label = QLabel("衬线字体")
        serif_label.setStyleSheet("font-family: 'Times New Roman', serif;")
        layout.addWidget(serif_label, 2, 0)
        
        sans_serif_label = QLabel("无衬线字体")
        sans_serif_label.setStyleSheet("font-family: Arial, sans-serif;")
        layout.addWidget(sans_serif_label, 2, 1)
        
        monospace_label = QLabel("等宽字体")
        monospace_label.setStyleSheet("font-family: 'Courier New', monospace;")
        layout.addWidget(monospace_label, 2, 2)
        
        self.main_layout.addLayout(layout)
    
    def create_background_style_example(self):
        """背景样式表示例"""
        section_label = QLabel("背景样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 带内边距的标签
        padding_label = QLabel("带内边距的标签")
        padding_label.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 15px;  /* 上下左右内边距 */
        """)
        layout.addWidget(padding_label)
        
        # 不同内边距的标签
        different_padding_label = QLabel("不同内边距")
        different_padding_label.setStyleSheet("""
            background-color: #FF9800;
            color: white;
            padding-top: 5px;
            padding-right: 15px;
            padding-bottom: 10px;
            padding-left: 20px;
        """)
        layout.addWidget(different_padding_label)
        
        self.main_layout.addLayout(layout)
    
    def create_border_style_example(self):
        """边框样式表示例"""
        section_label = QLabel("边框样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 实线边框标签
        solid_border_label = QLabel("实线边框")
        solid_border_label.setStyleSheet("""
            border: 2px solid #2196F3;
            padding: 10px;
        """)
        layout.addWidget(solid_border_label)
        
        # 虚线边框标签
        dashed_border_label = QLabel("虚线边框")
        dashed_border_label.setStyleSheet("""
            border: 2px dashed #f44336;
            padding: 10px;
        """)
        layout.addWidget(dashed_border_label)
        
        # 圆角边框标签
        rounded_label = QLabel("圆角边框")
        rounded_label.setStyleSheet("""
            background-color: #9C27B0;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(rounded_label)
        
        # 无边框但有背景色的标签
        no_border_label = QLabel("无边框背景")
        no_border_label.setStyleSheet("""
            background-color: #FFEB3B;
            color: #333;
            padding: 10px;
        """)
        layout.addWidget(no_border_label)
        
        self.main_layout.addLayout(layout)
    
    def create_shadow_style_example(self):
        """阴影效果样式表示例"""
        section_label = QLabel("阴影效果")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 文本阴影标签
        text_shadow_label = QLabel("文本阴影")
        text_shadow_label.setStyleSheet("""
            color: white;
            background-color: #3F51B5;
            padding: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* 水平偏移、垂直偏移、模糊半径、颜色 */
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(text_shadow_label)
        
        # 箱体阴影标签
        box_shadow_label = QLabel("箱体阴影")
        box_shadow_label.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            /* 注意：Qt样式表不直接支持box-shadow，但可以通过QFrame的阴影属性或自定义绘制实现类似效果 */
            /* 这里使用边框颜色模拟简单的阴影效果 */
            border: 1px solid rgba(0, 0, 0, 0.2);
        """)
        layout.addWidget(box_shadow_label)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """渐变背景样式表示例"""
        section_label = QLabel("渐变背景")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 水平线性渐变标签
        horizontal_gradient_label = QLabel("水平渐变")
        horizontal_gradient_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0,    /* 渐变起始点 */
                x2: 1, y2: 0,    /* 渐变结束点 */
                stop: 0 #FF9800, /* 起始颜色 */
                stop: 1 #E91E63  /* 结束颜色 */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(horizontal_gradient_label)
        
        # 垂直线性渐变标签
        vertical_gradient_label = QLabel("垂直渐变")
        vertical_gradient_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0,    /* 渐变起始点 */
                x2: 0, y2: 1,    /* 渐变结束点 */
                stop: 0 #2196F3, /* 起始颜色 */
                stop: 1 #00BCD4  /* 结束颜色 */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(vertical_gradient_label)
        
        # 辐射渐变标签
        radial_gradient_label = QLabel("辐射渐变")
        radial_gradient_label.setStyleSheet("""
            background: qradialgradient(
                cx: 0.5, cy: 0.5,    /* 中心点 */
                radius: 0.5,         /* 半径 */
                fx: 0.5, fy: 0.5,    /* 焦点 */
                stop: 0 #9C27B0,     /* 中心颜色 */
                stop: 1 #673AB7      /* 边缘颜色 */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(radial_gradient_label)
        
        self.main_layout.addLayout(layout)
    
    def create_html_style_example(self):
        """HTML样式表示例"""
        section_label = QLabel("HTML样式")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QVBoxLayout()
        
        # 带HTML标签的文本
        html_label = QLabel()
        html_label.setText("""
            <html>
            <head></head>
            <body>
                <p>这是一个<strong>粗体</strong>文本，这是<em>斜体</em>文本，这是<u>下划线</u>文本。</p>
                <p><font color="#f44336">红色</font>、<font color="#2196F3">蓝色</font>、<font color="#4CAF50">绿色</font>文本。</p>
                <p><font size="5">大字体</font>和<font size="2">小字体</font>。</p>
            </body>
            </html>
        """)
        html_label.setStyleSheet("padding: 10px;")
        layout.addWidget(html_label)
        
        # 结合样式表和HTML
        mixed_label = QLabel()
        mixed_label.setText("<html><body><p>样式表 + HTML</p></body></html>")
        mixed_label.setStyleSheet("""
            background-color: #00BCD4;
            color: white;
            padding: 10px;
            font-size: 18px;
        """)
        layout.addWidget(mixed_label)
        
        self.main_layout.addLayout(layout)
    
    def create_image_style_example(self):
        """图像样式表示例"""
        section_label = QLabel("图像背景")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # 带图像背景的标签
        # 注意：由于我们没有实际的图像文件，这里使用渐变来模拟
        # 实际项目中可以使用background-image属性设置图像背景
        image_bg_label = QLabel("带背景图的标签")
        image_bg_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #FFC107, stop: 1 #FF5722
            );
            color: white;
            padding: 20px;
            font-weight: bold;
            /* 实际项目中使用下面的代码设置图像背景 */
            /* background-image: url('path/to/image.png'); */
            /* background-repeat: no-repeat; */
            /* background-position: center; */
        """)
        layout.addWidget(image_bg_label)
        
        # 半透明背景标签
        transparent_label = QLabel("半透明背景")
        transparent_label.setStyleSheet("""
            background-color: rgba(0, 150, 136, 0.5);  /* RGBA颜色，最后一个参数是透明度 */
            color: white;
            padding: 20px;
            border: 2px solid #009688;
        """)
        layout.addWidget(transparent_label)
        
        self.main_layout.addLayout(layout)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabelStylesWindow()
    window.show()
    sys.exit(app.exec())