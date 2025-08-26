#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QTextEdit样式表示例
此文件展示了如何自定义Qt中QTextEdit控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QGroupBox
from PySide6.QtGui import QFont

class TextEditStylesWindow(QMainWindow):
    """QTextEdit样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTextEdit样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QTextEdit样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择文本编辑框样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本文本框", 
            "代码编辑器", 
            "富文本编辑器", 
            "笔记本风格",
            "纸质风格",
            "暗色主题",
            "只读文档",
            "带行号的编辑器"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_textedit_style)
        
        # 功能按钮
        self.apply_button = QPushButton("应用样式")
        self.apply_button.clicked.connect(lambda: self.update_textedit_style(self.style_combobox.currentIndex()))
        self.reset_button = QPushButton("重置")
        self.reset_button.clicked.connect(self.reset_textedit)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.apply_button)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建文本编辑框容器
        self.textedit_container = QWidget()
        self.textedit_layout = QVBoxLayout(self.textedit_container)
        self.main_layout.addWidget(self.textedit_container)
        
        # 创建各种文本编辑框
        self.create_textedits()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本文本框
        self.update_textedit_style(0)
    
    def create_textedits(self):
        """创建各种文本编辑框"""
        # 基本文本框
        self.basic_textedit = QTextEdit()
        self.basic_textedit.setPlaceholderText("这是一个基本文本编辑框...")
        self.basic_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("1. 基本文本框"))
        self.textedit_layout.addWidget(self.basic_textedit)
        
        # 代码编辑器
        self.code_textedit = QTextEdit()
        self.code_textedit.setPlaceholderText("// 这是一个代码编辑器\nprint('Hello, World!')")
        self.code_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("2. 代码编辑器"))
        self.textedit_layout.addWidget(self.code_textedit)
        
        # 富文本编辑器
        self.rich_textedit = QTextEdit()
        self.rich_textedit.setPlaceholderText("这是一个富文本编辑器...")
        self.rich_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("3. 富文本编辑器"))
        self.textedit_layout.addWidget(self.rich_textedit)
        
        # 笔记本风格
        self.notebook_textedit = QTextEdit()
        self.notebook_textedit.setPlaceholderText("这是一个笔记本风格的文本编辑器...")
        self.notebook_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("4. 笔记本风格"))
        self.textedit_layout.addWidget(self.notebook_textedit)
        
        # 纸质风格
        self.paper_textedit = QTextEdit()
        self.paper_textedit.setPlaceholderText("这是一个纸质风格的文本编辑器...")
        self.paper_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("5. 纸质风格"))
        self.textedit_layout.addWidget(self.paper_textedit)
        
        # 暗色主题
        self.dark_textedit = QTextEdit()
        self.dark_textedit.setPlaceholderText("这是一个暗色主题的文本编辑器...")
        self.dark_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("6. 暗色主题"))
        self.textedit_layout.addWidget(self.dark_textedit)
        
        # 只读文档
        self.readonly_textedit = QTextEdit()
        self.readonly_textedit.setReadOnly(True)
        self.readonly_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("7. 只读文档"))
        self.textedit_layout.addWidget(self.readonly_textedit)
        
        # 带行号的编辑器（模拟）
        self.linenumber_textedit = QTextEdit()
        self.linenumber_textedit.setPlaceholderText("1: 这是一个带行号的编辑器\n2: 第二行\n3: 第三行")
        self.linenumber_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("8. 带行号的编辑器（模拟）"))
        self.textedit_layout.addWidget(self.linenumber_textedit)
        
        # 应用样式
        self.apply_styles()
        
        # 默认隐藏所有文本编辑框
        for i in range(1, self.textedit_layout.count()):
            widget = self.textedit_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # 设置只读文档内容
        self.readonly_textedit.setHtml("""
        <h2>只读文档示例</h2>
        <p>这是一个只读文档的示例。在Qt中，你可以通过设置QTextEdit的setReadOnly(True)方法来创建一个只读文档。</p>
        <h3>只读文档的特点：</h3>
        <ul>
            <li>用户无法编辑文档内容</li>
            <li>可以设置特殊的样式以区分普通可编辑文档</li>
            <li>仍然可以选择和复制文本</li>
        </ul>
        <p>你可以使用CSS样式来自定义只读文档的外观，例如更改背景色、文字颜色、字体等。</p>
        """)
    
    def apply_styles(self):
        """应用各种文本编辑框样式"""
        # 1. 基本文本框样式
        self.basic_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                background-color: #FAFAFA;
                outline: none;
            }
        """)
        
        # 2. 代码编辑器样式
        code_font = QFont()
        code_font.setFamily("Consolas")
        code_font.setStyleHint(QFont.Monospace)
        code_font.setFixedPitch(True)
        code_font.setPointSize(10)
        self.code_textedit.setFont(code_font)
        
        self.code_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #2D2D2D;
                color: #D4D4D4;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                line-height: 1.4;
            }
            QTextEdit:hover {
                border-color: #666666;
            }
            QTextEdit:focus {
                border-color: #007ACC;
                background-color: #2D2D2D;
                outline: none;
            }
        """)
        
        # 3. 富文本编辑器样式
        self.rich_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
                selection-background-color: #2196F3;
                selection-color: white;
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                outline: none;
            }
        """)
        
        # 4. 笔记本风格样式
        self.notebook_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #FFFBE6;
                color: #333333;
                border: 1px solid #FFD700;
                border-radius: 4px;
                padding: 15px;
                font-family: 'SimSun', '宋体', serif;
                font-size: 14px;
                line-height: 1.6;
                background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSIxMDAiIHkyPSIwIiBzdHJva2U9IiNmZmQ3MDAiIHN0cm9rZS13aWR0aD0iMC41Ii8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3BhdHRlcm4pIiAvPjwvc3ZnPg==);
            }
            QTextEdit:hover {
                border-color: #FFA500;
            }
            QTextEdit:focus {
                border-color: #FFA500;
                background-color: #FFF8E1;
                outline: none;
            }
        """)
        
        # 5. 纸质风格样式
        self.paper_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 20px;
                font-family: 'SimSun', '宋体', serif;
                font-size: 14px;
                line-height: 1.8;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSIxMDAiIHkyPSIwIiBzdHJva2U9IiNmNWY1ZjUiIHN0cm9rZS13aWR0aD0iMC41Ii8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3BhdHRlcm4pIiAvPjwvc3ZnPg==);
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                box-shadow: 0 2px 15px rgba(33, 150, 243, 0.2);
                outline: none;
            }
        """)
        
        # 6. 暗色主题样式
        self.dark_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #D4D4D4;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                selection-background-color: #007ACC;
                selection-color: white;
            }
            QTextEdit:hover {
                border-color: #666666;
            }
            QTextEdit:focus {
                border-color: #007ACC;
                outline: none;
            }
        """)
        
        # 7. 只读文档样式
        self.readonly_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #F5F5F5;
                color: #666666;
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
            }
            QTextEdit QScrollBar:vertical {
                background-color: #F5F5F5;
                width: 10px;
            }
            QTextEdit QScrollBar::handle:vertical {
                background-color: #BDBDBD;
                border-radius: 5px;
            }
            QTextEdit QScrollBar::handle:vertical:hover {
                background-color: #9E9E9E;
            }
        """)
        
        # 8. 带行号的编辑器样式（模拟）
        self.linenumber_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #F7F7F7;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 10px 10px 10px 40px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                line-height: 1.4;
                background-image: 
                    linear-gradient(to right, #E0E0E0 0px, #E0E0E0 30px, transparent 30px),
                    url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIzMCIgeT0iMCIgd2lkdGg9IjcwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSI3MCIgeTI9IjAiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIwLjUiLz48L3BhdHRlcm4+PC9kZWZzPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9InVybCgjcGF0dGVybikiIC8+PC9zdmc+);
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                background-color: #F5F5F5;
                outline: none;
            }
        """)
    
    def update_textedit_style(self, index):
        """根据选择更新显示的文本编辑框样式"""
        # 隐藏所有文本编辑框
        for i in range(1, self.textedit_layout.count()):
            widget = self.textedit_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # 显示选中的文本编辑框
        textedits = [
            self.basic_textedit,
            self.code_textedit,
            self.rich_textedit,
            self.notebook_textedit,
            self.paper_textedit,
            self.dark_textedit,
            self.readonly_textedit,
            self.linenumber_textedit
        ]
        
        # 显示对应的标签和文本编辑框
        self.textedit_layout.itemAt(index * 2).widget().show()  # 显示标签
        textedits[index].show()  # 显示文本编辑框
        
        # 更新说明信息
        descriptions = [
            "基本文本框使用简洁的设计，适合大多数普通文本输入场景。",
            "代码编辑器使用等宽字体和暗色主题，适合编程和代码编辑。",
            "富文本编辑器优化了富文本显示和编辑，支持HTML格式。",
            "笔记本风格使用黄色背景和模拟线条，创造纸质笔记本的感觉。",
            "纸质风格通过阴影和质感创造出真实纸张的效果。",
            "暗色主题适合长时间阅读和编辑，减轻眼睛疲劳。",
            "只读文档样式适用于展示不可编辑的内容。",
            "带行号的编辑器（模拟）展示了如何创建类似IDE的编辑环境。"
        ]
        self.info_label.setText(descriptions[index])
    
    def reset_textedit(self):
        """重置文本编辑框"""
        # 清空所有文本编辑框内容
        textedits = [
            self.basic_textedit,
            self.code_textedit,
            self.rich_textedit,
            self.notebook_textedit,
            self.paper_textedit,
            self.dark_textedit,
            # 不重置只读文档
            self.linenumber_textedit
        ]
        
        for textedit in textedits:
            textedit.clear()

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditStylesWindow()
    window.show()
    sys.exit(app.exec())