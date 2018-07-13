# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\userC\Documents\GitHub\Defeaturing_WB\DefeaturingTools.ui'
#
# Created: Fri Jul 13 18:46:29 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(367, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons-new/Center-Align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DockWidget.setWindowIcon(icon)
        DockWidget.setToolTip("Defeaturing tools")
        DockWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        DockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        DockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        DockWidget.setWindowTitle("Defeaturing Tools")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.PB_RHoles = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RHoles.setGeometry(QtCore.QRect(12, 288, 81, 28))
        self.PB_RHoles.setToolTip("remove Hole from Face")
        self.PB_RHoles.setText("del Hole")
        self.PB_RHoles.setObjectName("PB_RHoles")
        self.PB_Edges = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Edges.setGeometry(QtCore.QRect(288, 36, 69, 28))
        self.PB_Edges.setToolTip("add selected Edges to List")
        self.PB_Edges.setText("Confirm")
        self.PB_Edges.setObjectName("PB_Edges")
        self.TE_Faces = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.TE_Faces.setGeometry(QtCore.QRect(41, 164, 237, 71))
        self.TE_Faces.setToolTip("List of Face(s)")
        self.TE_Faces.setObjectName("TE_Faces")
        self.checkBox_keep_original = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_keep_original.setGeometry(QtCore.QRect(248, 252, 110, 33))
        self.checkBox_keep_original.setToolTip("keep the original object")
        self.checkBox_keep_original.setText("keep Object")
        self.checkBox_keep_original.setChecked(True)
        self.checkBox_keep_original.setObjectName("checkBox_keep_original")
        self.InfoLabel = QtGui.QLabel(self.dockWidgetContents)
        self.InfoLabel.setGeometry(QtCore.QRect(43, 0, 196, 36))
        self.InfoLabel.setText("Select Edge(s)\n"
"Ctrl+Click")
        self.InfoLabel.setObjectName("InfoLabel")
        self.TE_Edges = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.TE_Edges.setEnabled(True)
        self.TE_Edges.setGeometry(QtCore.QRect(41, 36, 237, 66))
        self.TE_Edges.setToolTip("List of Edge(s)")
        self.TE_Edges.setPlainText("")
        self.TE_Edges.setObjectName("TE_Edges")
        self.PB_Faces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Faces.setGeometry(QtCore.QRect(288, 164, 69, 28))
        self.PB_Faces.setToolTip("add selected Faces to List")
        self.PB_Faces.setText("Confirm")
        self.PB_Faces.setObjectName("PB_Faces")
        self.PB_Edges_Clear = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Edges_Clear.setGeometry(QtCore.QRect(288, 71, 69, 28))
        self.PB_Edges_Clear.setText("Clear List")
        self.PB_Edges_Clear.setObjectName("PB_Edges_Clear")
        self.PB_Faces_Clear = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Faces_Clear.setGeometry(QtCore.QRect(288, 200, 69, 28))
        self.PB_Faces_Clear.setText("Clear List")
        self.PB_Faces_Clear.setObjectName("PB_Faces_Clear")
        self.Edge_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Edge_Nbr.setGeometry(QtCore.QRect(59, 104, 53, 16))
        self.Edge_Nbr.setText("0")
        self.Edge_Nbr.setObjectName("Edge_Nbr")
        self.Face_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Face_Nbr.setGeometry(QtCore.QRect(59, 236, 53, 16))
        self.Face_Nbr.setText("0")
        self.Face_Nbr.setObjectName("Face_Nbr")
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(43, 124, 177, 45))
        self.label.setText("Select Face(s)\n"
"Ctrl+Click")
        self.label.setObjectName("label")
        self.checkBox_Refine = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_Refine.setGeometry(QtCore.QRect(20, 260, 100, 20))
        self.checkBox_Refine.setToolTip("refine the resulting solid\n"
"after the operation ")
        self.checkBox_Refine.setText("refine")
        self.checkBox_Refine.setChecked(False)
        self.checkBox_Refine.setObjectName("checkBox_Refine")
        self.checkBox_keep_faces = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_keep_faces.setGeometry(QtCore.QRect(116, 260, 100, 20))
        self.checkBox_keep_faces.setToolTip("keep construcion faces")
        self.checkBox_keep_faces.setText("keep faces")
        self.checkBox_keep_faces.setObjectName("checkBox_keep_faces")
        self.PB_RFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RFaces.setGeometry(QtCore.QRect(100, 288, 81, 28))
        self.PB_RFaces.setToolTip("remove \'in List\' Faces")
        self.PB_RFaces.setText("del Faces")
        self.PB_RFaces.setObjectName("PB_RFaces")
        self.PB_AFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_AFaces.setGeometry(QtCore.QRect(188, 288, 81, 28))
        self.PB_AFaces.setToolTip("add Faces from \'in List\' Edges")
        self.PB_AFaces.setText("add Faces")
        self.PB_AFaces.setObjectName("PB_AFaces")
        self.PB_makeShell = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeShell.setGeometry(QtCore.QRect(12, 360, 81, 28))
        self.PB_makeShell.setToolTip("make Solid from in list Faces")
        self.PB_makeShell.setText("mk Solid")
        self.PB_makeShell.setObjectName("PB_makeShell")
        self.PB_makeShell_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeShell_2.setGeometry(QtCore.QRect(100, 360, 81, 28))
        self.PB_makeShell_2.setToolTip("make Solid from the Faces\n"
"of the selected Objects")
        self.PB_makeShell_2.setText("mk Solid 2")
        self.PB_makeShell_2.setObjectName("PB_makeShell_2")
        self.PB_check_TypeId = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_check_TypeId.setGeometry(QtCore.QRect(188, 468, 81, 28))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(False)
        self.PB_check_TypeId.setFont(font)
        self.PB_check_TypeId.setToolTip("show/hide TypeId of the Shape")
        self.PB_check_TypeId.setText("? TypeId")
        self.PB_check_TypeId.setObjectName("PB_check_TypeId")
        self.Obj_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Obj_Nbr.setGeometry(QtCore.QRect(223, 104, 53, 16))
        self.Obj_Nbr.setText("0")
        self.Obj_Nbr.setObjectName("Obj_Nbr")
        self.Obj_Nbr_2 = QtGui.QLabel(self.dockWidgetContents)
        self.Obj_Nbr_2.setGeometry(QtCore.QRect(223, 236, 53, 16))
        self.Obj_Nbr_2.setText("0")
        self.Obj_Nbr_2.setObjectName("Obj_Nbr_2")
        self.PB_AEdges = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_AEdges.setGeometry(QtCore.QRect(276, 288, 81, 28))
        self.PB_AEdges.setToolTip("create a copy of the \'in List\' Edges")
        self.PB_AEdges.setText("add Edges")
        self.PB_AEdges.setObjectName("PB_AEdges")
        self.PB_showEdgeList = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_showEdgeList.setGeometry(QtCore.QRect(12, 396, 81, 28))
        self.PB_showEdgeList.setToolTip("show \'in List\' Edge(s)")
        self.PB_showEdgeList.setText("show Edges")
        self.PB_showEdgeList.setObjectName("PB_showEdgeList")
        self.PB_showFaceList = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_showFaceList.setGeometry(QtCore.QRect(100, 396, 81, 28))
        self.PB_showFaceList.setToolTip("show \'in List\' Face(s)")
        self.PB_showFaceList.setText("show Faces")
        self.PB_showFaceList.setObjectName("PB_showFaceList")
        self.PB_Refine = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Refine.setGeometry(QtCore.QRect(188, 396, 81, 28))
        self.PB_Refine.setToolTip("refine")
        self.PB_Refine.setText("Refine")
        self.PB_Refine.setObjectName("PB_Refine")
        self.PB_RefineParametric = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RefineParametric.setGeometry(QtCore.QRect(276, 396, 81, 28))
        self.PB_RefineParametric.setToolTip("parametric Refine")
        self.PB_RefineParametric.setText("prm Refine")
        self.PB_RefineParametric.setObjectName("PB_RefineParametric")
        self.PB_CFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_CFaces.setGeometry(QtCore.QRect(12, 324, 81, 28))
        self.PB_CFaces.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_CFaces.setText("cpy Faces")
        self.PB_CFaces.setObjectName("PB_CFaces")
        self.PB_TFace = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_TFace.setGeometry(QtCore.QRect(100, 324, 81, 28))
        self.PB_TFace.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_TFace.setText("offset Face")
        self.PB_TFace.setObjectName("PB_TFace")
        self.offset_input = QtGui.QLineEdit(self.dockWidgetContents)
        self.offset_input.setGeometry(QtCore.QRect(192, 328, 73, 22))
        self.offset_input.setToolTip("Face offset to apply")
        self.offset_input.setText("0.0")
        self.offset_input.setObjectName("offset_input")
        self.PB_TEdge = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_TEdge.setGeometry(QtCore.QRect(276, 324, 81, 28))
        self.PB_TEdge.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_TEdge.setText("offset Edge")
        self.PB_TEdge.setObjectName("PB_TEdge")
        self.PB_close = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_close.setGeometry(QtCore.QRect(-1, -1, 20, 20))
        self.PB_close.setToolTip("add selected Edges to List")
        self.PB_close.setText("")
        self.PB_close.setObjectName("PB_close")
        self.Version = QtGui.QLabel(self.dockWidgetContents)
        self.Version.setGeometry(QtCore.QRect(300, 0, 53, 16))
        self.Version.setText("0")
        self.Version.setObjectName("Version")
        self.PB_left = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_left.setGeometry(QtCore.QRect(-1, 17, 20, 20))
        self.PB_left.setToolTip("dock left")
        self.PB_left.setText("")
        self.PB_left.setObjectName("PB_left")
        self.PB_right = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_right.setGeometry(QtCore.QRect(-1, 34, 20, 20))
        self.PB_right.setToolTip("dock right")
        self.PB_right.setText("")
        self.PB_right.setObjectName("PB_right")
        self.PB_makeEdge = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeEdge.setGeometry(QtCore.QRect(12, 468, 81, 28))
        self.PB_makeEdge.setToolTip("make Edge from selected Vertexes")
        self.PB_makeEdge.setText("mk Edge")
        self.PB_makeEdge.setObjectName("PB_makeEdge")
        self.PB_expSTEP = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_expSTEP.setGeometry(QtCore.QRect(188, 360, 81, 28))
        self.PB_expSTEP.setToolTip("make Solid from the Faces\n"
"of the selected Objects")
        self.PB_expSTEP.setText("mk Solid 3")
        self.PB_expSTEP.setObjectName("PB_expSTEP")
        self.PB_PartDefeaturing = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_PartDefeaturing.setEnabled(False)
        self.PB_PartDefeaturing.setGeometry(QtCore.QRect(100, 468, 81, 28))
        self.PB_PartDefeaturing.setToolTip("show \'in List\' Edge(s)")
        self.PB_PartDefeaturing.setText("Defeat")
        self.PB_PartDefeaturing.setObjectName("PB_PartDefeaturing")
        self.PB_CleaningFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_CleaningFaces.setGeometry(QtCore.QRect(276, 360, 81, 28))
        self.PB_CleaningFaces.setToolTip("clean Face(s) removing\n"
"holes and merging Outwire")
        self.PB_CleaningFaces.setText("clean Faces")
        self.PB_CleaningFaces.setObjectName("PB_CleaningFaces")
        self.PB_checkS = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_checkS.setGeometry(QtCore.QRect(12, 432, 81, 28))
        self.PB_checkS.setToolTip("show \'in List\' Edge(s)")
        self.PB_checkS.setText("check Shape")
        self.PB_checkS.setObjectName("PB_checkS")
        self.tolerance_value = QtGui.QLineEdit(self.dockWidgetContents)
        self.tolerance_value.setGeometry(QtCore.QRect(192, 436, 73, 22))
        self.tolerance_value.setToolTip("Face offset to apply")
        self.tolerance_value.setText("0.0")
        self.tolerance_value.setObjectName("tolerance_value")
        self.PB_setTol = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_setTol.setGeometry(QtCore.QRect(276, 432, 81, 28))
        self.PB_setTol.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_setTol.setText("set Tol")
        self.PB_setTol.setObjectName("PB_setTol")
        self.PB_getTol = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_getTol.setGeometry(QtCore.QRect(100, 432, 81, 28))
        self.PB_getTol.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_getTol.setText("get Tol")
        self.PB_getTol.setObjectName("PB_getTol")
        self.PB_sewS = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_sewS.setGeometry(QtCore.QRect(276, 468, 81, 28))
        self.PB_sewS.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_sewS.setText("sew Shape")
        self.PB_sewS.setObjectName("PB_sewS")
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DockWidget = QtGui.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

