# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 633)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.config_layout = QtWidgets.QVBoxLayout()
        self.config_layout.setObjectName("config_layout")
        self.import_connect_layout = QtWidgets.QHBoxLayout()
        self.import_connect_layout.setObjectName("import_connect_layout")
        self.import_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.import_btn.setObjectName("import_btn")
        self.import_connect_layout.addWidget(self.import_btn)
        self.connect_status_layout = QtWidgets.QHBoxLayout()
        self.connect_status_layout.setObjectName("connect_status_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connect_status_layout.addItem(spacerItem)
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.connect_btn.setObjectName("connect_btn")
        self.connect_status_layout.addWidget(self.connect_btn)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.status_label.setObjectName("status_label")
        self.connect_status_layout.addWidget(self.status_label)
        self.import_connect_layout.addLayout(self.connect_status_layout)
        self.config_layout.addLayout(self.import_connect_layout)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.config_layout.addWidget(self.line_8)
        self.exp_layout = QtWidgets.QHBoxLayout()
        self.exp_layout.setObjectName("exp_layout")
        self.exp_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.exp_line_edit.setText("")
        self.exp_line_edit.setObjectName("exp_line_edit")
        self.exp_layout.addWidget(self.exp_line_edit)
        self.ch_conf_layout = QtWidgets.QHBoxLayout()
        self.ch_conf_layout.setObjectName("ch_conf_layout")
        self.input_ch_layout = QtWidgets.QHBoxLayout()
        self.input_ch_layout.setObjectName("input_ch_layout")
        self.input_ch_label = QtWidgets.QLabel(self.centralwidget)
        self.input_ch_label.setObjectName("input_ch_label")
        self.input_ch_layout.addWidget(self.input_ch_label)
        self.n_channel_label = QtWidgets.QLabel(self.centralwidget)
        self.n_channel_label.setObjectName("n_channel_label")
        self.input_ch_layout.addWidget(self.n_channel_label)
        self.ch_conf_layout.addLayout(self.input_ch_layout)
        self.output_ch_layout = QtWidgets.QHBoxLayout()
        self.output_ch_layout.setObjectName("output_ch_layout")
        self.output_ch_label = QtWidgets.QLabel(self.centralwidget)
        self.output_ch_label.setObjectName("output_ch_label")
        self.output_ch_layout.addWidget(self.output_ch_label)
        self.output_ch_input = QtWidgets.QSpinBox(self.centralwidget)
        self.output_ch_input.setMinimum(1)
        self.output_ch_input.setMaximum(15)
        self.output_ch_input.setProperty("value", 6)
        self.output_ch_input.setObjectName("output_ch_input")
        self.output_ch_layout.addWidget(self.output_ch_input)
        self.ch_conf_layout.addLayout(self.output_ch_layout)
        self.exp_layout.addLayout(self.ch_conf_layout)
        self.config_layout.addLayout(self.exp_layout)
        self.verticalLayout_10.addLayout(self.config_layout)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_10.addWidget(self.line_4)
        self.inputs_main_layout = QtWidgets.QVBoxLayout()
        self.inputs_main_layout.setObjectName("inputs_main_layout")
        self.inputs_label = QtWidgets.QLabel(self.centralwidget)
        self.inputs_label.setObjectName("inputs_label")
        self.inputs_main_layout.addWidget(self.inputs_label)
        self.inputs_layout = QtWidgets.QHBoxLayout()
        self.inputs_layout.setObjectName("inputs_layout")
        self.machine_in_layout = QtWidgets.QVBoxLayout()
        self.machine_in_layout.setObjectName("machine_in_layout")
        self.maquina_label = QtWidgets.QLabel(self.centralwidget)
        self.maquina_label.setObjectName("maquina_label")
        self.machine_in_layout.addWidget(self.maquina_label)
        self.machine_in_form = QtWidgets.QFormLayout()
        self.machine_in_form.setObjectName("machine_in_form")
        self.v_label = QtWidgets.QLabel(self.centralwidget)
        self.v_label.setObjectName("v_label")
        self.machine_in_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.v_label)
        self.v_in = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.v_in.setObjectName("v_in")
        self.machine_in_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.v_in)
        self.current_label = QtWidgets.QLabel(self.centralwidget)
        self.current_label.setObjectName("current_label")
        self.machine_in_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.current_label)
        self.current_in = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.current_in.setObjectName("current_in")
        self.machine_in_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.current_in)
        self.machine_in_layout.addLayout(self.machine_in_form)
        self.inputs_layout.addLayout(self.machine_in_layout)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.inputs_layout.addWidget(self.line_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.canales_label = QtWidgets.QLabel(self.centralwidget)
        self.canales_label.setObjectName("canales_label")
        self.verticalLayout_4.addWidget(self.canales_label)
        self.flux_grid = QtWidgets.QGridLayout()
        self.flux_grid.setObjectName("flux_grid")
        self.ch1_in_label = QtWidgets.QLabel(self.centralwidget)
        self.ch1_in_label.setObjectName("ch1_in_label")
        self.flux_grid.addWidget(self.ch1_in_label, 1, 1, 1, 1)
        self.flux_label = QtWidgets.QLabel(self.centralwidget)
        self.flux_label.setObjectName("flux_label")
        self.flux_grid.addWidget(self.flux_label, 2, 0, 1, 1)
        self.ch1_in = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ch1_in.setObjectName("ch1_in")
        self.flux_grid.addWidget(self.ch1_in, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.flux_grid)
        self.inputs_layout.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.inputs_layout.addItem(spacerItem1)
        self.inputs_main_layout.addLayout(self.inputs_layout)
        self.verticalLayout_10.addLayout(self.inputs_main_layout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setObjectName("graph_layout")
        self.out_graph = PlotWidget(self.centralwidget)
        self.out_graph.setEnabled(True)
        self.out_graph.setObjectName("out_graph")
        self.graph_layout.addWidget(self.out_graph)
        self.verticalLayout_10.addLayout(self.graph_layout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.outputs_main_layout = QtWidgets.QVBoxLayout()
        self.outputs_main_layout.setObjectName("outputs_main_layout")
        self.outputs_label = QtWidgets.QLabel(self.centralwidget)
        self.outputs_label.setObjectName("outputs_label")
        self.outputs_main_layout.addWidget(self.outputs_label)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.outputs_main_layout.addWidget(self.line_6)
        self.channels_out_layout = QtWidgets.QVBoxLayout()
        self.channels_out_layout.setObjectName("channels_out_layout")
        self.ch_out_label = QtWidgets.QLabel(self.centralwidget)
        self.ch_out_label.setObjectName("ch_out_label")
        self.channels_out_layout.addWidget(self.ch_out_label)
        self.ch_grid_layout = QtWidgets.QHBoxLayout()
        self.ch_grid_layout.setObjectName("ch_grid_layout")
        self.temp_q_grid = QtWidgets.QGridLayout()
        self.temp_q_grid.setObjectName("temp_q_grid")
        self.q_out_label = QtWidgets.QLabel(self.centralwidget)
        self.q_out_label.setObjectName("q_out_label")
        self.temp_q_grid.addWidget(self.q_out_label, 3, 0, 1, 1)
        self.temp_out_label = QtWidgets.QLabel(self.centralwidget)
        self.temp_out_label.setObjectName("temp_out_label")
        self.temp_q_grid.addWidget(self.temp_out_label, 2, 0, 1, 1)
        self.ch1_out_label = QtWidgets.QLabel(self.centralwidget)
        self.ch1_out_label.setObjectName("ch1_out_label")
        self.temp_q_grid.addWidget(self.ch1_out_label, 1, 1, 1, 1)
        self.ch1_t_label = QtWidgets.QLabel(self.centralwidget)
        self.ch1_t_label.setObjectName("ch1_t_label")
        self.temp_q_grid.addWidget(self.ch1_t_label, 2, 1, 1, 1)
        self.ch1_q_label = QtWidgets.QLabel(self.centralwidget)
        self.ch1_q_label.setObjectName("ch1_q_label")
        self.temp_q_grid.addWidget(self.ch1_q_label, 3, 1, 1, 1)
        self.ch_grid_layout.addLayout(self.temp_q_grid)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ch_grid_layout.addItem(spacerItem2)
        self.channels_out_layout.addLayout(self.ch_grid_layout)
        self.outputs_main_layout.addLayout(self.channels_out_layout)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.outputs_main_layout.addWidget(self.line_7)
        self.calc_layout = QtWidgets.QVBoxLayout()
        self.calc_layout.setObjectName("calc_layout")
        self.calculos_label = QtWidgets.QLabel(self.centralwidget)
        self.calculos_label.setObjectName("calculos_label")
        self.calc_layout.addWidget(self.calculos_label)
        self.calc_form = QtWidgets.QFormLayout()
        self.calc_form.setObjectName("calc_form")
        self.p_out = QtWidgets.QLabel(self.centralwidget)
        self.p_out.setObjectName("p_out")
        self.calc_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.p_out)
        self.q_tot_label = QtWidgets.QLabel(self.centralwidget)
        self.q_tot_label.setObjectName("q_tot_label")
        self.calc_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.q_tot_label)
        self.q_tot_out = QtWidgets.QLabel(self.centralwidget)
        self.q_tot_out.setObjectName("q_tot_out")
        self.calc_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.q_tot_out)
        self.eff_label = QtWidgets.QLabel(self.centralwidget)
        self.eff_label.setObjectName("eff_label")
        self.calc_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.eff_label)
        self.eff_out = QtWidgets.QLabel(self.centralwidget)
        self.eff_out.setObjectName("eff_out")
        self.calc_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.eff_out)
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setObjectName("p_label")
        self.calc_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.p_label)
        self.calc_layout.addLayout(self.calc_form)
        self.outputs_main_layout.addLayout(self.calc_layout)
        self.verticalLayout_10.addLayout(self.outputs_main_layout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.buttons_main_layout = QtWidgets.QVBoxLayout()
        self.buttons_main_layout.setObjectName("buttons_main_layout")
        self.timer_layout = QtWidgets.QHBoxLayout()
        self.timer_layout.setObjectName("timer_layout")
        self.placeholder_widget = QtWidgets.QWidget(self.centralwidget)
        self.placeholder_widget.setObjectName("placeholder_widget")
        self.timer_layout.addWidget(self.placeholder_widget)
        self.buttons_main_layout.addLayout(self.timer_layout)
        self.start_stop_res_layout = QtWidgets.QHBoxLayout()
        self.start_stop_res_layout.setObjectName("start_stop_res_layout")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.start_stop_res_layout.addWidget(self.start_btn)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.start_stop_res_layout.addWidget(self.stop_btn)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setObjectName("reset_btn")
        self.start_stop_res_layout.addWidget(self.reset_btn)
        self.buttons_main_layout.addLayout(self.start_stop_res_layout)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.buttons_main_layout.addWidget(self.save_btn)
        self.verticalLayout_10.addLayout(self.buttons_main_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CCHEN APP"))
        self.import_btn.setText(_translate("MainWindow", "importar"))
        self.connect_btn.setText(_translate("MainWindow", "Conectar"))
        self.status_label.setText(_translate("MainWindow", "Status"))
        self.exp_line_edit.setPlaceholderText(_translate("MainWindow", "Experimento #"))
        self.input_ch_label.setText(_translate("MainWindow", "Input Channels:"))
        self.n_channel_label.setText(_translate("MainWindow", "1"))
        self.output_ch_label.setText(_translate("MainWindow", "Output Channels:"))
        self.inputs_label.setText(_translate("MainWindow", "Inputs:"))
        self.maquina_label.setText(_translate("MainWindow", "Maquina:"))
        self.v_label.setText(_translate("MainWindow", "Voltaje:"))
        self.current_label.setText(_translate("MainWindow", "Corriente:"))
        self.canales_label.setText(_translate("MainWindow", "Canales:"))
        self.ch1_in_label.setText(_translate("MainWindow", "CH1:"))
        self.flux_label.setText(_translate("MainWindow", "Flujo:"))
        self.outputs_label.setText(_translate("MainWindow", "Outputs:"))
        self.ch_out_label.setText(_translate("MainWindow", "Canales:"))
        self.q_out_label.setText(_translate("MainWindow", "Q:"))
        self.temp_out_label.setText(_translate("MainWindow", "Temperatura:"))
        self.ch1_out_label.setText(_translate("MainWindow", "CH1:"))
        self.ch1_t_label.setText(_translate("MainWindow", "empty"))
        self.ch1_q_label.setText(_translate("MainWindow", "empty"))
        self.calculos_label.setText(_translate("MainWindow", "Calculos:"))
        self.p_out.setText(_translate("MainWindow", "Empty"))
        self.q_tot_label.setText(_translate("MainWindow", "Q total:"))
        self.q_tot_out.setText(_translate("MainWindow", "Empty"))
        self.eff_label.setText(_translate("MainWindow", "Eficiencia:"))
        self.eff_out.setText(_translate("MainWindow", "Empty"))
        self.p_label.setText(_translate("MainWindow", "Potencia Maquina:"))
        self.start_btn.setText(_translate("MainWindow", "start"))
        self.stop_btn.setText(_translate("MainWindow", "stop"))
        self.reset_btn.setText(_translate("MainWindow", "reset"))
        self.save_btn.setText(_translate("MainWindow", "save"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
from pyqtgraph import PlotWidget
