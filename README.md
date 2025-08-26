Qt-Widgets-Stylesheet-Gallery / Qt控件样式表画廊

一个精心策划且全面的 Qt 控件样式表示例集合。实时查看不同 QSS 对各种控件的影响。是学习、获取灵感和进行 UI 开发的绝佳资源。

A comprehensive and curated collection of Qt widget styling examples. See how different QSS affects various widgets in real-time. Perfect for learning, inspiration, and UI development.

Qt样式表示例集合-怎么使用 / How to Use Qt Stylesheet Examples Collection

本文件夹包含了各种Qt控件的样式表示例，旨在帮助开发者学习如何自定义Qt应用程序的外观。每个文件都针对特定的Qt控件，提供了多种样式实现和详细的注释说明。

This folder contains various Qt widget stylesheet examples designed to help developers learn how to customize the appearance of Qt applications. Each file focuses on a specific Qt widget, providing multiple style implementations and detailed comments.

目录结构 / Directory Structure

· button_styles.py - QPushButton控件的样式表示例 / QPushButton widget stylesheet examples

· label_styles.py - QLabel控件的样式表示例 / QLabel widget stylesheet examples

· combobox_styles.py - QComboBox控件的样式表示例 / QComboBox widget stylesheet examples

· lineedit_styles.py - QLineEdit控件的样式表示例 / QLineEdit widget stylesheet examples

· slider_styles.py - QSlider控件的样式表示例 / QSlider widget stylesheet examples

· checkbox_styles.py - QCheckBox控件的样式表示例 / QCheckBox widget stylesheet examples

· global_styles.py - 全局样式表示例 / Global stylesheet examples

· progressbar_styles.py - QProgressBar控件的样式表示例 / QProgressBar widget stylesheet examples

· textedit_styles.py - QTextEdit控件的样式表示例 / QTextEdit widget stylesheet examples

· radiobutton_styles.py - QRadioButton控件的样式表示例 / QRadioButton widget stylesheet examples

· tablewidget_styles.py - QTableWidget控件的样式表示例 / QTableWidget widget stylesheet examples

· tabwidget_styles.py - QTabWidget控件的样式表示例 / QTabWidget widget stylesheet examples

· listwidget_styles.py - QListWidget控件的样式表示例 / QListWidget widget stylesheet examples

· treewidget_styles.py - QTreeWidget控件的样式表示例 / QTreeWidget widget stylesheet examples

· scrollbar_styles.py - QScrollBar控件的样式表示例 / QScrollBar widget stylesheet examples

· splitter_styles.py - QSplitter控件的样式表示例 / QSplitter widget stylesheet examples
· README.md - 本说明文件 / This documentation file


如何使用 / How to Use

每个Python文件都是一个独立的可运行程序，包含了完整的窗口界面和交互功能。你可以直接运行这些文件来查看各种样式效果。

Each Python file is an independent runnable program containing a complete window interface and interactive functionality. You can run these files directly to view various style effects.

运行单个示例 / Run a Single Example

```bash
python button_styles.py
```

在自己的项目中使用样式表 / Using Stylesheets in Your Own Projects

你可以从这些示例中复制样式表代码，然后在自己的项目中使用。有两种主要的方式来应用样式表：

You can copy stylesheet code from these examples and use it in your own projects. There are two main ways to apply stylesheets:

1. 设置应用程序全局样式表 / Set Application Global Stylesheet

```python
app.setStyleSheet("QPushButton { color: white; background-color: #1464A0; }")
```

1. 设置特定控件的样式表 / Set Specific Widget Stylesheet

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

样式表语法 / Stylesheet Syntax

Qt样式表的语法与CSS类似，但针对Qt控件进行了扩展。以下是一些基本规则：

Qt stylesheet syntax is similar to CSS but extended for Qt widgets. Here are some basic rules:

· 使用选择器来指定要设置样式的控件类型 / Use selectors to specify which widget types to style
· 在花括号内定义样式属性 / Define style properties within curly braces
· 使用分号分隔不同的属性 / Use semicolons to separate different properties
· 可以使用伪状态（如:hover, :pressed）来定义控件在不同状态下的样式 / Use pseudo-states (like :hover, :pressed) to define styles for widgets in different states
· 可以使用子控件选择器（如::handle, ::indicator）来设置控件子元素的样式 / Use sub-control selectors (like ::handle, ::indicator) to style sub-elements of widgets

学习资源 / Learning Resources

· Qt官方样式表文档 / Qt Official Stylesheet Documentation
· Qt样式表语法 / Qt Stylesheet Syntax
· Qt样式表参考 / Qt Stylesheet Reference
· Qt样式表自定义 / Qt Stylesheet Customization
· Qt样式表示例 / Qt Stylesheet Examples

注意事项 / Important Notes

1. 样式表的优先级：控件特定样式表优先于应用程序全局样式表 / Stylesheet priority: Widget-specific stylesheets take precedence over application global stylesheets
2. 某些复杂控件（如QTreeWidget, QTableWidget）有特殊的子控件选择器 / Some complex widgets (like QTreeWidget, QTableWidget) have special sub-control selectors
3. 样式表会影响控件的绘制性能，特别是在复杂界面中 / Stylesheets can affect widget rendering performance, especially in complex interfaces
4. 某些原生控件的外观可能会限制样式表的效果 / The appearance of some native widgets may limit the effectiveness of stylesheets

贡献 / Contribution

如果你有新的样式表示例或改进建议，欢迎分享！

If you have new stylesheet examples or improvement suggestions, please feel free to share!

```
Deepseek-r1: 代码基本框架生成 / Deepseek-r1: Code base framework generation
```
