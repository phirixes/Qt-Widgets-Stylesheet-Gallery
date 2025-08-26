#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QTreeWidget样式表示例
此文件展示了如何自定义Qt中QTreeWidget控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QGroupBox
)
from PySide6.QtGui import QFont, QBrush, QColor, QIcon

class TreeWidgetStylesWindow(QMainWindow):
    """QTreeWidget样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTreeWidget样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QTreeWidget样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择树样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本树", 
            "文件夹树", 
            "彩色树",
            "深色主题树",
            "文件系统树",
            "复选框树",
            "扁平风格树",
            "展开按钮自定义树"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_tree_style)
        
        # 功能按钮
        self.reset_button = QPushButton("重置树")
        self.reset_button.clicked.connect(self.reset_tree)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建树容器
        self.tree_container = QWidget()
        self.tree_layout = QVBoxLayout(self.tree_container)
        self.main_layout.addWidget(self.tree_container)
        
        # 创建树控件
        self.create_treewidget()
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # 默认显示基本树
        self.update_tree_style(0)
    
    def create_treewidget(self):
        """创建树控件并添加项目"""
        # 创建树控件
        self.tree_widget = QTreeWidget()
        
        # 设置列名
        self.tree_widget.setHeaderLabel("项目结构")
        
        # 添加树节点
        self._add_tree_items()
        
        # 添加树控件到布局
        self.tree_layout.addWidget(self.tree_widget)
    
    def _add_tree_items(self):
        """添加树节点"""
        # 创建根节点
        root1 = QTreeWidgetItem(self.tree_widget, ["项目1"])
        root2 = QTreeWidgetItem(self.tree_widget, ["项目2"])
        
        # 为root1添加子节点
        child1_1 = QTreeWidgetItem(root1, ["组件A"])
        child1_2 = QTreeWidgetItem(root1, ["组件B"])
        
        # 为root2添加子节点
        child2_1 = QTreeWidgetItem(root2, ["组件C"])
        child2_2 = QTreeWidgetItem(root2, ["组件D"])
        
        # 为child1_1添加子节点
        grandchild1_1_1 = QTreeWidgetItem(child1_1, ["元素1"])
        grandchild1_1_2 = QTreeWidgetItem(child1_1, ["元素2"])
        
        # 为child1_2添加子节点
        grandchild1_2_1 = QTreeWidgetItem(child1_2, ["元素3"])
        
        # 为child2_1添加子节点
        grandchild2_1_1 = QTreeWidgetItem(child2_1, ["元素4"])
        grandchild2_1_2 = QTreeWidgetItem(child2_1, ["元素5"])
        grandchild2_1_3 = QTreeWidgetItem(child2_1, ["元素6"])
        
        # 默认展开所有节点
        root1.setExpanded(True)
        root2.setExpanded(True)
        child1_1.setExpanded(True)
        child1_2.setExpanded(True)
        child2_1.setExpanded(True)
    
    def update_tree_style(self, index):
        """根据选择更新树样式"""
        # 清除之前的样式
        self.tree_widget.setStyleSheet("")
        
        # 应用新样式
        if index == 0:
            # 基本树样式
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 25px;
                    padding: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #CCE8FF;
                    color: #000000;
                }
                QTreeWidget::item:hover {
                    background-color: #F5F5F5;
                }
                QTreeWidget::branch {
                    background-color: white;
                }
            """)
            self.info_label.setText("基本树样式：使用简单的边框和背景色，清晰展示层次结构。")
        
        elif index == 1:
            # 文件夹树样式
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: #F8F9FA;
                    border: 1px solid #E9ECEF;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 28px;
                    padding: 3px 0;
                }
                QTreeWidget::item:selected {
                    background-color: #E3F2FD;
                    color: #1976D2;
                    font-weight: bold;
                }
                QTreeWidget::item:hover {
                    background-color: #FAFAFA;
                }
                QTreeWidget::branch {
                    background-color: #F8F9FA;
                }
            """)
            self.info_label.setText("文件夹树样式：模拟文件系统的树结构，适合显示目录层级。")
        
        elif index == 2:
            # 彩色树样式
            self.reset_tree()
            
            # 设置彩色样式
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 25px;
                    padding: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
                QTreeWidget::item:hover {
                    background-color: #FFF8E1;
                }
                /* 为不同层级的节点设置不同颜色 */
                QTreeWidget::item:first-level {
                    color: #2196F3;
                    font-weight: bold;
                }
                QTreeWidget::item:second-level {
                    color: #4CAF50;
                }
                QTreeWidget::item:third-level {
                    color: #9C27B0;
                }
            """)
            
            # 为不同层级的节点添加属性
            for i in range(self.tree_widget.topLevelItemCount()):
                top_item = self.tree_widget.topLevelItem(i)
                top_item.setData(0, Qt.UserRole, "first-level")
                
                for j in range(top_item.childCount()):
                    child_item = top_item.child(j)
                    child_item.setData(0, Qt.UserRole, "second-level")
                    
                    for k in range(child_item.childCount()):
                        grandchild_item = child_item.child(k)
                        grandchild_item.setData(0, Qt.UserRole, "third-level")
            
            self.info_label.setText("彩色树样式：根据节点层级设置不同的文本颜色，增强视觉层次感。")
        
        elif index == 3:
            # 深色主题树样式
            self.reset_tree()
            
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: #2C2C2C;
                    color: #FFFFFF;
                    border: 1px solid #444444;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 25px;
                    padding: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #3F51B5;
                    color: #FFFFFF;
                }
                QTreeWidget::item:hover {
                    background-color: #3C3C3C;
                }
                QTreeWidget::branch {
                    background-color: #2C2C2C;
                }
                QTreeWidget::branch:has-children:!has-siblings:closed,
                QTreeWidget::branch:closed:has-children:has-siblings {
                    border-image: none;
                    image: url(:/icons/right-arrow-white.png);
                }
                QTreeWidget::branch:open:has-children:!has-siblings,
                QTreeWidget::branch:open:has-children:has-siblings {
                    border-image: none;
                    image: url(:/icons/down-arrow-white.png);
                }
            """)
            self.info_label.setText("深色主题树样式：使用深色背景和高对比度的文本颜色，适合夜间使用。")
        
        elif index == 4:
            # 文件系统树样式
            self.reset_tree()
            
            # 重新设置标题
            self.tree_widget.setHeaderLabel("文件系统")
            
            # 清空现有节点
            self.tree_widget.clear()
            
            # 创建模拟文件系统的节点
            root = QTreeWidgetItem(self.tree_widget, ["项目"])
            docs = QTreeWidgetItem(root, ["文档"])
            src = QTreeWidgetItem(root, ["源代码"])
            assets = QTreeWidgetItem(root, ["资源"])
            
            readme = QTreeWidgetItem(docs, ["README.md"])
            license = QTreeWidgetItem(docs, ["LICENSE"])
            
            main_py = QTreeWidgetItem(src, ["main.py"])
            module1 = QTreeWidgetItem(src, ["module1"])
            module1_1 = QTreeWidgetItem(module1, ["__init__.py"])
            module1_2 = QTreeWidgetItem(module1, ["utils.py"])
            
            images = QTreeWidgetItem(assets, ["images"])
            icons = QTreeWidgetItem(assets, ["icons"])
            
            # 展开节点
            root.setExpanded(True)
            docs.setExpanded(True)
            src.setExpanded(True)
            assets.setExpanded(True)
            module1.setExpanded(True)
            
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 25px;
                    padding: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #E3F2FD;
                    color: #1976D2;
                }
                QTreeWidget::item:hover {
                    background-color: #FAFAFA;
                }
                /* 为不同类型的文件设置不同的图标位置指示器 */
                QTreeWidget::item[is_folder="true"] {
                    font-weight: bold;
                    color: #2196F3;
                }
                QTreeWidget::item[is_python="true"] {
                    color: #3776AB;
                }
                QTreeWidget::item[is_markdown="true"] {
                    color: #0088CC;
                }
            """)
            
            # 设置自定义数据
            root.setData(0, Qt.UserRole + 1, "true")  # is_folder
            docs.setData(0, Qt.UserRole + 1, "true")
            src.setData(0, Qt.UserRole + 1, "true")
            assets.setData(0, Qt.UserRole + 1, "true")
            module1.setData(0, Qt.UserRole + 1, "true")
            images.setData(0, Qt.UserRole + 1, "true")
            icons.setData(0, Qt.UserRole + 1, "true")
            
            readme.setData(0, Qt.UserRole + 2, "true")  # is_markdown
            main_py.setData(0, Qt.UserRole + 3, "true")  # is_python
            module1_1.setData(0, Qt.UserRole + 3, "true")
            module1_2.setData(0, Qt.UserRole + 3, "true")
            
            self.info_label.setText("文件系统树样式：模拟文件系统结构，为不同类型的文件和目录设置不同样式。")
        
        elif index == 5:
            # 复选框树样式
            self.reset_tree()
            
            # 为所有节点添加复选框
            self._add_checkboxes_to_tree()
            
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 25px;
                    padding: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #F5F5F5;
                    color: #000000;
                }
                QTreeWidget::item:hover {
                    background-color: #FAFAFA;
                }
                /* 自定义复选框样式 */
                QTreeWidget::indicator {
                    width: 18px;
                    height: 18px;
                }
                QTreeWidget::indicator:checked {
                    image: url(:/icons/checkbox-checked.png);
                }
                QTreeWidget::indicator:unchecked {
                    image: url(:/icons/checkbox-unchecked.png);
                }
                QTreeWidget::indicator:indeterminate {
                    image: url(:/icons/checkbox-indeterminate.png);
                }
            """)
            
            # 连接信号以便点击复选框时更新父节点
            self.tree_widget.itemChanged.connect(self._on_tree_item_changed)
            
            self.info_label.setText("复选框树样式：每个节点都带有复选框，支持级联选中/取消选中功能。")
        
        elif index == 6:
            # 扁平风格树样式
            self.reset_tree()
            
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: #FAFAFA;
                    border: 1px solid #EEEEEE;
                    font-size: 14px;
                    outline: none;
                }
                QTreeWidget::item {
                    height: 32px;
                    padding: 4px 8px;
                    border-radius: 4px;
                    margin: 2px;
                }
                QTreeWidget::item:selected {
                    background-color: #2196F3;
                    color: white;
                    border-radius: 4px;
                }
                QTreeWidget::item:hover {
                    background-color: #E3F2FD;
                }
                /* 隐藏默认展开/折叠指示器 */
                QTreeWidget::branch {
                    background: none;
                }
                QTreeWidget::branch:has-children:!has-siblings:closed,
                QTreeWidget::branch:closed:has-children:has-siblings {
                    border-image: none;
                    image: none;
                }
                QTreeWidget::branch:open:has-children:!has-siblings,
                QTreeWidget::branch:open:has-children:has-siblings {
                    border-image: none;
                    image: none;
                }
            """)
            
            self.info_label.setText("扁平风格树样式：使用圆角和较大的边距，隐藏了默认的展开/折叠指示器，呈现现代扁平设计。")
        
        elif index == 7:
            # 展开按钮自定义树样式
            self.reset_tree()
            
            self.tree_widget.setStyleSheet("""
                QTreeWidget {
                    background-color: white;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                QTreeWidget::item {
                    height: 28px;
                    padding: 3px;
                }
                QTreeWidget::item:selected {
                    background-color: #FFF3E0;
                    color: #E65100;
                }
                QTreeWidget::item:hover {
                    background-color: #FFF8E1;
                }
                /* 自定义展开/折叠指示器 */
                QTreeWidget::branch {
                    background-color: white;
                }
                QTreeWidget::branch:has-children:!has-siblings:closed,
                QTreeWidget::branch:closed:has-children:has-siblings {
                    border-image: none;
                    image: url(:/icons/right-arrow.png);
                }
                QTreeWidget::branch:open:has-children:!has-siblings,
                QTreeWidget::branch:open:has-children:has-siblings {
                    border-image: none;
                    image: url(:/icons/down-arrow.png);
                }
            """)
            
            self.info_label.setText("展开按钮自定义树样式：自定义了展开/折叠指示器，让树控件看起来更具特色。")
    
    def _add_checkboxes_to_tree(self):
        """为树中的所有节点添加复选框"""
        # 递归地为所有节点添加复选框
        def add_checkbox_to_item(item):
            # 设置为可选中
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            # 默认设置为未选中
            item.setCheckState(0, Qt.Unchecked)
            
            # 递归处理子节点
            for i in range(item.childCount()):
                add_checkbox_to_item(item.child(i))
        
        # 为所有顶级节点添加复选框
        for i in range(self.tree_widget.topLevelItemCount()):
            add_checkbox_to_item(self.tree_widget.topLevelItem(i))
    
    def _on_tree_item_changed(self, item, column):
        """当树节点状态改变时的处理函数，实现级联选择"""
        # 获取当前节点的选中状态
        check_state = item.checkState(column)
        
        # 递归地更新子节点
        def update_child_items(parent_item, state):
            for i in range(parent_item.childCount()):
                child_item = parent_item.child(i)
                child_item.setCheckState(0, state)
                update_child_items(child_item, state)
        
        # 更新子节点
        update_child_items(item, check_state)
        
        # 更新父节点
        parent = item.parent()
        if parent:
            self._update_parent_check_state(parent)
    
    def _update_parent_check_state(self, parent_item):
        """根据子节点状态更新父节点的选中状态"""
        # 检查所有子节点的状态
        checked_count = 0
        unchecked_count = 0
        total_count = parent_item.childCount()
        
        for i in range(total_count):
            child_state = parent_item.child(i).checkState(0)
            if child_state == Qt.Checked:
                checked_count += 1
            elif child_state == Qt.Unchecked:
                unchecked_count += 1
        
        # 更新父节点状态
        if checked_count == total_count:
            # 所有子节点都选中
            parent_item.setCheckState(0, Qt.Checked)
        elif unchecked_count == total_count:
            # 所有子节点都未选中
            parent_item.setCheckState(0, Qt.Unchecked)
        else:
            # 部分子节点选中（不确定状态）
            parent_item.setCheckState(0, Qt.PartiallyChecked)
        
        # 递归更新上层父节点
        grandparent = parent_item.parent()
        if grandparent:
            self._update_parent_check_state(grandparent)
    
    def reset_tree(self):
        """重置树数据和样式"""
        # 清空树
        self.tree_widget.clear()
        
        # 恢复默认列名
        self.tree_widget.setHeaderLabel("项目结构")
        
        # 重新添加项目
        self._add_tree_items()

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())