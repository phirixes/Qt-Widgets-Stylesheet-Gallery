#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QListWidget样式表示例
此文件展示了如何自定义Qt中QListWidget控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QGroupBox
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class ListWidgetStylesWindow(QMainWindow):
    """QListWidget样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QListWidget样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QListWidget样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择列表样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本列表", 
            "卡片式列表", 
            "水平列表",
            "图标列表",
            "彩色项目列表",
            "深色主题列表",
            "复选框列表",
            "自定义分隔符列表"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_list_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置列表")
        self.reset_button.clicked.connect(self.reset_list)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建列表容器
        self.list_container = QWidget()
        self.list_layout = QVBoxLayout(self.list_container)
        self.main_layout.addWidget(self.list_container)
        
        # 创建列表控件
        self.create_listwidget()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本列表
        self.update_list_style(0)
    
    def create_listwidget(self):
        """创建列表控件并添加项目"""
        # 创建列表控件
        self.list_widget = QListWidget()
        
        # 添加列表项
        items = [
            "项目一",
            "项目二",
            "项目三",
            "项目四",
            "项目五",
            "项目六",
            "项目七",
            "项目八",
            "项目九",
            "项目十"
        ]
        
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setTextAlignment(Qt.AlignVCenter)
            self.list_widget.addItem(item)
        
        # 添加列表控件到布局
        self.list_layout.addWidget(self.list_widget)
    
    def update_list_style(self, index):
        """根据选择更新列表样式"""
        # 清除之前的样式
        self.list_widget.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本列表样式
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 8px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #CCE8FF;
                    color: #000000;
                }
                QListWidget::item:hover {
                    background-color: #F5F5F5;
                }
            """)
            self.info_label.setText("基本列表样式：使用简单的边框和背景色，提供清晰的视觉层次。")
        
        elif index == 1:
            # 卡片式列表样式
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #F5F5F5;
                    border: none;
                    font-size: 14px;
                }
                QListWidget::item {
                    background-color: white;
                    padding: 12px;
                    margin: 8px;
                    border-radius: 8px;
                    border: 1px solid #E0E0E0;
                }
                QListWidget::item:selected {
                    background-color: #E3F2FD;
                    border-color: #2196F3;
                    color: #2196F3;
                    font-weight: bold;
                }
                QListWidget::item:hover {
                    border-color: #90CAF9;
                }
            """)
            self.info_label.setText("卡片式列表样式：每个项目都是一个独立的卡片，带有圆角和阴影效果。")
        
        elif index == 2:
            # 水平列表样式
            # 设置列表为水平滚动
            self.list_widget.setFlow(QListWidget.LeftToRight)
            self.list_widget.setWrapping(True)
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #FAFAFA;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    background-color: white;
                    padding: 10px 20px;
                    margin: 8px;
                    border-radius: 20px;
                    border: 1px solid #E0E0E0;
                    min-width: 100px;
                    height: 40px;
                    text-align: center;
                }
                QListWidget::item:selected {
                    background-color: #4CAF50;
                    color: white;
                    border-color: #4CAF50;
                }
                QListWidget::item:hover {
                    border-color: #4CAF50;
                }
            """)
            self.info_label.setText("水平列表样式：列表项水平排列，使用圆形按钮样式，适合分类标签。")
        
        elif index == 3:
            # 图标列表样式
            # 重置列表为垂直滚动
            self.list_widget.setFlow(QListWidget.TopToBottom)
            self.list_widget.setWrapping(False)
            
            # 重新创建带有图标的列表项
            self.reset_list()
            
            # 为每个项目添加图标
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                # 使用不同颜色的方块作为图标（实际使用中可以替换为真实图标）
                colors = ["#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", 
                          "#2196F3", "#03A9F4", "#00BCD4", "#009688", "#4CAF50"]
                color = colors[i % len(colors)]
                # 创建简单的图标样式
                item.setText(f"<span style='color:{color}; font-weight:bold'>●</span> {item.text()}")
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px 16px;
                    border-bottom: 1px solid #F5F5F5;
                }
                QListWidget::item:selected {
                    background-color: #F5F5F5;
                    color: #2196F3;
                }
                QListWidget::item:hover {
                    background-color: #FAFAFA;
                }
            """)
            self.info_label.setText("图标列表样式：每个列表项前都有一个图标，增强视觉识别能力。")
        
        elif index == 4:
            # 彩色项目列表样式
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #FFFFFF;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 12px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #E0E0E0;
                    color: #000000;
                }
                QListWidget::item:nth-child(even) {
                    background-color: #F9F9F9;
                }
                QListWidget::item:nth-child(3n) {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
            """)
            self.info_label.setText("彩色项目列表样式：使用nth-child选择器为不同行设置不同的背景色。")
        
        elif index == 5:
            # 深色主题列表样式
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    border: 1px solid #444444;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #444444;
                }
                QListWidget::item:selected {
                    background-color: #3F51B5;
                    color: #FFFFFF;
                }
                QListWidget::item:hover {
                    background-color: #3C3C3C;
                }
            """)
            self.info_label.setText("深色主题列表样式：使用深色背景和高对比度的文本颜色，适合夜间使用。")
        
        elif index == 6:
            # 复选框列表样式
            # 重新创建列表并添加复选框
            self.reset_list()
            
            # 为每个项目添加复选框样式
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                # 添加复选框符号
                item.setText(f"□ {item.text()}")
            
            # 连接信号以便点击时切换复选状态
            self.list_widget.itemClicked.connect(self.toggle_checkbox)
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #EEEEEE;
                }
                QListWidget::item:selected {
                    background-color: #F5F5F5;
                    color: #000000;
                }
            """)
            self.info_label.setText("复选框列表样式：每个列表项都有一个可以勾选的复选框，适合多选操作。")
        
        elif index == 7:
            # 自定义分隔符列表样式
            self.reset_list()
            
            self.list_widget.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border: 1px solid #E0E0E0;
                    font-size: 14px;
                }
                QListWidget::item {
                    padding: 12px 16px;
                    border-bottom: 2px dotted #E0E0E0;
                }
                QListWidget::item:selected {
                    background-color: #FFF8E1;
                    color: #FFA000;
                    font-weight: bold;
                }
                QListWidget::item:hover {
                    background-color: #FAFAFA;
                }
            """)
            self.info_label.setText("自定义分隔符列表样式：使用虚线分隔行，创造出独特的视觉风格。")
    
    def toggle_checkbox(self, item):
        """切换复选框状态"""
        text = item.text()
        if text.startswith("□"):
            # 选中状态
            item.setText(text.replace("□", "☑"))
        else:
            # 未选中状态
            item.setText(text.replace("☑", "□"))
    
    def reset_list(self):
        """重置列表数据和样式"""
        # 清空列表
        self.list_widget.clear()
        
        # 重新添加项目
        items = [
            "项目一",
            "项目二",
            "项目三",
            "项目四",
            "项目五",
            "项目六",
            "项目七",
            "项目八",
            "项目九",
            "项目十"
        ]
        
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setTextAlignment(Qt.AlignVCenter)
            self.list_widget.addItem(item)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())