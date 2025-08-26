# Qt样式表示例集合

本文件夹包含了各种Qt控件的样式表示例，旨在帮助开发者学习如何自定义Qt应用程序的外观。每个文件都针对特定的Qt控件，提供了多种样式实现和详细的注释说明。

## 目录结构

- `button_styles.py` - QPushButton控件的样式表示例
- `label_styles.py` - QLabel控件的样式表示例
- `combobox_styles.py` - QComboBox控件的样式表示例
- `lineedit_styles.py` - QLineEdit控件的样式表示例
- `slider_styles.py` - QSlider控件的样式表示例
- `checkbox_styles.py` - QCheckBox控件的样式表示例
- `global_styles.py` - 全局样式表示例
- `progressbar_styles.py` - QProgressBar控件的样式表示例
- `textedit_styles.py` - QTextEdit控件的样式表示例
- `radiobutton_styles.py` - QRadioButton控件的样式表示例
- `tablewidget_styles.py` - QTableWidget控件的样式表示例
- `tabwidget_styles.py` - QTabWidget控件的样式表示例
- `listwidget_styles.py` - QListWidget控件的样式表示例
- `treewidget_styles.py` - QTreeWidget控件的样式表示例
- `scrollbar_styles.py` - QScrollBar控件的样式表示例
- `splitter_styles.py` - QSplitter控件的样式表示例
- `README.md` - 本说明文件

## 如何使用

每个Python文件都是一个独立的可运行程序，包含了完整的窗口界面和交互功能。你可以直接运行这些文件来查看各种样式效果。

### 运行单个示例

```bash
python button_styles.py
```

### 在自己的项目中使用样式表

你可以从这些示例中复制样式表代码，然后在自己的项目中使用。有两种主要的方式来应用样式表：

1. **设置应用程序全局样式表**
```python
app.setStyleSheet("QPushButton { color: white; background-color: #1464A0; }")
```

2. **设置特定控件的样式表**
```python
button.setStyleSheet("""
    QPushButton {
        background-color: #1464A0;
        border: none;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #1C7BC4;
    }
""")
```

## 样式表语法

Qt样式表的语法与CSS类似，但针对Qt控件进行了扩展。以下是一些基本规则：

- 使用选择器来指定要设置样式的控件类型
- 在花括号内定义样式属性
- 使用分号分隔不同的属性
- 可以使用伪状态（如:hover, :pressed）来定义控件在不同状态下的样式
- 可以使用子控件选择器（如::handle, ::indicator）来设置控件子元素的样式

## 学习资源

- [Qt官方样式表文档](https://doc.qt.io/qt-6/stylesheet.html)
- [Qt样式表语法](https://doc.qt.io/qt-6/stylesheet-syntax.html)
- [Qt样式表参考](https://doc.qt.io/qt-6/stylesheet-reference.html)
- [Qt样式表自定义](https://doc.qt.io/qt-6/stylesheet-customizing.html)
- [Qt样式表示例](https://doc.qt.io/qt-6/stylesheet-examples.html)

## 注意事项

1. 样式表的优先级：控件特定样式表优先于应用程序全局样式表
2. 某些复杂控件（如QTreeWidget, QTableWidget）有特殊的子控件选择器
3. 样式表会影响控件的绘制性能，特别是在复杂界面中
4. 某些原生控件的外观可能会限制样式表的效果

## 贡献

如果你有新的样式表示例或改进建议，欢迎分享！