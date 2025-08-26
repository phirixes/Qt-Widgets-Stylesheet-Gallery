#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QTabWidget样式表示例
此文件展示了如何自定义Qt中QTabWidget控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QTextEdit,
    QGroupBox
)
from PySide6.QtGui import QFont, QIcon

class TabWidgetStylesWindow(QMainWindow):
    """QTabWidget样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTabWidget样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QTabWidget样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择标签样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本标签", 
            "现代风格标签", 
            "圆角标签",
            "下划线标签",
            "彩色标签",
            "深色主题标签",
            "垂直标签",
            "自定义标签"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_tab_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置标签")
        self.reset_button.clicked.connect(self.reset_tab)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建标签容器
        self.tab_container = QWidget()
        self.tab_layout = QVBoxLayout(self.tab_container)
        self.main_layout.addWidget(self.tab_container)
        
        # 创建标签控件
        self.create_tabwidget()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本标签
        self.update_tab_style(0)
    
    def create_tabwidget(self):
        """创建标签控件并添加标签页"""
        # 创建标签控件
        self.tab_widget = QTabWidget()
        
        # 创建多个标签页
        self.create_tab("基本信息", "这里是基本信息标签页的内容。")
        self.create_tab("详细设置", "这里是详细设置标签页的内容。")
        self.create_tab("高级选项", "这里是高级选项标签页的内容。")
        self.create_tab("帮助文档", "这里是帮助文档标签页的内容。")
        
        # 添加标签控件到布局
        self.tab_layout.addWidget(self.tab_widget)
    
    def create_tab(self, title, content_text):
        """创建单个标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 添加内容文本框
        content = QTextEdit()
        content.setPlainText(content_text)
        content.setReadOnly(True)
        content.setStyleSheet("background-color: #F8F9FA; border: none; padding: 10px;")
        
        # 添加一些控件作为示例
        group = QGroupBox("示例控件")
        group_layout = QVBoxLayout(group)
        
        label1 = QLabel("这是一个标签示例")
        label2 = QLabel("另一个标签示例")
        
        group_layout.addWidget(label1)
        group_layout.addWidget(label2)
        
        # 将控件添加到标签页布局
        layout.addWidget(content)
        layout.addWidget(group)
        
        # 添加标签页到标签控件
        self.tab_widget.addTab(tab, title)
    
    def update_tab_style(self, index):
        """根据选择更新标签样式"""
        # 清除之前的样式
        self.tab_widget.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #CCCCCC;
                    background-color: white;
                }
                QTabBar::tab {
                    background-color: #F0F0F0;
                    color: #333333;
                    padding: 8px 16px;
                    border: 1px solid #CCCCCC;
                    border-bottom: none;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("基本标签样式：使用简单的边框和背景色，提供清晰的视觉层次。")
        
        elif index == 1:
            # 现代风格标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 4px;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 10px 20px;
                    margin-right: 2px;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    color: #2196F3;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("现代风格标签样式：使用圆角和较大的内边距，提供更现代的外观。")
        
        elif index == 2:
            # 圆角标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 8px;
                    margin-top: 4px;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 10px 20px;
                    margin-right: 4px;
                    border-radius: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: #4CAF50;
                    color: white;
                    border-color: #4CAF50;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("圆角标签样式：所有标签都使用圆角设计，选中的标签使用对比色突出显示。")
        
        elif index == 3:
            # 下划线标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: none;
                    background-color: white;
                    border-bottom: 1px solid #E0E0E0;
                }
                QTabBar::tab {
                    background-color: transparent;
                    color: #666666;
                    padding: 12px 20px;
                    margin-right: 4px;
                }
                QTabBar::tab:hover {
                    color: #2196F3;
                }
                QTabBar::tab:selected {
                    color: #2196F3;
                    font-weight: bold;
                }
                QTabBar::tab:selected::after {
                    content: '';
                    background-color: #2196F3;
                    height: 3px;
                    width: 100%;
                    position: absolute;
                    bottom: 0;
                    left: 0;
                }
            """)
            self.info_label.setText("下划线标签样式：使用简单的下划线来标识选中的标签，提供极简设计。")
        
        elif index == 4:
            # 彩色标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                    border-radius: 4px;
                }
                QTabBar::tab {
                    color: white;
                    padding: 10px 20px;
                    margin-right: 4px;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                }
                QTabBar::tab:nth-child(1) {
                    background-color: #F44336;
                }
                QTabBar::tab:nth-child(2) {
                    background-color: #2196F3;
                }
                QTabBar::tab:nth-child(3) {
                    background-color: #4CAF50;
                }
                QTabBar::tab:nth-child(4) {
                    background-color: #FF9800;
                }
                QTabBar::tab:hover {
                    opacity: 0.8;
                }
                QTabBar::tab:selected {
                    font-weight: bold;
                }
            """)
            self.info_label.setText("彩色标签样式：每个标签使用不同的颜色，创造出丰富多彩的界面效果。")
        
        elif index == 5:
            # 深色主题标签样式
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #444444;
                    background-color: #2C2C2C;
                    color: white;
                }
                QTabBar::tab {
                    background-color: #3C3C3C;
                    color: #BBBBBB;
                    padding: 10px 20px;
                    margin-right: 2px;
                    border: 1px solid #444444;
                    border-bottom: none;
                }
                QTabBar::tab:hover {
                    background-color: #444444;
                    color: #FFFFFF;
                }
                QTabBar::tab:selected {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("深色主题标签样式：使用深色背景和高对比度的文本颜色，适合夜间使用。")
        
        elif index == 6:
            # 垂直标签样式
            # 设置标签位置为左侧
            self.tab_widget.setTabPosition(QTabWidget.West)
            
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #E0E0E0;
                    background-color: white;
                }
                QTabBar::tab {
                    background-color: #F5F5F5;
                    color: #666666;
                    padding: 12px 16px;
                    margin-bottom: 2px;
                    min-width: 80px;
                    height: 60px;
                    border-right: 1px solid #E0E0E0;
                }
                QTabBar::tab:hover {
                    background-color: #EEEEEE;
                }
                QTabBar::tab:selected {
                    background-color: white;
                    color: #2196F3;
                    border-right: none;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("垂直标签样式：标签排列在左侧，适合内容较长的标签名称。")
        
        elif index == 7:
            # 自定义标签样式
            # 恢复标签位置为顶部
            self.tab_widget.setTabPosition(QTabWidget.North)
            
            self.tab_widget.setStyleSheet("""
                QTabWidget::pane {
                    border: 2px solid #9C27B0;
                    background-color: #F5F5F5;
                    border-radius: 8px;
                    margin-top: 4px;
                }
                QTabBar::tab {
                    background-color: white;
                    color: #9C27B0;
                    padding: 10px 20px;
                    margin-right: 8px;
                    border-radius: 20px;
                    border: 2px solid #9C27B0;
                }
                QTabBar::tab:hover {
                    background-color: #F3E5F5;
                }
                QTabBar::tab:selected {
                    background-color: #9C27B0;
                    color: white;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("自定义标签样式：使用独特的圆形设计和颜色搭配，创造出个性化的标签样式。")
    
    def reset_tab(self):
        """重置标签样式"""
        # 重新创建标签控件
        while self.tab_layout.count() > 0:
            item = self.tab_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # 重新创建标签控件
        self.create_tabwidget()
        
        # 重置样式选择器
        self.style_combobox.setCurrentIndex(0)
        self.update_tab_style(0)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())