#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QSplitter样式表示例
此文件展示了如何自定义Qt中QSplitter控件的各种样式效果。
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
    """QSplitter样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QSplitter样式表示例")
        self.resize(900, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QSplitter样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择分隔器样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本分隔器", 
            "现代分隔器", 
            "虚线分隔器",
            "彩色分隔器",
            "隐藏分隔器",
            "圆形分隔器",
            "渐变分隔器",
            "立体分隔器"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_splitter_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置分隔器")
        self.reset_button.clicked.connect(self.reset_splitter)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建分隔器容器
        self.splitter_container = QWidget()
        self.splitter_layout = QVBoxLayout(self.splitter_container)
        self.splitter_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.splitter_container)
        
        # 创建分隔器
        self.create_splitter()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本分隔器
        self.update_splitter_style(0)
    
    def create_splitter(self):
        """创建分隔器和内容"""
        # 创建主垂直分隔器
        self.main_splitter = QSplitter(Qt.Vertical)
        
        # 创建顶部水平分隔器
        self.top_splitter = QSplitter(Qt.Horizontal)
        
        # 创建左侧和右侧面板
        self.left_panel = self._create_panel("左侧面板")
        self.right_panel = self._create_panel("右侧面板")
        
        # 添加到顶部水平分隔器
        self.top_splitter.addWidget(self.left_panel)
        self.top_splitter.addWidget(self.right_panel)
        self.top_splitter.setSizes([300, 400])  # 设置初始大小比例
        
        # 创建底部面板
        self.bottom_panel = self._create_panel("底部面板")
        
        # 添加到主垂直分隔器
        self.main_splitter.addWidget(self.top_splitter)
        self.main_splitter.addWidget(self.bottom_panel)
        self.main_splitter.setSizes([400, 200])  # 设置初始大小比例
        
        # 添加主分隔器到布局
        self.splitter_layout.addWidget(self.main_splitter)
    
    def _create_panel(self, title):
        """创建面板"""
        # 创建面板框架
        panel = QFrame()
        panel.setFrameShape(QFrame.StyledPanel)
        panel.setMinimumSize(200, 100)  # 设置最小尺寸
        
        # 创建布局
        panel_layout = QVBoxLayout(panel)
        
        # 添加标题
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        panel_layout.addWidget(title_label)
        
        # 添加内容区域
        content_text = QTextEdit()
        content_text.setReadOnly(True)
        content_text.setPlaceholderText(f"这是{title}的内容区域")
        panel_layout.addWidget(content_text)
        
        return panel
    
    def update_splitter_style(self, index):
        """根据选择更新分隔器样式"""
        # 清除之前的样式
        self.main_splitter.setStyleSheet("")
        self.top_splitter.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本分隔器样式
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
            self.info_label.setText("基本分隔器样式：简单的灰色分隔器，悬停和点击时有不同的背景色。")
        
        elif index == 1:
            # 现代分隔器样式
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
            self.info_label.setText("现代分隔器样式：更细的分隔器，带有圆角，并且只在中间部分显示。")
        
        elif index == 2:
            # 虚线分隔器样式
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
            self.info_label.setText("虚线分隔器样式：使用虚线边框而不是填充背景色，提供更轻量的视觉效果。")
        
        elif index == 3:
            # 彩色分隔器样式
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
            self.info_label.setText("彩色分隔器样式：为垂直和水平分隔器设置不同的颜色，使界面更加生动。")
        
        elif index == 4:
            # 隐藏分隔器样式
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
            self.info_label.setText("隐藏分隔器样式：默认不可见，只有在鼠标悬停或拖动时才显示。")
        
        elif index == 5:
            # 圆形分隔器样式
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
            self.info_label.setText("圆形分隔器样式：使用圆形的分隔器把手，看起来像一个可拖动的按钮。")
        
        elif index == 6:
            # 渐变分隔器样式
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
            self.info_label.setText("渐变分隔器样式：使用渐变效果增强分隔器的视觉吸引力。")
        
        elif index == 7:
            # 立体分隔器样式
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
            self.info_label.setText("立体分隔器样式：使用边框阴影创建立体感，拖动时边框效果会反转。")
    
    def reset_splitter(self):
        """重置分隔器样式和位置"""
        # 重置分隔器位置
        self.top_splitter.setSizes([300, 400])
        self.main_splitter.setSizes([400, 200])
        
        # 恢复默认样式
        self.update_splitter_style(self.style_combobox.currentIndex())

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitterStylesWindow()
    window.show()
    sys.exit(app.exec())