import sys
from PyQt5.QtWidgets import QApplication
from lad_markdown_viewer.ladmark_viewer import LadMark

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 默认加载的Markdown文件路径
    # viewer = LadMark('D:/lad/LAD_Project/00_Platform_Strategy/02_Strategic_Subdocs/01_Platform_Model/LAD-00-02-01-001.md')
    viewer = LadMark('D:/lad/LAD_Project/07_Templates_Standards/04_Naming_Conventions/LAD-07-04-001.md')
    viewer.show()
    sys.exit(app.exec_()) 