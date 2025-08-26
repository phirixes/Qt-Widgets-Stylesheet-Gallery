#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
全局样式表示例
此文件展示了如何在Qt应用程序中应用全局样式表，以及样式表的级联和继承关系。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLineEdit,
    QComboBox,
    QCheckBox,
    QTextEdit,
    QTabWidget,
    QGroupBox
)
from PySide6.QtGui import QFont, QColor

class GlobalStylesWindow(QMainWindow):
    """全局样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("全局样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("全局样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # 创建标签页控件，用于展示不同的样式表示例
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        
        # 添加不同的标签页
        self.create_global_style_tab()
        self.create_cascade_style_tab()
        self.create_custom_classes_tab()
        self.create_pseudo_states_tab()
    
    def create_global_style_tab(self):
        """全局样式表标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 说明标签
        info_label = QLabel("全局样式表应用于整个应用程序或窗口，会影响所有匹配的控件。")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        # 创建各种控件，以展示全局样式的效果
        controls_layout = QVBoxLayout()
        
        # 按钮
        button_layout = QHBoxLayout()
        button1 = QPushButton("按钮 1")
        button2 = QPushButton("按钮 2")
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        controls_layout.addLayout(button_layout)
        
        # 输入框
        lineedit_layout = QHBoxLayout()
        lineedit1 = QLineEdit()
        lineedit1.setPlaceholderText("输入框 1")
        lineedit2 = QLineEdit()
        lineedit2.setPlaceholderText("输入框 2")
        lineedit_layout.addWidget(lineedit1)
        lineedit_layout.addWidget(lineedit2)
        controls_layout.addLayout(lineedit_layout)
        
        # 标签
        label_layout = QHBoxLayout()
        label1 = QLabel("标签 1")
        label2 = QLabel("标签 2")
        label_layout.addWidget(label1)
        label_layout.addWidget(label2)
        controls_layout.addLayout(label_layout)
        
        # 复选框
        checkbox_layout = QHBoxLayout()
        checkbox1 = QCheckBox("复选框 1")
        checkbox2 = QCheckBox("复选框 2")
        checkbox_layout.addWidget(checkbox1)
        checkbox_layout.addWidget(checkbox2)
        controls_layout.addLayout(checkbox_layout)
        
        # 下拉框
        combobox_layout = QHBoxLayout()
        combobox1 = QComboBox()
        combobox1.addItems(["选项 1", "选项 2", "选项 3"])
        combobox2 = QComboBox()
        combobox2.addItems(["A", "B", "C"])
        combobox_layout.addWidget(combobox1)
        combobox_layout.addWidget(combobox2)
        controls_layout.addLayout(combobox_layout)
        
        layout.addLayout(controls_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "全局样式")
    
    def create_cascade_style_tab(self):
        """样式表级联标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 说明标签
        info_label = QLabel("样式表具有级联效果，可以在不同级别应用样式。控件级别的样式会覆盖更高级别的样式。")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        # 创建具有不同级别样式的控件
        controls_layout = QVBoxLayout()
        
        # 1. 仅应用全局样式的按钮
        global_button = QPushButton("仅全局样式")
        controls_layout.addWidget(global_button)
        
        # 2. 应用全局和窗口级别样式的按钮
        # 窗口级别的样式在主应用程序中设置
        window_button = QPushButton("全局 + 窗口样式")
        controls_layout.addWidget(window_button)
        
        # 3. 应用全局、窗口和控件级别样式的按钮
        widget_button = QPushButton("全局 + 窗口 + 控件样式")
        # 控件级别的样式在下方设置
        widget_button.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
        """)
        controls_layout.addWidget(widget_button)
        
        # 4. 应用全局样式和不同控件级别样式的按钮
        special_button = QPushButton("特殊样式按钮")
        special_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: 2px dashed #E65100;
                border-radius: 4px;
                padding: 10px;
                font-style: italic;
            }
        """)
        controls_layout.addWidget(special_button)
        
        # 创建一个组，展示组内控件的样式
        group_box = QGroupBox("组内控件样式")
        group_layout = QVBoxLayout(group_box)
        
        group_button = QPushButton("组内按钮")
        group_lineedit = QLineEdit()
        group_lineedit.setPlaceholderText("组内输入框")
        group_checkbox = QCheckBox("组内复选框")
        
        group_layout.addWidget(group_button)
        group_layout.addWidget(group_lineedit)
        group_layout.addWidget(group_checkbox)
        
        controls_layout.addWidget(group_box)
        
        layout.addLayout(controls_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "样式级联")
    
    def create_custom_classes_tab(self):
        """自定义类和ID样式标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 说明标签
        info_label = QLabel("可以通过设置对象名称（ID选择器）或继承自定义类来应用特定样式。")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        # 创建具有自定义ID和类的控件
        controls_layout = QVBoxLayout()
        
        # 1. 使用ID选择器的按钮
        id_button = QPushButton("ID选择器按钮")
        id_button.setObjectName("specialButton")  # 设置对象名称作为ID
        controls_layout.addWidget(id_button)
        
        # 2. 另一个使用ID选择器的按钮
        danger_button = QPushButton("危险按钮")
        danger_button.setObjectName("dangerButton")  # 设置对象名称作为ID
        controls_layout.addWidget(danger_button)
        
        # 3. 创建一个自定义类的按钮（在这个例子中，我们只是设置对象名称来模拟类）
        primary_button = QPushButton("主要按钮")
        primary_button.setProperty("class", "primary")  # 设置属性来模拟类
        controls_layout.addWidget(primary_button)
        
        # 4. 创建一个次要按钮
        secondary_button = QPushButton("次要按钮")
        secondary_button.setProperty("class", "secondary")  # 设置属性来模拟类
        controls_layout.addWidget(secondary_button)
        
        # 5. 创建一个带有多个类的按钮
        complex_button = QPushButton("复杂样式按钮")
        complex_button.setProperty("class", "primary large")  # 设置多个类
        controls_layout.addWidget(complex_button)
        
        # 在实际项目中，您可以通过创建自定义控件类来实现更灵活的样式选择
        # 例如: class PrimaryButton(QPushButton): pass
        
        layout.addLayout(controls_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "自定义类和ID")
    
    def create_pseudo_states_tab(self):
        """伪状态样式标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 说明标签
        info_label = QLabel("Qt样式表支持伪状态（如:hover, :pressed, :checked等）来为控件的不同状态定义样式。")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        # 创建展示不同伪状态的控件
        controls_layout = QVBoxLayout()
        
        # 1. 具有悬停、按下状态的按钮
        state_button = QPushButton("悬停和按下效果")
        controls_layout.addWidget(state_button)
        
        # 2. 具有焦点状态的输入框
        focus_lineedit = QLineEdit()
        focus_lineedit.setPlaceholderText("获取焦点查看效果")
        controls_layout.addWidget(focus_lineedit)
        
        # 3. 具有选中和未选中状态的复选框
        checkbox_layout = QHBoxLayout()
        checkbox1 = QCheckBox("复选框 1")
        checkbox2 = QCheckBox("复选框 2")
        checkbox2.setChecked(True)
        checkbox_layout.addWidget(checkbox1)
        checkbox_layout.addWidget(checkbox2)
        controls_layout.addLayout(checkbox_layout)
        
        # 4. 禁用状态的控件
        disabled_layout = QHBoxLayout()
        disabled_button = QPushButton("禁用按钮")
        disabled_button.setEnabled(False)
        disabled_lineedit = QLineEdit()
        disabled_lineedit.setPlaceholderText("禁用输入框")
        disabled_lineedit.setEnabled(False)
        disabled_layout.addWidget(disabled_button)
        disabled_layout.addWidget(disabled_lineedit)
        controls_layout.addLayout(disabled_layout)
        
        # 5. 只读状态的文本编辑框
        readonly_textedit = QTextEdit()
        readonly_textedit.setReadOnly(True)
        readonly_textedit.setText("这是一个只读的文本编辑框")
        readonly_textedit.setMaximumHeight(80)
        controls_layout.addWidget(readonly_textedit)
        
        layout.addLayout(controls_layout)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "伪状态样式")

# 设置应用程序全局样式表
def setup_global_stylesheet(app):
    """设置应用程序的全局样式表"""
    
    # 全局样式表
    global_stylesheet = """
        /* 应用程序全局样式 */
        * {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
        }
        
        /* QMainWindow样式 */
        QMainWindow {
            background-color: #F5F5F5;
        }
        
        /* QWidget样式 */
        QWidget {
            background-color: transparent;
        }
        
        /* QPushButton基础样式 */
        QPushButton {
            background-color: #2196F3;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 6px 12px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #1976D2;
        }
        QPushButton:pressed {
            background-color: #1565C0;
        }
        QPushButton:disabled {
            background-color: #BDBDBD;
            color: #757575;
        }
        
        /* QLabel样式 */
        QLabel {
            color: #333333;
            font-size: 14px;
        }
        
        /* QLineEdit样式 */
        QLineEdit {
            background-color: white;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
            padding: 5px;
            font-size: 14px;
        }
        QLineEdit:hover {
            border-color: #999999;
        }
        QLineEdit:focus {
            border-color: #2196F3;
            background-color: #F5F5F5;
        }
        QLineEdit:disabled {
            background-color: #F5F5F5;
            color: #BDBDBD;
            border-color: #E0E0E0;
        }
        
        /* QComboBox样式 */
        QComboBox {
            background-color: white;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
            padding: 5px;
            font-size: 14px;
        }
        QComboBox:hover {
            border-color: #999999;
        }
        QComboBox:focus {
            border-color: #2196F3;
        }
        QComboBox::drop-down {
            border-left: 1px solid #CCCCCC;
        }
        
        /* QCheckBox样式 */
        QCheckBox {
            color: #333333;
            font-size: 14px;
        }
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border: 1px solid #CCCCCC;
            border-radius: 3px;
            background-color: white;
        }
        QCheckBox::indicator:checked {
            background-color: #2196F3;
            border-color: #2196F3;
        }
        
        /* QGroupBox样式 */
        QGroupBox {
            border: 1px solid #DDDDDD;
            border-radius: 4px;
            margin-top: 10px;
            padding: 10px;
            color: #333333;
            font-weight: bold;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
            background-color: #F5F5F5;
        }
        
        /* QTabWidget样式 */
        QTabWidget::pane {
            border: 1px solid #CCCCCC;
            background-color: white;
            border-radius: 4px;
        }
        QTabBar::tab {
            background-color: #E0E0E0;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            padding: 8px 16px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: white;
            color: #2196F3;
            font-weight: bold;
        }
        
        /* QTextEdit样式 */
        QTextEdit {
            background-color: white;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
            padding: 5px;
            font-size: 14px;
        }
        QTextEdit:read-only {
            background-color: #F5F5F5;
            color: #757575;
        }
        
        /* 自定义ID选择器 */
        QPushButton#specialButton {
            background-color: #4CAF50;
            font-weight: bold;
        }
        QPushButton#dangerButton {
            background-color: #F44336;
        }
        
        /* 自定义属性选择器 */
        QPushButton[class="primary"] {
            background-color: #2196F3;
            border: 2px solid #1976D2;
        }
        QPushButton[class="secondary"] {
            background-color: #607D8B;
        }
        QPushButton[class="primary large"] {
            background-color: #2196F3;
            font-size: 16px;
            padding: 10px 20px;
        }
    """
    
    # 应用全局样式表
    app.setStyleSheet(global_stylesheet)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 设置全局样式表
    setup_global_stylesheet(app)
    
    window = GlobalStylesWindow()
    window.show()
    sys.exit(app.exec())