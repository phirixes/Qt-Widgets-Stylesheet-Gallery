#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QTableWidget样式表示例
此文件展示了如何自定义Qt中QTableWidget控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QGroupBox
)
from PySide6.QtGui import QFont, QBrush, QColor

class TableWidgetStylesWindow(QMainWindow):
    """QTableWidget样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableWidget样式表示例")
        self.resize(900, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QTableWidget样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择表格样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本表格", 
            "斑马纹表格", 
            "现代风格表格",
            "深色主题表格",
            "单元格高亮表格",
            "无边框表格",
            "自定义网格表格",
            "复杂样式表格"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_table_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置表格")
        self.reset_button.clicked.connect(self.reset_table)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建表格容器
        self.table_container = QWidget()
        self.table_layout = QVBoxLayout(self.table_container)
        self.main_layout.addWidget(self.table_container)
        
        # 创建表格
        self.create_table()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本表格
        self.update_table_style(0)
    
    def create_table(self):
        """创建表格并填充示例数据"""
        # 创建表格控件
        self.table_widget = QTableWidget(5, 4)
        
        # 设置表头
        headers = ["产品名称", "价格", "库存", "状态"]
        self.table_widget.setHorizontalHeaderLabels(headers)
        
        # 填充示例数据
        data = [
            ["笔记本电脑", "¥6,999", "12", "有货"],
            ["智能手机", "¥3,999", "50", "有货"],
            ["平板电脑", "¥2,499", "0", "缺货"],
            ["智能手表", "¥1,299", "28", "有货"],
            ["无线耳机", "¥899", "45", "有货"]
        ]
        
        for row in range(5):
            for col in range(4):
                item = QTableWidgetItem(data[row][col])
                item.setTextAlignment(Qt.AlignCenter)
                
                # 设置库存状态的特殊样式
                if col == 3:
                    if data[row][col] == "缺货":
                        item.setForeground(QBrush(QColor(255, 0, 0)))
                    else:
                        item.setForeground(QBrush(QColor(0, 150, 0)))
                
                self.table_widget.setItem(row, col, item)
        
        # 自动调整列宽
        self.table_widget.horizontalHeader().setSectionResizeMode(0, self.table_widget.horizontalHeader().Stretch)
        for i in range(1, 4):
            self.table_widget.horizontalHeader().setSectionResizeMode(i, self.table_widget.horizontalHeader().ResizeToContents)
        
        # 添加表格到布局
        self.table_layout.addWidget(self.table_widget)
    
    def update_table_style(self, index):
        """根据选择更新表格样式"""
        # 清除之前的样式
        self.table_widget.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #DDDDDD;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #DDDDDD;
                }
                QHeaderView::section {
                    background-color: #F5F5F5;
                    padding: 8px;
                    border: 1px solid #DDDDDD;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("基本表格样式：使用简单的边框和背景色，提供清晰的视觉层次。")
        
        elif index == 1:
            # 斑马纹表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #E0E0E0;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTableWidget::item:selected {
                    background-color: #CCE8FF;
                    color: #000000;
                }
                QTableWidget::item:alternate {
                    background-color: #F9F9F9;
                }
                QHeaderView::section {
                    background-color: #4285F4;
                    color: white;
                    padding: 8px;
                    border: 1px solid #4285F4;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("斑马纹表格样式：使用alternate选择器创建行交替颜色效果，提高可读性。")
        
        elif index == 2:
            # 现代风格表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #FFFFFF;
                    border: 1px solid #E0E0E0;
                    border-radius: 4px;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 10px;
                    border-bottom: 1px solid #F0F0F0;
                }
                QTableWidget::item:selected {
                    background-color: #2196F3;
                    color: white;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                }
                QHeaderView::section {
                    background-color: #F5F5F5;
                    color: #333333;
                    padding: 10px;
                    border: none;
                    border-bottom: 2px solid #E0E0E0;
                    font-weight: bold;
                    font-size: 15px;
                }
            """)
            self.info_label.setText("现代风格表格样式：使用圆角边框、简洁的底部线条和悬停效果，提供现代UI体验。")
        
        elif index == 3:
            # 深色主题表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    gridline-color: #444444;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #444444;
                }
                QTableWidget::item:selected {
                    background-color: #3F51B5;
                    color: #FFFFFF;
                }
                QHeaderView::section {
                    background-color: #1A1A1A;
                    color: #FFFFFF;
                    padding: 8px;
                    border: 1px solid #444444;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("深色主题表格样式：使用深色背景和高对比度的文本颜色，适合夜间使用。")
        
        elif index == 4:
            # 单元格高亮表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #E0E0E0;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: 1px solid #E0E0E0;
                }
                QTableWidget::item:nth-child(4n+3) {
                    background-color: #FFF9C4;
                }
                QTableWidget::item:selected {
                    background-color: #FFCDD2;
                    color: #C62828;
                    font-weight: bold;
                }
                QHeaderView::section {
                    background-color: #81C784;
                    color: white;
                    padding: 8px;
                    border: 1px solid #66BB6A;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("单元格高亮表格样式：使用nth-child选择器高亮特定行，并为选中项添加特殊样式。")
        
        elif index == 5:
            # 无边框表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    border: none;
                    gridline-color: transparent;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 10px;
                    border: none;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                    border-radius: 4px;
                }
                QTableWidget::item:selected {
                    background-color: #E3F2FD;
                    border-radius: 4px;
                    color: #1565C0;
                }
                QHeaderView::section {
                    background-color: transparent;
                    color: #424242;
                    padding: 10px;
                    border: none;
                    font-weight: bold;
                }
            """)
            self.info_label.setText("无边框表格样式：移除所有边框，使用微妙的悬停效果和圆角选中状态，创造简洁的外观。")
        
        elif index == 6:
            # 自定义网格表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: #FAFAFA;
                    border: 2px solid #E0E0E0;
                    border-radius: 8px;
                    font-size: 14px;
                }
                QTableWidget::item {
                    padding: 8px;
                    border: none;
                    border-bottom: 1px dashed #E0E0E0;
                }
                QTableWidget::item:last-row {
                    border-bottom: none;
                }
                QTableWidget::item:selected {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
                QHeaderView::section {
                    background-color: #FAFAFA;
                    color: #333333;
                    padding: 10px;
                    border: none;
                    border-right: 1px solid #E0E0E0;
                    font-weight: bold;
                }
                QHeaderView::section:last-column {
                    border-right: none;
                }
            """)
            self.info_label.setText("自定义网格表格样式：使用虚线分隔行，自定义表头边框，创造独特的视觉风格。")
        
        elif index == 7:
            # 复杂样式表格样式
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    gridline-color: #EEEEEE;
                    font-size: 14px;
                    border-radius: 8px;
                    border: 1px solid #EEEEEE;
                }
                QTableWidget::item {
                    padding: 12px 8px;
                    border: 1px solid #EEEEEE;
                }
                QTableWidget::item:selected {
                    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                                  stop:0 #64B5F6, stop:1 #42A5F5);
                    color: white;
                    border: 1px solid #42A5F5;
                }
                QTableWidget::item:hover {
                    background-color: #F5F5F5;
                }
                QHeaderView::section {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                                  stop:0 #F5F5F5, stop:1 #EEEEEE);
                    color: #333333;
                    padding: 12px 8px;
                    border: 1px solid #EEEEEE;
                    font-weight: bold;
                }
                QHeaderView::section:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                                  stop:0 #EEEEEE, stop:1 #E0E0E0);
                }
                QTableCornerButton::section {
                    background-color: #F5F5F5;
                    border: 1px solid #EEEEEE;
                }
            """)
            self.info_label.setText("复杂样式表格样式：使用渐变、悬停效果和多种边框样式，创造精致的视觉体验。")
    
    def reset_table(self):
        """重置表格数据和样式"""
        # 重新创建表格
        while self.table_layout.count() > 0:
            item = self.table_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # 重新创建表格
        self.create_table()
        
        # 重置样式选择器
        self.style_combobox.setCurrentIndex(0)
        self.update_table_style(0)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())