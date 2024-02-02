import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template= """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Map_2</class>
 <widget class="QMainWindow" name="Map_2">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>787</width>
    <height>534</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QComboBox" name="VidCarti">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>40</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <item>
     <property name="text">
      <string>Спутник</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Схема</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Гибрид</string>
     </property>
    </item>
   </widget>
   <widget class="QCheckBox" name="Adr1">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>90</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Адресс</string>
    </property>
   </widget>
   <widget class="QLabel" name="Adrtext">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>450</y>
      <width>101</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>50</weight>
      <italic>false</italic>
      <bold>false</bold>
      <underline>false</underline>
     </font>
    </property>
    <property name="text">
     <string>Адресс :</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>40</y>
      <width>81</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>13</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Поиск:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="Poiskstorka">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>40</y>
      <width>441</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="Poisk">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>40</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Найти</string>
    </property>
   </widget>
   <widget class="QLabel" name="Map">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>100</y>
      <width>531</width>
      <height>321</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="AdrVivod">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>450</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Map.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        pass
        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())