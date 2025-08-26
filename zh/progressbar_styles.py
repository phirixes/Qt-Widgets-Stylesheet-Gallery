#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QProgressBar样式表示例
此文件展示了如何自定义Qt中QProgressBar控件的各种样式效果。
"""

import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QProgressBar, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox
from PySide6.QtGui import QColor

class ProgressBarStylesWindow(QMainWindow):
    """QProgressBar样式表示例窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QProgressBar样式表示例")
        self.resize(800, 600)
        
        # 创建中心部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 添加标题
        title_label = QLabel("QProgressBar样式表示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # 创建样式选择器
        selector_layout = QHBoxLayout()
        selector_label = QLabel("选择进度条样式:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "基本进度条", 
            "渐变进度条", 
            "圆形进度条", 
            "分段进度条",
            "磨砂玻璃效果",
            "霓虹效果",
            "3D效果",
            "自定义文本显示"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_progress_bar_style)
        
        # 控制按钮
        self.start_button = QPushButton("开始")
        self.start_button.clicked.connect(self.start_progress)
        self.reset_button = QPushButton("重置")
        self.reset_button.clicked.connect(self.reset_progress)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.start_button)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # 创建进度条容器
        self.progress_container = QWidget()
        self.progress_layout = QVBoxLayout(self.progress_container)
        self.main_layout.addWidget(self.progress_container)
        
        # 创建各种进度条
        self.create_progress_bars()
        
        # 设置定时器用于更新进度
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        
        # 默认显示基本进度条
        self.update_progress_bar_style(0)
    
    def create_progress_bars(self):
        """创建各种进度条"""
        # 基本进度条
        self.basic_progress = QProgressBar()
        self.basic_progress.setValue(0)
        self.basic_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("1. 基本进度条"))
        self.progress_layout.addWidget(self.basic_progress)
        
        # 渐变进度条
        self.gradient_progress = QProgressBar()
        self.gradient_progress.setValue(0)
        self.gradient_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("2. 渐变进度条"))
        self.progress_layout.addWidget(self.gradient_progress)
        
        # 圆形进度条
        self.circular_progress = QProgressBar()
        self.circular_progress.setValue(0)
        self.circular_progress.setMinimumSize(150, 150)
        self.progress_layout.addWidget(QLabel("3. 圆形进度条"))
        self.progress_layout.addWidget(self.circular_progress, alignment=Qt.AlignCenter)
        
        # 分段进度条
        self.segmented_progress = QProgressBar()
        self.segmented_progress.setValue(0)
        self.segmented_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("4. 分段进度条"))
        self.progress_layout.addWidget(self.segmented_progress)
        
        # 磨砂玻璃效果进度条
        self.glass_progress = QProgressBar()
        self.glass_progress.setValue(0)
        self.glass_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("5. 磨砂玻璃效果"))
        self.progress_layout.addWidget(self.glass_progress)
        
        # 霓虹效果进度条
        self.neon_progress = QProgressBar()
        self.neon_progress.setValue(0)
        self.neon_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("6. 霓虹效果"))
        self.progress_layout.addWidget(self.neon_progress)
        
        # 3D效果进度条
        self.three_d_progress = QProgressBar()
        self.three_d_progress.setValue(0)
        self.three_d_progress.setMinimumHeight(40)
        self.progress_layout.addWidget(QLabel("7. 3D效果"))
        self.progress_layout.addWidget(self.three_d_progress)
        
        # 自定义文本显示进度条
        self.custom_text_progress = QProgressBar()
        self.custom_text_progress.setValue(0)
        self.custom_text_progress.setMinimumHeight(30)
        self.progress_layout.addWidget(QLabel("8. 自定义文本显示"))
        self.progress_layout.addWidget(self.custom_text_progress)
        
        # 添加说明
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.progress_layout.addWidget(self.info_label)
        
        # 应用样式
        self.apply_styles()
        
        # 默认隐藏所有进度条
        for i in range(1, self.progress_layout.count()):
            widget = self.progress_layout.itemAt(i).widget()
            if widget and widget != self.info_label:
                widget.hide()
    
    def apply_styles(self):
        """应用各种进度条样式"""
        # 1. 基本进度条样式
        self.basic_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #333;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                border-radius: 10px;
            }
        """)
        
        # 2. 渐变进度条样式
        self.gradient_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-weight: bold;
                border: 1px solid #BDBDBD;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                          stop:0 #4CAF50, stop:1 #2196F3);
                border-radius: 15px;
                border: 1px solid #4CAF50;
            }
        """)
        
        # 3. 圆形进度条样式
        self.circular_progress.setStyleSheet("""
            QProgressBar {
                background-color: #F5F5F5;
                border-radius: 75px;
                text-align: center;
                color: #2196F3;
                font-weight: bold;
                font-size: 18px;
                border: 8px solid #E0E0E0;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                border-radius: 75px;
                border: 8px solid #1976D2;
            }
        """)
        
        # 4. 分段进度条样式
        self.segmented_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #333;
                font-weight: bold;
                border: 1px solid #BDBDBD;
            }
            QProgressBar::chunk {
                background-color: #FF9800;
                width: 20px;
                margin: 1px;
                border-radius: 3px;
            }
        """)
        
        # 5. 磨砂玻璃效果进度条样式
        self.glass_progress.setStyleSheet("""
            QProgressBar {
                background-color: rgba(224, 224, 224, 150);
                border-radius: 15px;
                text-align: center;
                color: #333;
                font-weight: bold;
                border: 1px solid rgba(189, 189, 189, 150);
                backdrop-filter: blur(5px);
            }
            QProgressBar::chunk {
                background-color: rgba(33, 150, 243, 200);
                border-radius: 15px;
                border: 1px solid rgba(25, 118, 210, 200);
            }
        """)
        
        # 6. 霓虹效果进度条样式
        self.neon_progress.setStyleSheet("""
            QProgressBar {
                background-color: #1A1A1A;
                border-radius: 15px;
                text-align: center;
                color: #00BCD4;
                font-weight: bold;
                border: 1px solid #00BCD4;
                padding: 2px;
            }
            QProgressBar::chunk {
                background-color: #00BCD4;
                border-radius: 13px;
                box-shadow: 0 0 10px #00BCD4, 0 0 20px #00BCD4;
            }
        """)
        
        # 7. 3D效果进度条样式
        self.three_d_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 20px;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border: 1px solid #BDBDBD;
                box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #4CAF50, stop:1 #388E3C);
                border-radius: 20px;
                border: 1px solid #4CAF50;
                box-shadow: inset 0 2px 4px rgba(255, 255, 255, 0.3);
            }
        """)
        
        # 8. 自定义文本显示进度条样式
        self.custom_text_progress.setStyleSheet("""
            QProgressBar {
                background-color: #E0E0E0;
                border-radius: 10px;
                text-align: center;
                color: #F44336;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QProgressBar::chunk {
                background-color: #F44336;
                border-radius: 10px;
            }
        """)
        
        # 设置自定义文本显示
        self.custom_text_progress.setFormat("%v%% 完成")
    
    def update_progress_bar_style(self, index):
        """根据选择更新显示的进度条样式"""
        # 隐藏所有进度条
        for i in range(1, self.progress_layout.count()):
            widget = self.progress_layout.itemAt(i).widget()
            if widget and widget != self.info_label:
                widget.hide()
        
        # 显示选中的进度条
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        # 显示对应的标签和进度条
        self.progress_layout.itemAt(index * 2).widget().show()  # 显示标签
        progress_bars[index].show()  # 显示进度条
        
        # 更新说明信息
        descriptions = [
            "基本进度条使用简单的圆角矩形设计，适合大多数应用场景。",
            "渐变进度条使用线性渐变效果，创造出平滑的色彩过渡。",
            "圆形进度条采用圆形设计，适合展示百分比完成度。",
            "分段进度条将进度显示为离散的块状，提供不同的视觉体验。",
            "磨砂玻璃效果通过半透明和模糊效果创造现代感界面。",
            "霓虹效果使用发光和阴影创造出科技感十足的视觉效果。",
            "3D效果通过多重阴影和渐变创造出立体的视觉体验。",
            "自定义文本显示允许你修改进度条上显示的文本格式和样式。"
        ]
        self.info_label.setText(descriptions[index])
    
    def start_progress(self):
        """开始更新进度"""
        if not self.timer.isActive():
            self.timer.start(50)  # 每50毫秒更新一次
            self.start_button.setText("暂停")
        else:
            self.timer.stop()
            self.start_button.setText("继续")
    
    def reset_progress(self):
        """重置进度"""
        self.timer.stop()
        self.progress_value = 0
        
        # 重置所有进度条
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        for progress_bar in progress_bars:
            progress_bar.setValue(0)
        
        self.start_button.setText("开始")
    
    def update_progress(self):
        """更新进度值"""
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        
        # 更新所有进度条
        progress_bars = [
            self.basic_progress,
            self.gradient_progress,
            self.circular_progress,
            self.segmented_progress,
            self.glass_progress,
            self.neon_progress,
            self.three_d_progress,
            self.custom_text_progress
        ]
        
        for progress_bar in progress_bars:
            progress_bar.setValue(self.progress_value)

# 启动函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBarStylesWindow()
    window.show()
    sys.exit(app.exec())