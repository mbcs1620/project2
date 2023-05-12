from PyQt5.QtWidgets import *
from view2 import *
from PyQt5.QtGui import QPixmap
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

distance = ''
convert_from = ''
convert_to = ''


class Controller(QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())


        self.label_finalconversion.setText('')
        self.radio_scy1.setChecked(True)
        self.radio_scy2.setChecked(True)
        self.radio_50.setChecked(True)

        self.add_image()

    def add_image(self):
        Qpixmap = QPixmap('background.jpg')
        self.label_picture.setPixmap(Qpixmap)


    def submit(self):

        global distance
        global convert_from
        global convert_to

        for x in ['50', '100', '200', '500', '1000', '1500']:
            radio_button = getattr(self, f'radio_{x}')
            if radio_button.isChecked():
                distance = x

        for y in ['scy', 'scm', 'lcm']:
            radio_button = getattr(self, f'radio_{y}1')
            if radio_button.isChecked():
                convert_from = y

        for z in ['scy', 'scm', 'lcm']:
            radio_button = getattr(self, f'radio_{z}2')
            if radio_button.isChecked():
                convert_to = z


        minutes = self.input_minutes.text()
        seconds = self.input_seconds.text()
        hundredths = self.input_hundredths.text()
        self.label_error.setText('')
        
        try:
            if int(minutes) < 0 or int(minutes) > 59:
                self.label_error.setText('PLEASE ENTER NUMBERS FROM 0 TO 59!')
                self.input_minutes.setText('')

            if int(seconds) < 0 or int(seconds) > 59:
                self.label_error.setText('PLEASE ENTER NUMBERS FROM 0 TO 59!')
                self.input_seconds.setText('')

            if int(hundredths) < 0 or int(hundredths) > 100:
                self.label_error.setText('PLEASE ENTER NUMBERS FROM 0 TO 100!')
                self.input_hundredths.setText('')

            else:
                final_time = (60 * (int(minutes))) + (1 * (int(seconds))) + (0.01 * (int(hundredths)))

        except:
            self.label_error.setText('PLEASE ENTER NUMERICAL WHOLE NUMBERS!')
            self.input_minutes.setText('')
            self.input_seconds.setText('')
            self.input_hundredths.setText('')




        try:
            minutes_int = int(minutes)
            seconds_int = int(seconds)
            hundredths_int = int(hundredths)

            if convert_from == 'scy':
                if convert_to == 'scy':
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCY race\n is {minutes_int}:{final_seconds}.{final_hundredths} in SCY')
                    
                elif convert_to == 'scm':
                    final_list = self.time_convert(self.scy_scm(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCY race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in SCM')
                else:
                    final_list = self.time_convert(self.scy_lcm(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCY race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in LCM')

            elif convert_from == 'scm':
                if convert_to == 'scm':
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int

                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCM race\n is {minutes_int}:{final_seconds}.{final_hundredths} in SCM')
                elif convert_to == 'scy':
                    final_list = self.time_convert(self.scm_scy(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCM race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in SCY')
                else:
                    final_list = self.time_convert(self.scm_lcm(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} SCM race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in LCM')

            else:
                if convert_to == 'lcm':
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} LCM race\n is {minutes_int}:{final_seconds}.{final_hundredths} in LCM')
                elif convert_to == 'scy':
                    final_list = self.time_convert(self.lcm_scy(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} LCM race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in SCY')
                else:
                    final_list = self.time_convert(self.lcm_scm(float(final_time)))
                    if seconds_int < 10 or hundredths_int < 10:
                        if seconds_int < 10:
                            time_str = str(seconds_int)
                            final_seconds = '0'+ time_str
            
                        if hundredths_int < 10:
                            time_str = str(hundredths_int)
                            final_hundredths = '0'+ time_str
                    if seconds_int >= 10:
                        final_seconds = seconds_int
                    if hundredths_int >= 10:
                        final_hundredths = hundredths_int
                    self.label_finalconversion.setText(f'{minutes_int}:{final_seconds}.{final_hundredths} for a {distance} LCM race\n is {final_list[0]}:{final_list[1]}.{final_list[2]} in SCM')
                    
            self.input_minutes.hide()
            self.input_seconds.hide()
            self.input_hundredths.hide()
            self.button_submit.hide()
            self.label.hide()
            self.label_error.hide()
            self.label_prompt1.hide()
            self.label_prompt2.hide()
            self.label_prompt3.hide()
            self.label_prompt4.hide()
            self.radio_50.hide()
            self.radio_100.hide()
            self.radio_200.hide()
            self.radio_500.hide()
            self.radio_1000.hide()
            self.radio_1500.hide()
            self.radio_lcm1.hide()
            self.radio_lcm2.hide()
            self.radio_scm1.hide()
            self.radio_scm2.hide()
            self.radio_scy1.hide()
            self.radio_scy2.hide()
            


        except:
            self.label_error.setText('PLEASE ENTER NUMERICAL WHOLE NUMBERS!')
            self.input_minutes.setText('')
            self.input_seconds.setText('')
            self.input_hundredths.setText('')



    def scy_scm(self, seconds):
        final_time = seconds * 1.11
        return final_time

    def scy_lcm(self,seconds):
        final_time = (seconds * 1.11) + (0.02*(seconds * 1.11))
        return final_time

    def scm_scy(self,seconds):
        final_time = seconds * 0.89
        return final_time

    def scm_lcm(self,seconds):
        final_time = (0.02*(seconds)) + (seconds)
        return final_time

    def lcm_scy(self,seconds):
        final_time = ((seconds) * 0.89) - (0.02*((seconds) * 0.89))
        return final_time

    def lcm_scm(self,seconds):
        final_time = (seconds) - (0.02*(seconds))
        return final_time

    def time_convert(self, final_time):
        minutes = final_time // 60
        final_time %= 60
        hundredths = final_time % 1 * 100
        
        if final_time < 10 or hundredths < 10:
            if final_time < 10:
                floor_time = math.floor(final_time)
                time_str = str(floor_time)
                final_seconds = '0'+ time_str
                return math.floor(minutes), final_seconds, round(hundredths)
            
            else:
                round_time = round(hundredths)
                time_str = str(round_time)
                final_hundredths = '0'+ time_str
                return math.floor(minutes), math.floor(final_time), final_hundredths
        else:
            return math.floor(minutes), math.floor(final_time), round(hundredths)

