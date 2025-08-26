# -*- coding: utf-8 -*-

"""
QTreeWidget Style Examples
This file demonstrates how to customize various style effects of the QTreeWidget control in Qt.
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
    """QTreeWidget style example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTreeWidget Style Examples")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QTreeWidget Style Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select Tree Style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Tree", 
            "Folder Tree", 
            "Colored Tree",
            "Dark Theme Tree",
            "File System Tree",
            "Checkbox Tree",
            "Flat Style Tree",
            "Custom Expand Button Tree"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_tree_style)
        
        # Function buttons
        self.reset_button = QPushButton("Reset Tree")
        self.reset_button.clicked.connect(self.reset_tree)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create tree container
        self.tree_container = QWidget()
        self.tree_layout = QVBoxLayout(self.tree_container)
        self.main_layout.addWidget(self.tree_container)
        
        # Create tree widget
        self.create_treewidget()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic tree by default
        self.update_tree_style(0)
    
    def create_treewidget(self):
        """Create tree widget and add items"""
        # Create tree widget
        self.tree_widget = QTreeWidget()
        
        # Set column name
        self.tree_widget.setHeaderLabel("Project Structure")
        
        # Add tree nodes
        self._add_tree_items()
        
        # Add tree widget to layout
        self.tree_layout.addWidget(self.tree_widget)
    
    def _add_tree_items(self):
        """Add tree nodes"""
        # Create root nodes
        root1 = QTreeWidgetItem(self.tree_widget, ["Project 1"])
        root2 = QTreeWidgetItem(self.tree_widget, ["Project 2"])
        
        # Add child nodes to root1
        child1_1 = QTreeWidgetItem(root1, ["Component A"])
        child1_2 = QTreeWidgetItem(root1, ["Component B"])
        
        # Add child nodes to root2
        child2_1 = QTreeWidgetItem(root2, ["Component C"])
        child2_2 = QTreeWidgetItem(root2, ["Component D"])
        
        # Add child nodes to child1_1
        grandchild1_1_1 = QTreeWidgetItem(child1_1, ["Element 1"])
        grandchild1_1_2 = QTreeWidgetItem(child1_1, ["Element 2"])
        
        # Add child nodes to child1_2
        grandchild1_2_1 = QTreeWidgetItem(child1_2, ["Element 3"])
        
        # Add child nodes to child2_1
        grandchild2_1_1 = QTreeWidgetItem(child2_1, ["Element 4"])
        grandchild2_1_2 = QTreeWidgetItem(child2_1, ["Element 5"])
        grandchild2_1_3 = QTreeWidgetItem(child2_1, ["Element 6"])
        
        # Expand all nodes by default
        root1.setExpanded(True)
        root2.setExpanded(True)
        child1_1.setExpanded(True)
        child1_2.setExpanded(True)
        child2_1.setExpanded(True)
    
    def update_tree_style(self, index):
        """Update tree style based on selection"""
        # Clear previous styles
        self.tree_widget.setStyleSheet("")
        
        # Apply new style
        if index == 0:
            # Basic tree style
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
            self.info_label.setText("Basic Tree Style: Uses simple borders and background colors to clearly display hierarchical structure.")
        
        elif index == 1:
            # Folder tree style
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
            self.info_label.setText("Folder Tree Style: Simulates file system tree structure, suitable for displaying directory hierarchy.")
        
        elif index == 2:
            # Colored tree style
            self.reset_tree()
            
            # Set colored style
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
                /* Set different colors for nodes at different levels */
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
            
            # Add attributes for nodes at different levels
            for i in range(self.tree_widget.topLevelItemCount()):
                top_item = self.tree_widget.topLevelItem(i)
                top_item.setData(0, Qt.UserRole, "first-level")
                
                for j in range(top_item.childCount()):
                    child_item = top_item.child(j)
                    child_item.setData(0, Qt.UserRole, "second-level")
                    
                    for k in range(child_item.childCount()):
                        grandchild_item = child_item.child(k)
                        grandchild_item.setData(0, Qt.UserRole, "third-level")
            
            self.info_label.setText("Colored Tree Style: Sets different text colors based on node levels to enhance visual hierarchy.")
        
        elif index == 3:
            # Dark theme tree style
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
            self.info_label.setText("Dark Theme Tree Style: Uses dark background and high-contrast text colors, suitable for night use.")
        
        elif index == 4:
            # File system tree style
            self.reset_tree()
            
            # Reset header
            self.tree_widget.setHeaderLabel("File System")
            
            # Clear existing nodes
            self.tree_widget.clear()
            
            # Create nodes simulating a file system
            root = QTreeWidgetItem(self.tree_widget, ["Project"])
            docs = QTreeWidgetItem(root, ["Documents"])
            src = QTreeWidgetItem(root, ["Source Code"])
            assets = QTreeWidgetItem(root, ["Assets"])
            
            readme = QTreeWidgetItem(docs, ["README.md"])
            license = QTreeWidgetItem(docs, ["LICENSE"])
            
            main_py = QTreeWidgetItem(src, ["main.py"])
            module1 = QTreeWidgetItem(src, ["module1"])
            module1_1 = QTreeWidgetItem(module1, ["__init__.py"])
            module1_2 = QTreeWidgetItem(module1, ["utils.py"])
            
            images = QTreeWidgetItem(assets, ["images"])
            icons = QTreeWidgetItem(assets, ["icons"])
            
            # Expand nodes
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
                /* Set different icon position indicators for different types of files */
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
            
            # Set custom data
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
            
            self.info_label.setText("File System Tree Style: Simulates file system structure, setting different styles for different types of files and directories.")
        
        elif index == 5:
            # Checkbox tree style
            self.reset_tree()
            
            # Add checkboxes to all nodes
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
                /* Custom checkbox style */
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
            
            # Connect signal to update parent nodes when checkbox is clicked
            self.tree_widget.itemChanged.connect(self._on_tree_item_changed)
            
            self.info_label.setText("Checkbox Tree Style: Each node has a checkbox, supporting cascading select/deselect functionality.")
        
        elif index == 6:
            # Flat style tree style
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
                /* Hide default expand/collapse indicators */
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
            
            self.info_label.setText("Flat Style Tree: Uses rounded corners and larger margins, hides default expand/collapse indicators, presenting a modern flat design.")
        
        elif index == 7:
            # Custom expand button tree style
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
                /* Custom expand/collapse indicators */
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
            
            self.info_label.setText("Custom Expand Button Tree: Customized expand/collapse indicators to make the tree widget look more distinctive.")
    
    def _add_checkboxes_to_tree(self):
        """Add checkboxes to all nodes in the tree"""
        # Recursively add checkboxes to all nodes
        def add_checkbox_to_item(item):
            # Set to selectable
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            # Set to unchecked by default
            item.setCheckState(0, Qt.Unchecked)
            
            # Recursively process child nodes
            for i in range(item.childCount()):
                add_checkbox_to_item(item.child(i))
        
        # Add checkboxes to all top-level nodes
        for i in range(self.tree_widget.topLevelItemCount()):
            add_checkbox_to_item(self.tree_widget.topLevelItem(i))
    
    def _on_tree_item_changed(self, item, column):
        """Handler function when tree node state changes, implementing cascading selection"""
        # Get the current node's checked state
        check_state = item.checkState(column)
        
        # Recursively update child nodes
        def update_child_items(parent_item, state):
            for i in range(parent_item.childCount()):
                child_item = parent_item.child(i)
                child_item.setCheckState(0, state)
                update_child_items(child_item, state)
        
        # Update child nodes
        update_child_items(item, check_state)
        
        # Update parent node
        parent = item.parent()
        if parent:
            self._update_parent_check_state(parent)
    
    def _update_parent_check_state(self, parent_item):
        """Update the checked state of parent node based on child nodes' states"""
        # Check the states of all child nodes
        checked_count = 0
        unchecked_count = 0
        total_count = parent_item.childCount()
        
        for i in range(total_count):
            child_state = parent_item.child(i).checkState(0)
            if child_state == Qt.Checked:
                checked_count += 1
            elif child_state == Qt.Unchecked:
                unchecked_count += 1
        
        # Update parent node state
        if checked_count == total_count:
            # All child nodes are checked
            parent_item.setCheckState(0, Qt.Checked)
        elif unchecked_count == total_count:
            # All child nodes are unchecked
            parent_item.setCheckState(0, Qt.Unchecked)
        else:
            # Some child nodes are checked (indeterminate state)
            parent_item.setCheckState(0, Qt.PartiallyChecked)
        
        # Recursively update upper parent nodes
        grandparent = parent_item.parent()
        if grandparent:
            self._update_parent_check_state(grandparent)
    
    def reset_tree(self):
        """Reset tree data and style"""
        # Clear the tree
        self.tree_widget.clear()
        
        # Restore default column name
        self.tree_widget.setHeaderLabel("Project Structure")
        
        # Add items again
        self._add_tree_items()

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeWidgetStylesWindow()
    window.show()
    sys.exit(app.exec())