EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "F38C_U2S"
Date "2019-6-18"
Rev "1.0"
Comp "CFPT - Ecole d'Electronique"
Comment1 "Nicolas Albanesi"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L F38C_U2S-rescue:8051F38C-My_symbols U2
U 1 1 5D08FA92
P 6900 3800
F 0 "U2" H 6600 4700 50  0000 C CNN
F 1 "8051F38C" H 7100 4700 50  0000 C CNN
F 2 "Package_QFP:LQFP-32_7x7mm_P0.8mm" H 7000 3700 50  0001 C CNN
F 3 "" H 7000 3700 50  0001 C CNN
	1    6900 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5D090366
P 10000 1000
F 0 "R4" V 9900 950 50  0000 L CNN
F 1 "1k" V 10000 950 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9930 1000 50  0001 C CNN
F 3 "~" H 10000 1000 50  0001 C CNN
	1    10000 1000
	0    1    1    0   
$EndComp
$Comp
L Device:LED D1
U 1 1 5D0A3413
P 10450 1000
F 0 "D1" H 10450 900 50  0000 C CNN
F 1 "LED" H 10441 1125 50  0001 C CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 10450 1000 50  0001 C CNN
F 3 "~" H 10450 1000 50  0001 C CNN
	1    10450 1000
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR016
U 1 1 5D0A3A3E
P 6900 4900
F 0 "#PWR016" H 6900 4650 50  0001 C CNN
F 1 "GND" H 6905 4727 50  0000 C CNN
F 2 "" H 6900 4900 50  0001 C CNN
F 3 "" H 6900 4900 50  0001 C CNN
	1    6900 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 4800 6900 4900
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J2
U 1 1 5D0A7D67
P 4100 5000
F 0 "J2" H 4150 5325 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 4150 5326 50  0001 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Horizontal" H 4100 5000 50  0001 C CNN
F 3 "~" H 4100 5000 50  0001 C CNN
	1    4100 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5D0A7DC9
P 1900 4800
F 0 "R1" H 1970 4846 50  0000 L CNN
F 1 "1k" H 1970 4755 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 1830 4800 50  0001 C CNN
F 3 "~" H 1900 4800 50  0001 C CNN
	1    1900 4800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5D0A7E56
P 2350 5200
F 0 "C2" H 2465 5246 50  0000 L CNN
F 1 "1u" H 2465 5155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 2388 5050 50  0001 C CNN
F 3 "~" H 2350 5200 50  0001 C CNN
	1    2350 5200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 5D0A7EA8
P 1900 5200
F 0 "C1" H 2015 5246 50  0000 L CNN
F 1 "0.1u" H 2015 5155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 1938 5050 50  0001 C CNN
F 3 "~" H 1900 5200 50  0001 C CNN
	1    1900 5200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5D0A7EE4
P 2350 4800
F 0 "R2" H 2420 4846 50  0000 L CNN
F 1 "1k" H 2420 4755 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 2280 4800 50  0001 C CNN
F 3 "~" H 2350 4800 50  0001 C CNN
	1    2350 4800
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 5D0A7FB2
P 1500 5000
F 0 "SW1" H 1500 5285 50  0000 C CNN
F 1 "SW_Push" H 1500 5194 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_SPST_FSMSM" H 1500 5200 50  0001 C CNN
F 3 "" H 1500 5200 50  0001 C CNN
	1    1500 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2350 4950 2350 5000
Wire Wire Line
	1900 4950 1900 5000
Wire Wire Line
	1900 5000 2350 5000
Connection ~ 1900 5000
Wire Wire Line
	1900 5000 1900 5050
Connection ~ 2350 5000
Wire Wire Line
	2350 5000 2350 5050
Wire Wire Line
	2350 5000 2700 5000
Wire Wire Line
	1900 5000 1700 5000
Wire Wire Line
	1900 5350 1900 5400
Wire Wire Line
	2350 5350 2350 5400
Wire Wire Line
	1200 5400 1200 5000
Wire Wire Line
	1200 5000 1300 5000
$Comp
L power:GND #PWR01
U 1 1 5D0A954D
P 1200 5400
F 0 "#PWR01" H 1200 5150 50  0001 C CNN
F 1 "GND" H 1205 5227 50  0000 C CNN
F 2 "" H 1200 5400 50  0001 C CNN
F 3 "" H 1200 5400 50  0001 C CNN
	1    1200 5400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR04
U 1 1 5D0A9581
P 1900 5400
F 0 "#PWR04" H 1900 5150 50  0001 C CNN
F 1 "GND" H 1905 5227 50  0000 C CNN
F 2 "" H 1900 5400 50  0001 C CNN
F 3 "" H 1900 5400 50  0001 C CNN
	1    1900 5400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 5D0A95AE
P 2350 5400
F 0 "#PWR06" H 2350 5150 50  0001 C CNN
F 1 "GND" H 2355 5227 50  0000 C CNN
F 2 "" H 2350 5400 50  0001 C CNN
F 3 "" H 2350 5400 50  0001 C CNN
	1    2350 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 4650 1900 4600
Wire Wire Line
	2350 4650 2350 4350
Wire Wire Line
	2700 4350 2350 4350
Connection ~ 2350 4350
Wire Wire Line
	2350 4350 1200 4350
Wire Wire Line
	1200 4150 2700 4150
$Comp
L power:+3V3 #PWR03
U 1 1 5D0AAADB
P 1900 4600
F 0 "#PWR03" H 1900 4450 50  0001 C CNN
F 1 "+3V3" H 1900 4750 50  0000 C CNN
F 2 "" H 1900 4600 50  0001 C CNN
F 3 "" H 1900 4600 50  0001 C CNN
	1    1900 4600
	1    0    0    -1  
$EndComp
Text Label 2700 4350 0    50   ~ 0
JTAG_7
Text Label 2700 4150 0    50   ~ 0
JTAG_4
Text Label 1200 4150 2    50   ~ 0
C2D
Text Label 1200 4350 2    50   ~ 0
RST
$Comp
L Device:R R3
U 1 1 5D0AC660
P 4800 4700
F 0 "R3" H 4870 4746 50  0000 L CNN
F 1 "1k" H 4870 4655 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 4730 4700 50  0001 C CNN
F 3 "~" H 4800 4700 50  0001 C CNN
	1    4800 4700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR011
U 1 1 5D0ACBE8
P 3750 5400
F 0 "#PWR011" H 3750 5150 50  0001 C CNN
F 1 "GND" H 3755 5227 50  0000 C CNN
F 2 "" H 3750 5400 50  0001 C CNN
F 3 "" H 3750 5400 50  0001 C CNN
	1    3750 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 5200 3750 5200
Wire Wire Line
	3750 5200 3750 5400
Wire Wire Line
	3900 4900 3750 4900
Wire Wire Line
	3750 4900 3750 5200
Connection ~ 3750 5200
Wire Wire Line
	4400 4800 4550 4800
Wire Wire Line
	4550 4800 4550 4550
Wire Wire Line
	4550 4550 3750 4550
Wire Wire Line
	3750 4550 3750 4900
Connection ~ 3750 4900
Wire Wire Line
	3900 5000 3450 5000
Wire Wire Line
	3900 5100 3450 5100
Text Label 3450 5100 0    50   ~ 0
JTAG_7
Text Label 3450 5000 0    50   ~ 0
JTAG_5
Text Label 2700 5000 0    50   ~ 0
JTAG_5
Wire Wire Line
	4400 5000 4800 5000
Wire Wire Line
	4800 5000 4800 4850
Wire Wire Line
	4400 4900 4650 4900
Wire Wire Line
	4650 4900 4650 4400
Wire Wire Line
	4800 4550 4800 4400
Wire Wire Line
	4800 4400 4650 4400
Wire Wire Line
	4650 4400 3450 4400
Connection ~ 4650 4400
Wire Wire Line
	3900 4800 3450 4800
Wire Wire Line
	3450 4800 3450 4650
$Comp
L power:+3V3 #PWR09
U 1 1 5D0B6789
P 3450 4650
F 0 "#PWR09" H 3450 4500 50  0001 C CNN
F 1 "+3V3" H 3450 4800 50  0000 C CNN
F 2 "" H 3450 4650 50  0001 C CNN
F 3 "" H 3450 4650 50  0001 C CNN
	1    3450 4650
	1    0    0    -1  
$EndComp
Text Label 3450 4400 0    50   ~ 0
JTAG_4
NoConn ~ 4400 5100
NoConn ~ 4400 5200
$Comp
L power:+5V #PWR012
U 1 1 5D0BB19F
P 6250 3650
F 0 "#PWR012" H 6250 3500 50  0001 C CNN
F 1 "+5V" V 6250 3850 50  0000 C CNN
F 2 "" H 6250 3650 50  0001 C CNN
F 3 "" H 6250 3650 50  0001 C CNN
	1    6250 3650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6250 3650 6350 3650
Wire Wire Line
	6900 2750 6900 2650
$Comp
L power:+3V3 #PWR015
U 1 1 5D0BD3A1
P 6900 2650
F 0 "#PWR015" H 6900 2500 50  0001 C CNN
F 1 "+3V3" H 6900 2800 50  0000 C CNN
F 2 "" H 6900 2650 50  0001 C CNN
F 3 "" H 6900 2650 50  0001 C CNN
	1    6900 2650
	1    0    0    -1  
$EndComp
Text Label 6150 3300 0    50   ~ 0
C2D
Text Label 6150 3400 0    50   ~ 0
RST
Wire Wire Line
	6150 3300 6350 3300
Wire Wire Line
	6150 3400 6350 3400
Wire Wire Line
	10300 1000 10150 1000
Wire Wire Line
	10600 1000 10700 1000
$Comp
L Device:R R5
U 1 1 5D0CFEA9
P 10000 1250
F 0 "R5" V 9900 1200 50  0000 L CNN
F 1 "1k" V 10000 1200 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9930 1250 50  0001 C CNN
F 3 "~" H 10000 1250 50  0001 C CNN
	1    10000 1250
	0    1    1    0   
$EndComp
$Comp
L Device:LED D2
U 1 1 5D0CFEB0
P 10450 1250
F 0 "D2" H 10450 1150 50  0000 C CNN
F 1 "LED" H 10441 1375 50  0001 C CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 10450 1250 50  0001 C CNN
F 3 "~" H 10450 1250 50  0001 C CNN
	1    10450 1250
	-1   0    0    1   
$EndComp
Wire Wire Line
	10300 1250 10150 1250
Wire Wire Line
	9850 1000 9650 1000
Wire Wire Line
	10600 1250 10700 1250
Wire Wire Line
	9850 1250 9650 1250
Wire Wire Line
	10700 1000 10700 1250
Connection ~ 10700 1250
$Comp
L power:GND #PWR021
U 1 1 5D0D4CB2
P 10700 1650
F 0 "#PWR021" H 10700 1400 50  0001 C CNN
F 1 "GND" H 10705 1477 50  0000 C CNN
F 2 "" H 10700 1650 50  0001 C CNN
F 3 "" H 10700 1650 50  0001 C CNN
	1    10700 1650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R6
U 1 1 5D0D5119
P 10000 3100
F 0 "R6" V 9900 3050 50  0000 L CNN
F 1 "10k" V 10000 3050 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9930 3100 50  0001 C CNN
F 3 "~" H 10000 3100 50  0001 C CNN
	1    10000 3100
	-1   0    0    1   
$EndComp
Wire Wire Line
	10100 2850 10000 2850
Wire Wire Line
	10000 2850 10000 2950
$Comp
L power:GND #PWR019
U 1 1 5D0D72F0
P 10000 3350
F 0 "#PWR019" H 10000 3100 50  0001 C CNN
F 1 "GND" H 10005 3177 50  0000 C CNN
F 2 "" H 10000 3350 50  0001 C CNN
F 3 "" H 10000 3350 50  0001 C CNN
	1    10000 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	10000 3350 10000 3250
$Comp
L power:+5V #PWR022
U 1 1 5D0D84F1
P 10700 2700
F 0 "#PWR022" H 10700 2550 50  0001 C CNN
F 1 "+5V" V 10700 2900 50  0000 C CNN
F 2 "" H 10700 2700 50  0001 C CNN
F 3 "" H 10700 2700 50  0001 C CNN
	1    10700 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	10700 2700 10700 2850
Wire Wire Line
	10700 2850 10500 2850
$Comp
L Switch:SW_Push SW3
U 1 1 5D0DE1B7
P 10300 3850
F 0 "SW3" H 10300 4050 50  0000 C CNN
F 1 "SW_Push" H 10300 4044 50  0001 C CNN
F 2 "Button_Switch_SMD:SW_SPST_FSMSM" H 10300 4050 50  0001 C CNN
F 3 "" H 10300 4050 50  0001 C CNN
	1    10300 3850
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5D0DE1BE
P 10000 4100
F 0 "R7" V 9900 4050 50  0000 L CNN
F 1 "10k" V 10000 4050 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9930 4100 50  0001 C CNN
F 3 "~" H 10000 4100 50  0001 C CNN
	1    10000 4100
	-1   0    0    1   
$EndComp
Wire Wire Line
	10100 3850 10000 3850
Wire Wire Line
	10000 3850 10000 3950
$Comp
L power:GND #PWR020
U 1 1 5D0DE1C7
P 10000 4350
F 0 "#PWR020" H 10000 4100 50  0001 C CNN
F 1 "GND" H 10005 4177 50  0000 C CNN
F 2 "" H 10000 4350 50  0001 C CNN
F 3 "" H 10000 4350 50  0001 C CNN
	1    10000 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	10000 4350 10000 4250
$Comp
L power:+5V #PWR023
U 1 1 5D0DE1CE
P 10700 3700
F 0 "#PWR023" H 10700 3550 50  0001 C CNN
F 1 "+5V" V 10700 3900 50  0000 C CNN
F 2 "" H 10700 3700 50  0001 C CNN
F 3 "" H 10700 3700 50  0001 C CNN
	1    10700 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	10700 3700 10700 3850
Wire Wire Line
	10700 3850 10500 3850
Wire Wire Line
	9650 2850 10000 2850
Wire Wire Line
	9650 3850 10000 3850
$Comp
L Switch:SW_Push SW2
U 1 1 5D0E5FF3
P 10300 2850
F 0 "SW2" H 10300 3050 50  0000 C CNN
F 1 "SW_Push" H 10300 3044 50  0001 C CNN
F 2 "Button_Switch_SMD:SW_SPST_FSMSM" H 10300 3050 50  0001 C CNN
F 3 "" H 10300 3050 50  0001 C CNN
	1    10300 2850
	1    0    0    -1  
$EndComp
$Comp
L Device:C C5
U 1 1 5D0F08CE
P 7100 1350
F 0 "C5" H 7215 1396 50  0000 L CNN
F 1 "0.1u" H 7215 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 7138 1200 50  0001 C CNN
F 3 "~" H 7100 1350 50  0001 C CNN
	1    7100 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5D0F08D5
P 6650 1350
F 0 "C4" H 6765 1396 50  0000 L CNN
F 1 "0.1u" H 6765 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 6688 1200 50  0001 C CNN
F 3 "~" H 6650 1350 50  0001 C CNN
	1    6650 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 1500 6650 1550
Wire Wire Line
	7100 1500 7100 1550
$Comp
L power:GND #PWR014
U 1 1 5D0F08DE
P 6650 1550
F 0 "#PWR014" H 6650 1300 50  0001 C CNN
F 1 "GND" H 6655 1377 50  0000 C CNN
F 2 "" H 6650 1550 50  0001 C CNN
F 3 "" H 6650 1550 50  0001 C CNN
	1    6650 1550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR018
U 1 1 5D0F08E4
P 7100 1550
F 0 "#PWR018" H 7100 1300 50  0001 C CNN
F 1 "GND" H 7105 1377 50  0000 C CNN
F 2 "" H 7100 1550 50  0001 C CNN
F 3 "" H 7100 1550 50  0001 C CNN
	1    7100 1550
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR013
U 1 1 5D0F22DA
P 6650 1100
F 0 "#PWR013" H 6650 950 50  0001 C CNN
F 1 "+5V" H 6650 1250 50  0000 C CNN
F 2 "" H 6650 1100 50  0001 C CNN
F 3 "" H 6650 1100 50  0001 C CNN
	1    6650 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 1100 6650 1200
Wire Wire Line
	7100 1100 7100 1200
Wire Wire Line
	9850 5550 9550 5550
Wire Wire Line
	9850 5650 9550 5650
Wire Wire Line
	9850 5750 9550 5750
Text Label 9550 5550 0    50   ~ 0
P1.4
Text Label 9550 5650 0    50   ~ 0
P1.5
Text Label 9550 5750 0    50   ~ 0
P1.6
Text Label 9650 2850 2    50   ~ 0
P0.5
Text Label 9650 3850 2    50   ~ 0
P0.6
Wire Wire Line
	7650 3100 7450 3100
Wire Wire Line
	7450 3500 7650 3500
Text Label 7650 3500 2    50   ~ 0
P0.5
Wire Wire Line
	7450 3600 7650 3600
Text Label 7650 3600 2    50   ~ 0
P0.6
Wire Wire Line
	7650 4250 7450 4250
Wire Wire Line
	7650 4350 7450 4350
Wire Wire Line
	7650 4450 7450 4450
Text Label 7650 4250 2    50   ~ 0
P1.4
Text Label 7650 4350 2    50   ~ 0
P1.5
Text Label 7650 4450 2    50   ~ 0
P1.6
Connection ~ 10000 2850
Connection ~ 10000 3850
Wire Wire Line
	7650 3000 7450 3000
$Comp
L power:+3V3 #PWR017
U 1 1 5D0BBCC0
P 7100 1100
F 0 "#PWR017" H 7100 950 50  0001 C CNN
F 1 "+3V3" H 7100 1250 50  0000 C CNN
F 2 "" H 7100 1100 50  0001 C CNN
F 3 "" H 7100 1100 50  0001 C CNN
	1    7100 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	10700 1250 10700 1650
Wire Wire Line
	6350 3850 6150 3850
Wire Wire Line
	6350 3950 6150 3950
Text Label 6150 3850 0    50   ~ 0
P2.7
Text Label 6150 3950 0    50   ~ 0
P2.6
Text Label 9650 1000 2    50   ~ 0
P2.7
Text Label 9650 1250 2    50   ~ 0
P2.6
Text Label 7650 3100 2    50   ~ 0
RX1
Text Label 7650 3000 2    50   ~ 0
TX1
Wire Wire Line
	9850 5250 9550 5250
Wire Wire Line
	9850 5850 9550 5850
$Comp
L power:GND #PWR0101
U 1 1 5D217795
P 9550 5950
F 0 "#PWR0101" H 9550 5700 50  0001 C CNN
F 1 "GND" H 9555 5777 50  0000 C CNN
F 2 "" H 9550 5950 50  0001 C CNN
F 3 "" H 9550 5950 50  0001 C CNN
	1    9550 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	9550 5850 9550 5950
$Comp
L power:+5V #PWR0102
U 1 1 5D21BCBD
P 9550 5150
F 0 "#PWR0102" H 9550 5000 50  0001 C CNN
F 1 "+5V" H 9565 5323 50  0000 C CNN
F 2 "" H 9550 5150 50  0001 C CNN
F 3 "" H 9550 5150 50  0001 C CNN
	1    9550 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9550 5150 9550 5250
$Comp
L F38C_U2S-rescue:USB_B-Connector J1
U 1 1 5D335BFB
P 1600 1700
F 0 "J1" H 1657 2167 50  0000 C CNN
F 1 "USB_B" H 1657 2076 50  0000 C CNN
F 2 "Connector_USB:USB_B_OST_USB-B1HSxx_Horizontal" H 1750 1650 50  0001 C CNN
F 3 " ~" H 1750 1650 50  0001 C CNN
	1    1600 1700
	1    0    0    -1  
$EndComp
Text Label 2400 1500 0    50   ~ 0
TXD
Text Label 2400 1600 0    50   ~ 0
RXD
Text Label 2050 1800 0    50   ~ 0
D-
Text Label 2050 1700 0    50   ~ 0
D+
$Comp
L power:GND #PWR010
U 1 1 5D0A7623
P 3650 2250
F 0 "#PWR010" H 3650 2000 50  0001 C CNN
F 1 "GND" H 3655 2077 50  0000 C CNN
F 2 "" H 3650 2250 50  0001 C CNN
F 3 "" H 3650 2250 50  0001 C CNN
	1    3650 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 2250 3650 2050
Wire Wire Line
	3650 1600 3350 1600
Wire Wire Line
	3650 1750 3650 1600
$Comp
L Device:C C3
U 1 1 5D0A735E
P 3650 1900
F 0 "C3" H 3765 1946 50  0000 L CNN
F 1 "0.1u" H 3765 1855 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 3688 1750 50  0001 C CNN
F 3 "~" H 3650 1900 50  0001 C CNN
	1    3650 1900
	1    0    0    -1  
$EndComp
NoConn ~ 3350 1900
NoConn ~ 3350 1800
NoConn ~ 3350 1700
Wire Wire Line
	2550 1600 2400 1600
Wire Wire Line
	2550 1500 2400 1500
Wire Wire Line
	3450 1500 3350 1500
Wire Wire Line
	3450 1400 3450 1500
$Comp
L power:+5V #PWR08
U 1 1 5D0A6C94
P 3450 1400
F 0 "#PWR08" H 3450 1250 50  0001 C CNN
F 1 "+5V" H 3465 1573 50  0000 C CNN
F 2 "" H 3450 1400 50  0001 C CNN
F 3 "" H 3450 1400 50  0001 C CNN
	1    3450 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 1900 2400 2250
Wire Wire Line
	2550 1900 2400 1900
$Comp
L power:GND #PWR07
U 1 1 5D0A6B04
P 2400 2250
F 0 "#PWR07" H 2400 2000 50  0001 C CNN
F 1 "GND" H 2405 2077 50  0000 C CNN
F 2 "" H 2400 2250 50  0001 C CNN
F 3 "" H 2400 2250 50  0001 C CNN
	1    2400 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 1800 2550 1800
Wire Wire Line
	1900 1700 2550 1700
$Comp
L F38C_U2S-rescue:CH340E-My_symbols U1
U 1 1 5D0A6882
P 2550 1500
F 0 "U1" H 2950 1725 50  0000 C CNN
F 1 "CH340E" H 2950 1634 50  0000 C CNN
F 2 "Package_SO:MSOP-10_3x3mm_P0.5mm" H 2650 1000 50  0001 L CNN
F 3 "http://www.datasheet5.com/pdf-local-2195953" H 2600 1900 50  0001 C CNN
	1    2550 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 2100 1600 2250
Wire Wire Line
	2000 1500 1900 1500
Wire Wire Line
	2000 1400 2000 1500
$Comp
L power:GND #PWR02
U 1 1 5D08F94A
P 1600 2250
F 0 "#PWR02" H 1600 2000 50  0001 C CNN
F 1 "GND" H 1605 2077 50  0000 C CNN
F 2 "" H 1600 2250 50  0001 C CNN
F 3 "" H 1600 2250 50  0001 C CNN
	1    1600 2250
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR05
U 1 1 5D08F8FA
P 2000 1400
F 0 "#PWR05" H 2000 1250 50  0001 C CNN
F 1 "+5V" H 2015 1573 50  0000 C CNN
F 2 "" H 2000 1400 50  0001 C CNN
F 3 "" H 2000 1400 50  0001 C CNN
	1    2000 1400
	1    0    0    -1  
$EndComp
Wire Notes Line
	8350 600  8350 2200
Wire Notes Line
	8350 2200 11100 2200
Wire Notes Line
	11100 2300 8350 2300
Wire Notes Line
	8350 2300 8350 4800
Wire Notes Line
	8350 4800 11100 4800
Wire Notes Line
	11100 4900 8350 4900
Wire Notes Line
	8350 4900 8350 6400
Wire Notes Line
	5400 3400 600  3400
Wire Notes Line
	600  3400 600  6400
Wire Notes Line
	600  6400 5400 6400
Wire Notes Line
	5400 6400 5400 3400
Wire Notes Line
	5400 3300 5400 600 
Wire Notes Line
	5400 600  600  600 
Wire Notes Line
	600  600  600  3300
Wire Notes Line
	600  3300 5400 3300
Wire Notes Line
	5500 600  8250 600 
Wire Notes Line
	8250 600  8250 6400
Wire Notes Line
	8250 6400 5500 6400
Wire Notes Line
	5500 6400 5500 600 
Wire Notes Line
	8350 600  11100 600 
Wire Notes Line
	11100 600  11100 2200
Wire Notes Line
	11100 2300 11100 4800
Wire Notes Line
	11100 4900 11100 6400
Wire Notes Line
	11100 6400 8350 6400
Text Notes 650  6350 0    200  ~ 0
Interface de programmation
Text Notes 650  3250 0    200  ~ 0
Interface UART-SERIAL
Text Notes 5550 6250 0    200  ~ 0
MicroControlleur
Text Notes 5600 6350 0    50   ~ 0
+ découplage
Text Notes 8400 2150 0    200  ~ 0
LED
Text Notes 8400 4750 0    200  ~ 0
Push Button
Text Notes 8400 6350 0    200  ~ 0
Pin Paramètrable\n
Text Label 4150 1500 0    50   ~ 0
TXD
Text Label 4150 1600 0    50   ~ 0
RXD
Wire Wire Line
	4850 1600 4150 1600
Wire Wire Line
	4850 1500 4150 1500
Text Label 4850 1600 2    50   ~ 0
TX1
Text Label 4850 1500 2    50   ~ 0
RX1
Text Label 6100 3000 0    50   ~ 0
D-_uC
Text Label 6100 3100 0    50   ~ 0
D+_uC
Wire Wire Line
	6100 3000 6350 3000
Wire Wire Line
	6100 3100 6350 3100
$Comp
L Connector:Conn_01x07_Male J3
U 1 1 6038ED0C
P 10050 5550
F 0 "J3" H 10022 5574 50  0000 R CNN
F 1 "Conn_01x07_Male" H 10022 5483 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x07_P2.54mm_Vertical" H 10050 5550 50  0001 C CNN
F 3 "~" H 10050 5550 50  0001 C CNN
	1    10050 5550
	-1   0    0    -1  
$EndComp
Wire Wire Line
	9850 5350 9550 5350
Wire Wire Line
	9850 5450 9550 5450
Text Label 9550 5450 0    50   ~ 0
D-_uC
Text Label 9550 5350 0    50   ~ 0
D+_uC
$EndSCHEMATC
