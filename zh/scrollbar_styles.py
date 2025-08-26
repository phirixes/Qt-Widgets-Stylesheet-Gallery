#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QScrollBar样式表示例
此文件展示了如何自定义Qt中QScrollBar控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QFrame
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class ScrollBarStylesWindow(QMainWindow):
    """QScrollBar样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QScrollBar样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QScrollBar样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择滚动条样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本滚动条", 
            "现代滚动条", 
            "超薄滚动条",
            "圆形滚动条",
            "彩色滚动条",
            "深色主题滚动条",
            "隐藏式滚动条",
            "渐变滚动条"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_scrollbar_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置滚动条")
        self.reset_button.clicked.connect(self.reset_scrollbar)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建滚动区域
        self.create_scroll_area()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本滚动条
        self.update_scrollbar_style(0)
    
    def create_scroll_area(self):
        """创建滚动区域和内容"""
        # 创建滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        # 创建滚动区域的内容
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        
        # 添加足够多的内容以激活滚动条
        for i in range(20):
            # 创建一个框架作为内容项
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setMinimumHeight(80)
            frame.setMaximumWidth(700)
            
            # 设置标签显示内容
            label = QLabel(f"滚动内容示例 #{i+1}")
            label.setStyleSheet("font-size: 16px; margin: 20px;")
            label.setAlignment(Qt.AlignCenter)
            
            # 添加到框架中
            frame_layout = QVBoxLayout(frame)
            frame_layout.addWidget(label)
            
            # 添加到内容布局
            self.content_layout.addWidget(frame)
        
        # 创建水平内容
        horizontal_content = QWidget()
        horizontal_layout = QHBoxLayout(horizontal_content)
        horizontal_layout.setContentsMargins(20, 20, 20, 20)
        
        for i in range(15):
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setMinimumWidth(100)
            frame.setMinimumHeight(100)
            
            label = QLabel(f"{i+1}")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 16px;")
            
            frame_layout = QVBoxLayout(frame)
            frame_layout.addWidget(label)
            
            horizontal_layout.addWidget(frame)
        
        self.content_layout.addWidget(horizontal_content)
        
        # 设置滚动区域的内容
        self.scroll_area.setWidget(content_widget)
        
        # 添加滚动区域到主布局
        self.main_layout.addWidget(self.scroll_area)
    
    def update_scrollbar_style(self, index):
        """根据选择更新滚动条样式"""
        # 清除之前的样式
        self.scroll_area.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #CCCCCC;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: #F5F5F5;
                    width: 12px;
                    margin: 0;
                }
                QScrollBar::handle:vertical {
                    background: #CCCCCC;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #BBBBBB;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #AAAAAA;
                }
                QScrollBar::sub-line:vertical {
                    background: none;
                }
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: #F5F5F5;
                    height: 12px;
                    margin: 0;
                }
                QScrollBar::handle:horizontal {
                    background: #CCCCCC;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #BBBBBB;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #AAAAAA;
                }
                QScrollBar::sub-line:horizontal {
                    background: none;
                }
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("基本滚动条样式：简单的灰色滚动条，没有箭头按钮，提供基本的滚动功能。")
        
        elif index == 1:
            # 现代滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: white;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: #FAFAFA;
                    width: 8px;
                    margin: 2px;
                    border-radius: 4px;
                }
                QScrollBar::handle:vertical {
                    background: #CCCCCC;
                    border-radius: 4px;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #AAAAAA;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: #FAFAFA;
                    height: 8px;
                    margin: 2px;
                    border-radius: 4px;
                }
                QScrollBar::handle:horizontal {
                    background: #CCCCCC;
                    border-radius: 4px;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #AAAAAA;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("现代滚动条样式：更窄的滚动条，带有圆角，悬停和点击时有不同的背景色。")
        
        elif index == 2:
            # 超薄滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: none;
                    background-color: white;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: transparent;
                    width: 4px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical {
                    background: #BBBBBB;
                    border-radius: 2px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #888888;
                    width: 6px;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #555555;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 4px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal {
                    background: #BBBBBB;
                    border-radius: 2px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #888888;
                    height: 6px;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #555555;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("超薄滚动条样式：非常细的滚动条，悬停时会变粗，几乎不可见，适合极简界面。")
        
        elif index == 3:
            # 圆形滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: #FAFAFA;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: transparent;
                    width: 20px;
                    margin: 5px;
                }
                QScrollBar::handle:vertical {
                    background: #4CAF50;
                    border-radius: 10px;
                    min-height: 40px;
                    width: 16px;
                    margin: 2px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #45A049;
                    width: 18px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #388E3C;
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: #4CAF50;
                    width: 16px;
                    height: 16px;
                    margin: 2px;
                    border-radius: 8px;
                }
                QScrollBar::sub-line:vertical:hover,
                QScrollBar::add-line:vertical:hover {
                    background: #45A049;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: transparent;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 20px;
                    margin: 5px;
                }
                QScrollBar::handle:horizontal {
                    background: #2196F3;
                    border-radius: 10px;
                    min-width: 40px;
                    height: 16px;
                    margin: 2px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #0B7dda;
                    height: 18px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #0d47a1;
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: #2196F3;
                    width: 16px;
                    height: 16px;
                    margin: 2px;
                    border-radius: 8px;
                }
                QScrollBar::sub-line:horizontal:hover,
                QScrollBar::add-line:horizontal:hover {
                    background: #0B7dda;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: transparent;
                }
            """)
            self.info_label.setText("圆形滚动条样式：使用圆形的滚动条和按钮，呈现友好的视觉效果。")
        
        elif index == 4:
            # 彩色滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #EEEEEE;
                    background-color: white;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: #F9F9F9;
                    width: 14px;
                    margin: 2px;
                    border-radius: 7px;
                }
                QScrollBar::handle:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF5722, stop:1 #E91E63);
                    border-radius: 7px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #FF7043, stop:1 #F06292);
                }
                QScrollBar::handle:vertical:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #E64A19, stop:1 #C2185B);
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: #F9F9F9;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow.png);
                }
                QScrollBar::sub-page:vertical {
                    background: #FFF3E0;
                    border-radius: 7px;
                }
                QScrollBar::add-page:vertical {
                    background: #F3E5F5;
                    border-radius: 7px;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: #F9F9F9;
                    height: 14px;
                    margin: 2px;
                    border-radius: 7px;
                }
                QScrollBar::handle:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #2196F3, stop:1 #00BCD4);
                    border-radius: 7px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #42A5F5, stop:1 #26C6DA);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1976D2, stop:1 #00ACC1);
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: #F9F9F9;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow.png);
                }
                QScrollBar::sub-page:horizontal {
                    background: #E0F7FA;
                    border-radius: 7px;
                }
                QScrollBar::add-page:horizontal {
                    background: #E8F5E9;
                    border-radius: 7px;
                }
            """)
            self.info_label.setText("彩色滚动条样式：使用渐变背景和彩色区域，使滚动条更加醒目。")
        
        elif index == 5:
            # 深色主题滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #444444;
                    background-color: #2C2C2C;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: #3C3C3C;
                    width: 14px;
                    margin: 2px;
                }
                QScrollBar::handle:vertical {
                    background: #666666;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #777777;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:vertical {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::add-line:vertical {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow-white.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow-white.png);
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: #333333;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: #3C3C3C;
                    height: 14px;
                    margin: 2px;
                }
                QScrollBar::handle:horizontal {
                    background: #666666;
                    min-width: 20px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #777777;
                }
                QScrollBar::handle:horizontal:pressed {
                    background: #888888;
                }
                QScrollBar::sub-line:horizontal {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::add-line:horizontal {
                    background: #444444;
                    width: 14px;
                    height: 14px;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow-white.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow-white.png);
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: #333333;
                }
            """)
            self.info_label.setText("深色主题滚动条样式：使用深色背景，适合暗色主题界面。")
        
        elif index == 6:
            # 隐藏式滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: none;
                    background-color: white;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: transparent;
                    width: 8px;
                    margin: 1px;
                }
                QScrollBar::handle:vertical {
                    background: transparent;
                    border-radius: 4px;
                    min-height: 30px;
                }
                QScrollBar::handle:vertical:hover {
                    background: rgba(100, 100, 100, 0.3);
                }
                QScrollBar::handle:vertical:pressed {
                    background: rgba(100, 100, 100, 0.5);
                }
                QScrollBar::sub-line:vertical,
                QScrollBar::add-line:vertical {
                    background: none;
                }
                QScrollBar::up-arrow:vertical,
                QScrollBar::down-arrow:vertical {
                    background: none;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: transparent;
                    height: 8px;
                    margin: 1px;
                }
                QScrollBar::handle:horizontal {
                    background: transparent;
                    border-radius: 4px;
                    min-width: 30px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: rgba(100, 100, 100, 0.3);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: rgba(100, 100, 100, 0.5);
                }
                QScrollBar::sub-line:horizontal,
                QScrollBar::add-line:horizontal {
                    background: none;
                }
                QScrollBar::left-arrow:horizontal,
                QScrollBar::right-arrow:horizontal {
                    background: none;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("隐藏式滚动条样式：默认隐藏，仅在鼠标悬停时显示，提供干净的视觉效果。")
        
        elif index == 7:
            # 渐变滚动条样式
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 1px solid #E0E0E0;
                    background-color: #F5F5F5;
                }
                
                /* 垂直滚动条 */
                QScrollBar:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #EEEEEE, stop:1 #E0E0E0);
                    width: 16px;
                    margin: 0;
                    border-left: 1px solid #CCCCCC;
                }
                QScrollBar::handle:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #1A237E, stop:1 #283593);
                    min-height: 40px;
                    border-radius: 8px;
                    margin: 3px;
                }
                QScrollBar::handle:vertical:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #303F9F, stop:1 #3949AB);
                }
                QScrollBar::handle:vertical:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #1A237E, stop:1 #0D47A1);
                }
                QScrollBar::sub-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    height: 24px;
                    border-bottom: 1px solid #CCCCCC;
                }
                QScrollBar::add-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    height: 24px;
                    border-top: 1px solid #CCCCCC;
                }
                QScrollBar::up-arrow:vertical {
                    image: url(:/icons/up-arrow-white.png);
                }
                QScrollBar::down-arrow:vertical {
                    image: url(:/icons/down-arrow-white.png);
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                
                /* 水平滚动条 */
                QScrollBar:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #EEEEEE, stop:1 #E0E0E0);
                    height: 16px;
                    margin: 0;
                    border-top: 1px solid #CCCCCC;
                }
                QScrollBar::handle:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1A237E, stop:1 #283593);
                    min-width: 40px;
                    border-radius: 8px;
                    margin: 3px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #303F9F, stop:1 #3949AB);
                }
                QScrollBar::handle:horizontal:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #1A237E, stop:1 #0D47A1);
                }
                QScrollBar::sub-line:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    width: 24px;
                    border-right: 1px solid #CCCCCC;
                }
                QScrollBar::add-line:horizontal {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #BDBDBD, stop:1 #9E9E9E);
                    width: 24px;
                    border-left: 1px solid #CCCCCC;
                }
                QScrollBar::left-arrow:horizontal {
                    image: url(:/icons/left-arrow-white.png);
                }
                QScrollBar::right-arrow:horizontal {
                    image: url(:/icons/right-arrow-white.png);
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            """)
            self.info_label.setText("渐变滚动条样式：使用渐变效果增强滚动条的视觉吸引力。")
    
    def reset_scrollbar(self):
        """重置滚动条样式"""
        # 重置滚动条位置
        self.scroll_area.verticalScrollBar().setValue(0)
        self.scroll_area.horizontalScrollBar().setValue(0)
        
        # 恢复默认样式
        self.update_scrollbar_style(self.style_combobox.currentIndex())

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollBarStylesWindow()
    window.show()
    sys.exit(app.exec())