<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>130</y>
      <width>271</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>36</pointsize>
     </font>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuFile">
    <property name="title">
     <string>File</string>
    </property>
    <addaction name="actionNew"/>
    <addaction name="actionSave"/>
   </widget>
   <widget class="QMenu" name="menuEdit">
    <property name="title">
     <string>Edit</string>
    </property>
    <addaction name="actionCopy"/>
    <addaction name="actionPaste"/>
   </widget>
   <addaction name="menuFile"/>
   <addaction name="menuEdit"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionNew">
   <property name="text">
    <string>New</string>
   </property>
   <property name="statusTip">
    <string>Create New File</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+N</string>
   </property>
  </action>
  <action name="actionSave">
   <property name="text">
    <string>Save</string>
   </property>
   <property name="statusTip">
    <string>Save File</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+S</string>
   </property>
  </action>
  <action name="actionCopy">
   <property name="text">
    <string>Copy</string>
   </property>
   <property name="statusTip">
    <string>Copy a File</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+C</string>
   </property>
  </action>
  <action name="actionPaste">
   <property name="text">
    <string>Paste</string>
   </property>
   <property name="statusTip">
    <string>Paste a file</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+V</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
