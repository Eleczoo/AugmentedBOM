EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Garden Wemos"
Date "2019-05-19"
Rev "1.0"
Comp "ThePurpleCompagny"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L wemos_mini:WeMos_mini U3
U 1 1 5CE19146
P 6500 4000
F 0 "U3" H 6500 4625 60  0000 C CNN
F 1 "WeMos_mini" H 6525 4525 60  0000 C CNN
F 2 "Module:WEMOS_D1_mini_light" H 7050 3300 60  0001 C CNN
F 3 "http://www.wemos.cc/Products/d1_mini.html" H 6500 4531 60  0001 C CNN
	1    6500 4000
	1    0    0    -1  
$EndComp
$Comp
L 4xxx:4051 U4
U 1 1 5CE1A1EC
P 8975 4375
F 0 "U4" H 9325 4425 50  0000 L CNN
F 1 "4051" H 9300 4350 50  0000 L CNN
F 2 "Package_DIP:DIP-16_W7.62mm_Socket_LongPads" H 8975 4375 50  0001 C CNN
F 3 "http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4051bms-52bms-53bms.pdf" H 8975 4375 50  0001 C CNN
	1    8975 4375
	1    0    0    -1  
$EndComp
$Comp
L My_symbols:MoistSensor U2
U 1 1 5CE220CB
P 4150 3425
F 0 "U2" H 3708 3550 50  0000 C CNN
F 1 "MoistSensor" H 3708 3459 50  0000 C CNN
F 2 "Connectorss:Fan_Pin_Header_Straight_1x03" H 4150 3425 50  0001 C CNN
F 3 "" H 4150 3425 50  0001 C CNN
	1    4150 3425
	1    0    0    -1  
$EndComp
$Comp
L SYMBOLES_LIB:PHOTO.R R1
U 1 1 5CE231BE
P 3725 1950
F 0 "R1" V 3672 2106 60  0000 L CNN
F 1 "PHOTO.R" V 3778 2106 60  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Vertical" V 3725 1950 60  0001 C CNN
F 3 "" V 3725 1950 60  0001 C CNN
	1    3725 1950
	0    1    1    0   
$EndComp
$Comp
L gardenWemos-rescue:R-device R2
U 1 1 5CE24388
P 3725 2550
F 0 "R2" H 3795 2596 50  0000 L CNN
F 1 "10k" H 3795 2505 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 3655 2550 50  0001 C CNN
F 3 "" H 3725 2550 50  0001 C CNN
	1    3725 2550
	1    0    0    -1  
$EndComp
$Comp
L gardenWemos-rescue:DHT11-sensors U1
U 1 1 5CE256F1
P 3725 5400
F 0 "U1" V 3360 5400 50  0000 C CNN
F 1 "DHT11" V 3451 5400 50  0000 C CNN
F 2 "Sensor:Aosong_DHT11_5.5x12.0_P2.54mm" H 3875 5650 50  0001 C CNN
F 3 "http://akizukidenshi.com/download/ds/aosong/DHT11.pdf" H 3875 5650 50  0001 C CNN
	1    3725 5400
	0    1    1    0   
$EndComp
$Comp
L gardenWemos-rescue:R-device R3
U 1 1 5CE26F9F
P 4225 5550
F 0 "R3" H 4295 5596 50  0000 L CNN
F 1 "10k" H 4295 5505 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 4155 5550 50  0001 C CNN
F 3 "" H 4225 5550 50  0001 C CNN
	1    4225 5550
	1    0    0    -1  
$EndComp
$Comp
L gardenWemos-rescue:C-device C1
U 1 1 5CE273F8
P 3725 4850
F 0 "C1" V 3473 4850 50  0000 C CNN
F 1 "1u" V 3564 4850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 3763 4700 50  0001 C CNN
F 3 "" H 3725 4850 50  0001 C CNN
	1    3725 4850
	0    1    1    0   
$EndComp
Wire Wire Line
	4025 5300 4225 5300
Wire Wire Line
	4225 5300 4225 5400
Wire Wire Line
	3725 5700 3725 5775
Wire Wire Line
	3725 5775 4225 5775
Wire Wire Line
	4225 5775 4225 5700
Wire Wire Line
	3875 4850 4225 4850
Wire Wire Line
	4225 4850 4225 5300
Connection ~ 4225 5300
Wire Wire Line
	3575 4850 3200 4850
Wire Wire Line
	3200 4850 3200 5300
Wire Wire Line
	3200 5300 3425 5300
$Comp
L gardenWemos-rescue:GND-power #PWR0101
U 1 1 5CE2F994
P 5200 3900
F 0 "#PWR0101" H 5200 3650 50  0001 C CNN
F 1 "GND" H 5205 3727 50  0000 C CNN
F 2 "" H 5200 3900 50  0001 C CNN
F 3 "" H 5200 3900 50  0001 C CNN
	1    5200 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 3650 6000 3650
$Comp
L gardenWemos-rescue:+5V-power #PWR0102
U 1 1 5CE2FE91
P 5200 3500
F 0 "#PWR0102" H 5200 3350 50  0001 C CNN
F 1 "+5V" H 5215 3673 50  0000 C CNN
F 2 "" H 5200 3500 50  0001 C CNN
F 3 "" H 5200 3500 50  0001 C CNN
	1    5200 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 3650 5200 3500
Wire Wire Line
	6000 3750 5200 3750
Wire Wire Line
	5200 3750 5200 3900
Text Label 5900 3650 2    50   ~ 0
+5V
Text Label 5900 3750 2    50   ~ 0
GND
Text Label 3850 5775 0    50   ~ 0
IO_DHT
Wire Wire Line
	4350 3725 4475 3725
Wire Wire Line
	4350 3625 4475 3625
Wire Wire Line
	4350 3525 4475 3525
Text Label 4475 3625 0    50   ~ 0
+5V
Text Label 4475 3525 0    50   ~ 0
GND
Text Label 8350 3775 2    50   ~ 0
Moisture1
$Comp
L gardenWemos-rescue:GND-power #PWR0103
U 1 1 5CE3B6F2
P 3725 2825
F 0 "#PWR0103" H 3725 2575 50  0001 C CNN
F 1 "GND" H 3730 2652 50  0000 C CNN
F 2 "" H 3725 2825 50  0001 C CNN
F 3 "" H 3725 2825 50  0001 C CNN
	1    3725 2825
	1    0    0    -1  
$EndComp
$Comp
L gardenWemos-rescue:+5V-power #PWR0104
U 1 1 5CE3BF5E
P 3725 1625
F 0 "#PWR0104" H 3725 1475 50  0001 C CNN
F 1 "+5V" H 3740 1798 50  0000 C CNN
F 2 "" H 3725 1625 50  0001 C CNN
F 3 "" H 3725 1625 50  0001 C CNN
	1    3725 1625
	1    0    0    -1  
$EndComp
Wire Wire Line
	3725 1625 3725 1750
Wire Wire Line
	3725 2150 3725 2275
Wire Wire Line
	3725 2700 3725 2825
Wire Wire Line
	3725 2275 3900 2275
Connection ~ 3725 2275
Wire Wire Line
	3725 2275 3725 2400
Text Label 3900 2275 0    50   ~ 0
LightOut
Text Label 8350 3875 2    50   ~ 0
Moisture2
Wire Wire Line
	8475 3775 8350 3775
Wire Wire Line
	8350 3875 8475 3875
Wire Wire Line
	8475 4675 8350 4675
Wire Wire Line
	8350 4775 8475 4775
Wire Wire Line
	8475 4875 8350 4875
Wire Wire Line
	8475 4975 8350 4975
Wire Wire Line
	7000 4250 7125 4250
Text Label 7125 4250 0    50   ~ 0
AnalogInput
Wire Wire Line
	6000 3850 5875 3850
Text Label 5875 3850 2    50   ~ 0
IO_DHT
Wire Wire Line
	7000 4150 7125 4150
Text Label 7125 3850 0    50   ~ 0
inh
Text Label 8350 4775 2    50   ~ 0
A
Text Label 8350 4875 2    50   ~ 0
B
Text Label 8350 4975 2    50   ~ 0
C
Text Label 9600 3775 0    50   ~ 0
AnalogInput
Wire Wire Line
	9475 3775 9600 3775
$Comp
L gardenWemos-rescue:GND-power #PWR0105
U 1 1 5CE49A43
P 9025 5400
F 0 "#PWR0105" H 9025 5150 50  0001 C CNN
F 1 "GND" H 9030 5227 50  0000 C CNN
F 2 "" H 9025 5400 50  0001 C CNN
F 3 "" H 9025 5400 50  0001 C CNN
	1    9025 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	9075 5275 9075 5325
Wire Wire Line
	9075 5325 9025 5325
Wire Wire Line
	9025 5325 9025 5400
Wire Wire Line
	8975 5275 8975 5325
Wire Wire Line
	8975 5325 9025 5325
Connection ~ 9025 5325
$Comp
L gardenWemos-rescue:+5V-power #PWR0106
U 1 1 5CE4B9DE
P 8975 3350
F 0 "#PWR0106" H 8975 3200 50  0001 C CNN
F 1 "+5V" H 8990 3523 50  0000 C CNN
F 2 "" H 8975 3350 50  0001 C CNN
F 3 "" H 8975 3350 50  0001 C CNN
	1    8975 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	8975 3475 8975 3350
Wire Wire Line
	7125 4050 7000 4050
Wire Wire Line
	7000 3950 7125 3950
Wire Wire Line
	7000 3850 7125 3850
Text Label 7125 4150 0    50   ~ 0
A
Text Label 7125 4050 0    50   ~ 0
B
Text Label 7125 3950 0    50   ~ 0
C
Text Label 8350 4675 2    50   ~ 0
inh
NoConn ~ 8475 4075
NoConn ~ 8475 4175
NoConn ~ 8475 4275
NoConn ~ 8475 4375
NoConn ~ 8475 4475
NoConn ~ 7000 3650
NoConn ~ 7000 4350
NoConn ~ 6000 4350
NoConn ~ 6000 4250
NoConn ~ 6000 3950
$Comp
L gardenWemos-rescue:Conn_01x01_Female-Connector J1
U 1 1 5CE56954
P 5425 4050
F 0 "J1" H 5375 4000 50  0000 C CNN
F 1 "Conn_01x01_Female" H 5317 3916 50  0001 C CNN
F 2 "Connectorss:Pin_d1.0mm_L10.0mm" H 5425 4050 50  0001 C CNN
F 3 "~" H 5425 4050 50  0001 C CNN
	1    5425 4050
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 4050 5625 4050
$Comp
L gardenWemos-rescue:Conn_01x01_Female-Connector J2
U 1 1 5CE58873
P 5425 4150
F 0 "J2" H 5375 4100 50  0000 C CNN
F 1 "Conn_01x01_Female" H 5317 4016 50  0001 C CNN
F 2 "Connectorss:Pin_d1.0mm_L10.0mm" H 5425 4150 50  0001 C CNN
F 3 "~" H 5425 4150 50  0001 C CNN
	1    5425 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 4150 5625 4150
Text Label 5875 4050 2    50   ~ 0
SCL
Text Label 5875 4150 2    50   ~ 0
SDA
$Comp
L gardenWemos-rescue:Screw_Terminal_01x02-Connector J3
U 1 1 5CE514BE
P 9425 2275
F 0 "J3" H 9505 2221 50  0000 L CNN
F 1 "Screw_Terminal_01x02" V 9298 2087 50  0001 R CNN
F 2 "TerminalBlock:TerminalBlock_Wuerth_691311400102_P7.62mm" H 9425 2275 50  0001 C CNN
F 3 "~" H 9425 2275 50  0001 C CNN
	1    9425 2275
	1    0    0    -1  
$EndComp
$Comp
L My_symbols:MoistSensor U5
U 1 1 5CE58BE1
P 4150 4000
F 0 "U5" H 3708 4125 50  0000 C CNN
F 1 "MoistSensor" H 3708 4034 50  0000 C CNN
F 2 "Connectorss:Fan_Pin_Header_Straight_1x03" H 4150 4000 50  0001 C CNN
F 3 "" H 4150 4000 50  0001 C CNN
	1    4150 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 4300 4475 4300
Wire Wire Line
	4350 4200 4475 4200
Wire Wire Line
	4350 4100 4475 4100
Text Label 4475 4200 0    50   ~ 0
+5V
Text Label 4475 4100 0    50   ~ 0
GND
Wire Wire Line
	8475 3975 8350 3975
Text Label 8350 3975 2    50   ~ 0
LightOut
$Comp
L gardenWemos-rescue:Q_NMOS_GSD-device Q1
U 1 1 5CE60364
P 8875 1950
F 0 "Q1" H 9081 1996 50  0000 L CNN
F 1 "NTR4003NT1G" H 9081 1905 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 9075 2050 50  0001 C CNN
F 3 "" H 8875 1950 50  0001 C CNN
	1    8875 1950
	1    0    0    -1  
$EndComp
$Comp
L gardenWemos-rescue:GND-power #PWR0107
U 1 1 5CE728AB
P 8975 2500
F 0 "#PWR0107" H 8975 2250 50  0001 C CNN
F 1 "GND" H 8980 2327 50  0000 C CNN
F 2 "" H 8975 2500 50  0001 C CNN
F 3 "" H 8975 2500 50  0001 C CNN
	1    8975 2500
	1    0    0    -1  
$EndComp
$Comp
L gardenWemos-rescue:+5V-power #PWR0108
U 1 1 5CE7C027
P 8975 1625
F 0 "#PWR0108" H 8975 1475 50  0001 C CNN
F 1 "+5V" H 8990 1798 50  0000 C CNN
F 2 "" H 8975 1625 50  0001 C CNN
F 3 "" H 8975 1625 50  0001 C CNN
	1    8975 1625
	1    0    0    -1  
$EndComp
Wire Wire Line
	8975 2150 8975 2275
Wire Wire Line
	8975 2275 9225 2275
Wire Wire Line
	9225 2375 8975 2375
Wire Wire Line
	8975 2375 8975 2500
Wire Wire Line
	8975 1625 8975 1750
Wire Wire Line
	7000 3750 7125 3750
Text Label 7125 3750 0    50   ~ 0
WaterPump
Text Label 8525 1950 2    50   ~ 0
WaterPump
Text Label 4475 3725 0    50   ~ 0
Moisture1
Text Label 4475 4300 0    50   ~ 0
Moisture2
$Comp
L gardenWemos-rescue:R-device R4
U 1 1 5CE5AF5F
P 8600 2275
F 0 "R4" H 8670 2321 50  0000 L CNN
F 1 "10k" H 8670 2230 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 8530 2275 50  0001 C CNN
F 3 "" H 8600 2275 50  0001 C CNN
	1    8600 2275
	1    0    0    -1  
$EndComp
Wire Wire Line
	8600 2425 8600 2500
Wire Wire Line
	8525 1950 8600 1950
Wire Wire Line
	8600 2125 8600 1950
Connection ~ 8600 1950
Wire Wire Line
	8600 1950 8675 1950
$Comp
L gardenWemos-rescue:GND-power #PWR0109
U 1 1 5CE5F74E
P 8600 2500
F 0 "#PWR0109" H 8600 2250 50  0001 C CNN
F 1 "GND" H 8605 2327 50  0000 C CNN
F 2 "" H 8600 2500 50  0001 C CNN
F 3 "" H 8600 2500 50  0001 C CNN
	1    8600 2500
	1    0    0    -1  
$EndComp
Text Label 4225 4850 2    50   ~ 0
+5V
$EndSCHEMATC
